import tensorflow as tf
from tensorflow import keras
import tensorflow.keras.backend as K


class SAMModel(tf.keras.models.Model):
    """
    Arxiv article: [Sharpness-Aware Minimization for Efficiently Improving Generalization](https://arxiv.org/pdf/2010.01412.pdf)
    Implementation by: [Keras SAM (Sharpness-Aware Minimization)](https://qiita.com/T-STAR/items/8c3afe3a116a8fc08429)

    Usage is same with `keras.modeols.Model`: `model = SAMModel(inputs, outputs, rho=sam_rho, name=name)`
    """

    def __init__(self, *args, rho=0.05, **kwargs):
        super().__init__(*args, **kwargs)
        self.rho = tf.constant(rho, dtype=tf.float32)

    def train_step(self, data):
        if len(data) == 3:
            x, y, sample_weight = data
        else:
            sample_weight = None
            x, y = data

        # 1st step
        with tf.GradientTape() as tape:
            y_pred = self(x, training=True)
            loss = self.compiled_loss(y, y_pred, sample_weight=sample_weight, regularization_losses=self.losses)

        trainable_vars = self.trainable_variables
        gradients = tape.gradient(loss, trainable_vars)

        norm = tf.linalg.global_norm(gradients)
        scale = self.rho / (norm + 1e-12)
        e_w_list = []
        for v, grad in zip(trainable_vars, gradients):
            e_w = grad * scale
            v.assign_add(e_w)
            e_w_list.append(e_w)

        # 2nd step
        with tf.GradientTape() as tape:
            y_pred_adv = self(x, training=True)
            loss_adv = self.compiled_loss(y, y_pred_adv, sample_weight=sample_weight, regularization_losses=self.losses)
        gradients_adv = tape.gradient(loss_adv, trainable_vars)
        for v, e_w in zip(trainable_vars, e_w_list):
            v.assign_sub(e_w)

        # optimize
        self.optimizer.apply_gradients(zip(gradients_adv, trainable_vars))

        self.compiled_metrics.update_state(y, y_pred, sample_weight=sample_weight)
        return_metrics = {}
        for metric in self.metrics:
            result = metric.result()
            if isinstance(result, dict):
                return_metrics.update(result)
            else:
                return_metrics[metric.name] = result
        return return_metrics


@keras.utils.register_keras_serializable(package="model_surgery")
class DropConnect(keras.layers.Layer):
    def __init__(self, rate=0, **kwargs):
        super(DropConnect, self).__init__(**kwargs)
        self.rate = rate
        self.supports_masking = False

    def build(self, input_shape):
        if self.rate > 0:
            noise_shape = [None] + [1] * (len(input_shape) - 1)  # [None, 1, 1, 1]
            self.drop = keras.layers.Dropout(self.rate, noise_shape=noise_shape, name=self.name + "drop")
        else:
            self.drop = lambda xx: xx

    def call(self, inputs, **kwargs):
        shortcut, deep = inputs
        deep = self.drop(deep)
        return keras.layers.Add()([shortcut, deep])

    def get_config(self):
        config = super(DropConnect, self).get_config()
        config.update({"rate": self.rate})
        return config


def add_l2_regularizer_2_model(model, weight_decay, custom_objects={}, apply_to_batch_normal=False, apply_to_bias=False):
    # https://github.com/keras-team/keras/issues/2717#issuecomment-456254176
    if 0:
        regularizers_type = {}
        for layer in model.layers:
            rrs = [kk for kk in layer.__dict__.keys() if "regularizer" in kk and not kk.startswith("_")]
            if len(rrs) != 0:
                # print(layer.name, layer.__class__.__name__, rrs)
                if layer.__class__.__name__ not in regularizers_type:
                    regularizers_type[layer.__class__.__name__] = rrs
        print(regularizers_type)

    for layer in model.layers:
        attrs = []
        if isinstance(layer, keras.layers.Dense) or isinstance(layer, keras.layers.Conv2D):
            # print(">>>> Dense or Conv2D", layer.name, "use_bias:", layer.use_bias)
            attrs = ["kernel_regularizer"]
            if apply_to_bias and layer.use_bias:
                attrs.append("bias_regularizer")
        elif isinstance(layer, keras.layers.DepthwiseConv2D):
            # print(">>>> DepthwiseConv2D", layer.name, "use_bias:", layer.use_bias)
            attrs = ["depthwise_regularizer"]
            if apply_to_bias and layer.use_bias:
                attrs.append("bias_regularizer")
        elif isinstance(layer, keras.layers.SeparableConv2D):
            # print(">>>> SeparableConv2D", layer.name, "use_bias:", layer.use_bias)
            attrs = ["pointwise_regularizer", "depthwise_regularizer"]
            if apply_to_bias and layer.use_bias:
                attrs.append("bias_regularizer")
        elif apply_to_batch_normal and isinstance(layer, keras.layers.BatchNormalization):
            # print(">>>> BatchNormalization", layer.name, "scale:", layer.scale, ", center:", layer.center)
            if layer.center:
                attrs.append("beta_regularizer")
            if layer.scale:
                attrs.append("gamma_regularizer")
        elif apply_to_batch_normal and isinstance(layer, keras.layers.PReLU):
            # print(">>>> PReLU", layer.name)
            attrs = ["alpha_regularizer"]

        for attr in attrs:
            if hasattr(layer, attr) and layer.trainable:
                setattr(layer, attr, keras.regularizers.L2(weight_decay / 2))

    # So far, the regularizers only exist in the model config. We need to
    # reload the model so that Keras adds them to each layer's losses.
    # temp_weight_file = "tmp_weights.h5"
    # model.save_weights(temp_weight_file)
    # out_model = keras.models.model_from_json(model.to_json(), custom_objects=custom_objects)
    # out_model.load_weights(temp_weight_file, by_name=True)
    # os.remove(temp_weight_file)
    # return out_model
    return keras.models.clone_model(model)


def replace_ReLU(model, target_activation="PReLU", **kwargs):
    from tensorflow.keras.layers import ReLU, PReLU, Activation

    def convert_ReLU(layer):
        # print(layer.name)
        if isinstance(layer, ReLU) or (isinstance(layer, Activation) and layer.activation == keras.activations.relu):
            if target_activation == "PReLU":
                layer_name = layer.name.replace("_relu", "_prelu")
                print(">>>> Convert ReLU:", layer.name, "-->", layer_name)
                # Default initial value in mxnet and pytorch is 0.25
                return PReLU(shared_axes=[1, 2], alpha_initializer=tf.initializers.Constant(0.25), name=layer_name, **kwargs)
            elif isinstance(target_activation, str):
                layer_name = layer.name.replace("_relu", "_" + target_activation)
                print(">>>> Convert ReLU:", layer.name, "-->", layer_name)
                return Activation(activation=target_activation, name=layer_name, **kwargs)
            else:
                act_class_name = target_activation.__name__
                layer_name = layer.name.replace("_relu", "_" + act_class_name)
                print(">>>> Convert ReLU:", layer.name, "-->", layer_name)
                return target_activation(**kwargs)
        return layer

    input_tensors = keras.layers.Input(model.input_shape[1:])
    return keras.models.clone_model(model, input_tensors=input_tensors, clone_function=convert_ReLU)


def replace_add_with_stochastic_depth(model, survivals=(1, 0.8)):
    """
    - [Deep Networks with Stochastic Depth](https://arxiv.org/pdf/1603.09382.pdf)
    - [tfa.layers.StochasticDepth](https://www.tensorflow.org/addons/api_docs/python/tfa/layers/StochasticDepth)
    """
    from tensorflow_addons.layers import StochasticDepth

    add_layers = [ii.name for ii in model.layers if isinstance(ii, keras.layers.Add)]
    total_adds = len(add_layers)
    if isinstance(survivals, float):
        survivals = [survivals] * total_adds
    elif isinstance(survivals, (list, tuple)) and len(survivals) == 2:
        start, end = survivals
        survivals = [start - (1 - end) * float(ii) / total_adds for ii in range(total_adds)]
    survivals_dict = dict(zip(add_layers, survivals))

    def __replace_add_with_stochastic_depth__(layer):
        if isinstance(layer, keras.layers.Add):
            layer_name = layer.name
            new_layer_name = layer_name.replace("_add", "_stochastic_depth")
            new_layer_name = new_layer_name.replace("add_", "stochastic_depth_")
            survival_probability = survivals_dict[layer_name]
            if survival_probability < 1:
                print("Converting:", layer_name, "-->", new_layer_name, ", survival_probability:", survival_probability)
                return StochasticDepth(survival_probability, name=new_layer_name)
            else:
                return layer
        return layer

    input_tensors = keras.layers.Input(model.input_shape[1:])
    return keras.models.clone_model(model, input_tensors=input_tensors, clone_function=__replace_add_with_stochastic_depth__)


def replace_add_with_drop_connect(model, drop_rate=(0, 0.2)):
    """
    - [Deep Networks with Stochastic Depth](https://arxiv.org/pdf/1603.09382.pdf)
    - [tfa.layers.StochasticDepth](https://www.tensorflow.org/addons/api_docs/python/tfa/layers/StochasticDepth)
    """

    add_layers = [ii.name for ii in model.layers if isinstance(ii, keras.layers.Add)]
    total_adds = len(add_layers)
    if isinstance(drop_rate, float):
        drop_rates = [drop_rate] * total_adds
    elif isinstance(drop_rate, (list, tuple)) and len(drop_rate) == 2:
        start, end = drop_rate
        drop_rates = [(end - start) * float(ii) / total_adds for ii in range(total_adds)]
    drop_conn_rate_dict = dict(zip(add_layers, drop_rates))

    def __replace_add_with_stochastic_depth__(layer):
        if isinstance(layer, keras.layers.Add):
            layer_name = layer.name
            new_layer_name = layer_name.replace("_add", "_drop_conn")
            new_layer_name = new_layer_name.replace("add_", "drop_conn_")
            drop_conn_rate = drop_conn_rate_dict[layer_name]
            if drop_conn_rate < 1:
                print("Converting:", layer_name, "-->", new_layer_name, ", drop_conn_rate:", drop_conn_rate)
                return DropConnect(drop_conn_rate, name=new_layer_name)
            else:
                return layer
        return layer

    input_tensors = keras.layers.Input(model.input_shape[1:])
    return keras.models.clone_model(model, input_tensors=input_tensors, clone_function=__replace_add_with_stochastic_depth__)


def replace_stochastic_depth_with_add(model, drop_survival=False):
    from tensorflow_addons.layers import StochasticDepth

    def __replace_stochastic_depth_with_add__(layer):
        if isinstance(layer, StochasticDepth):
            layer_name = layer.name
            new_layer_name = layer_name.replace("_stochastic_depth", "_lambda")
            survival = layer.survival_probability
            print("Converting:", layer_name, "-->", new_layer_name, ", survival_probability:", survival)
            if drop_survival or not survival < 1:
                return keras.layers.Add(name=new_layer_name)
            else:
                return keras.layers.Lambda(lambda xx: xx[0] + xx[1] * survival, name=new_layer_name)
        return layer

    input_tensors = keras.layers.Input(model.input_shape[1:])
    return keras.models.clone_model(model, input_tensors=input_tensors, clone_function=__replace_stochastic_depth_with_add__)


def get_actual_survival_probabilities(model):
    from tensorflow_addons.layers import StochasticDepth

    return [ii.survival_probability for ii in model.layers if isinstance(ii, StochasticDepth)]


def get_actual_drop_connect_rates(model):
    return [ii.rate for ii in model.layers if isinstance(ii, keras.layers.Dropout) or isinstance(ii, DropConnect)]


def convert_to_mixed_float16(model, convert_batch_norm=False):
    policy = keras.mixed_precision.Policy("mixed_float16")
    policy_config = keras.utils.serialize_keras_object(policy)
    from tensorflow.keras.layers import InputLayer, Activation
    from tensorflow.keras.activations import linear

    def do_convert_to_mixed_float16(layer):
        if not convert_batch_norm and isinstance(layer, keras.layers.BatchNormalization):
            return layer
        if not isinstance(layer, InputLayer) and not (isinstance(layer, Activation) and layer.activation == linear):
            aa = layer.get_config()
            aa.update({"dtype": policy_config})
            bb = layer.__class__.from_config(aa)
            bb.build(layer.input_shape)
            bb.set_weights(layer.get_weights())
            return bb
        return layer

    input_tensors = keras.layers.Input(model.input_shape[1:])
    return keras.models.clone_model(model, input_tensors=input_tensors, clone_function=do_convert_to_mixed_float16)


def convert_mixed_float16_to_float32(model):
    from tensorflow.keras.layers import InputLayer, Activation
    from tensorflow.keras.activations import linear

    def do_convert_to_mixed_float16(layer):
        if not isinstance(layer, InputLayer) and not (isinstance(layer, Activation) and layer.activation == linear):
            aa = layer.get_config()
            aa.update({"dtype": "float32"})
            bb = layer.__class__.from_config(aa)
            bb.build(layer.input_shape)
            bb.set_weights(layer.get_weights())
            return bb
        return layer

    input_tensors = keras.layers.Input(model.input_shape[1:])
    return keras.models.clone_model(model, input_tensors=input_tensors, clone_function=do_convert_to_mixed_float16)


def fuse_conv_bn(conv_layer, bn_layer):
    # BatchNormalization returns: gamma * (batch - self.moving_mean) / sqrt(self.moving_var + epsilon) + beta
    # --> conv_w_new = gamma * conv_w / np.sqrt(var + epsilon)
    # --> conv_b_new = gamma * (conv_b - mean) / sqrt(var + epsilon) + beta
    batch_std = tf.sqrt(bn_layer.moving_variance + bn_layer.epsilon)
    if isinstance(conv_layer, keras.layers.DepthwiseConv2D):
        ww = tf.transpose(conv_layer.depthwise_kernel, [0, 1, 3, 2]) * bn_layer.gamma / batch_std
        ww = tf.transpose(ww, [0, 1, 3, 2])
    else:
        ww = conv_layer.kernel * bn_layer.gamma / batch_std

    if conv_layer.use_bias:
        bias = bn_layer.gamma * (conv_layer.bias - bn_layer.moving_mean) / batch_std + bn_layer.beta
    else:
        bias = bn_layer.gamma * (-1 * bn_layer.moving_mean) / batch_std + bn_layer.beta

    cc = conv_layer.get_config()
    cc["use_bias"] = True
    fused_conv_bn = conv_layer.__class__.from_config(cc)
    fused_conv_bn.build(conv_layer.input_shape)
    fused_conv_bn.set_weights([ww, bias])
    return fused_conv_bn


def convert_to_fused_conv_bn_model(model):
    """
    Convert model by fusing Conv + batchnorm

    Exampls:
    >>> from keras_cv_attention_models import model_surgery
    >>> mm = keras.applications.ResNet50()
    >>> bb = model_surgery.convert_to_fused_conv_bn_model(mm)
    """
    import json

    """ Check bn layers with conv layer input """
    model_config = json.loads(model.to_json())
    ee = {layer["name"]: layer for layer in model_config["config"]["layers"]}
    fuse_convs, fuse_bns = [], []
    conv_names = ["Conv2D", "DepthwiseConv2D"]
    for layer in model_config["config"]["layers"]:
        if layer["class_name"] == "BatchNormalization" and len(layer["inbound_nodes"]) == 1:
            input_node = layer["inbound_nodes"][0][0]
            if isinstance(input_node, list) and ee.get(input_node[0], {"class_name": None})["class_name"] in conv_names:
                fuse_convs.append(input_node[0])
                fuse_bns.append(layer["name"])
    print(">>>> len(fuse_convs) =", len(fuse_convs), "len(fuse_bns) =", len(fuse_bns))
    # len(fuse_convs) = 53, len(fuse_bns) = 53

    """ Create new model config """
    layers = []
    fused_bn_dict = dict(zip(fuse_bns, fuse_convs))
    fused_conv_dict = dict(zip(fuse_convs, fuse_bns))
    for layer in model_config["config"]["layers"]:
        if layer["name"] in fuse_convs:
            print(">>>> Fuse conv bn:", layer["name"])
            layer["config"]["use_bias"] = True
        elif layer["name"] in fuse_bns:
            continue

        if len(layer["inbound_nodes"]) != 0:
            for ii in layer["inbound_nodes"][0]:
                if isinstance(ii, list) and ii[0] in fused_bn_dict:
                    print(">>>> Replace inbound_nodes: {}, {} --> {}".format(layer["name"], ii[0], fused_bn_dict[ii[0]]))
                    ii[0] = fused_bn_dict[ii[0]]
        layers.append(layer)
    model_config["config"]["layers"] = layers
    new_model = keras.models.model_from_json(json.dumps(model_config))

    """ New model set layer weights by layer names """
    for layer in new_model.layers:
        if layer.name in fuse_bns:  # This should not happen
            continue

        orign_layer = model.get_layer(layer.name)
        if layer.name in fused_conv_dict:
            orign_bn_layer = model.get_layer(fused_conv_dict[layer.name])
            print(">>>> Fuse conv bn", layer.name, orign_bn_layer.name)
            conv_bn = fuse_conv_bn(orign_layer, orign_bn_layer)
            layer.set_weights(conv_bn.get_weights())
        else:
            layer.set_weights(orign_layer.get_weights())
    return new_model
