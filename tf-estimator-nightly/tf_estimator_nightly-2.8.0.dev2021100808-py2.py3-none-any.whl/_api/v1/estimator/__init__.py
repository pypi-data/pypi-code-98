# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Estimator: High level tools for working with models.
"""

import sys as _sys

from tensorflow_estimator._api.v1.estimator import experimental
from tensorflow_estimator._api.v1.estimator import export
from tensorflow_estimator._api.v1.estimator import inputs
from tensorflow_estimator._api.v1.estimator import tpu
from tensorflow_estimator.python.estimator.canned.baseline import BaselineClassifier
from tensorflow_estimator.python.estimator.canned.baseline import BaselineEstimator
from tensorflow_estimator.python.estimator.canned.baseline import BaselineRegressor
from tensorflow_estimator.python.estimator.canned.baseline import ModeKeys
from tensorflow_estimator.python.estimator.canned.boosted_trees import BoostedTreesClassifier
from tensorflow_estimator.python.estimator.canned.boosted_trees import BoostedTreesEstimator
from tensorflow_estimator.python.estimator.canned.boosted_trees import BoostedTreesRegressor
from tensorflow_estimator.python.estimator.canned.dnn import DNNClassifier
from tensorflow_estimator.python.estimator.canned.dnn import DNNEstimator
from tensorflow_estimator.python.estimator.canned.dnn import DNNRegressor
from tensorflow_estimator.python.estimator.canned.dnn_linear_combined import DNNLinearCombinedClassifier
from tensorflow_estimator.python.estimator.canned.dnn_linear_combined import DNNLinearCombinedEstimator
from tensorflow_estimator.python.estimator.canned.dnn_linear_combined import DNNLinearCombinedRegressor
from tensorflow_estimator.python.estimator.canned.linear import LinearClassifier
from tensorflow_estimator.python.estimator.canned.linear import LinearEstimator
from tensorflow_estimator.python.estimator.canned.linear import LinearRegressor
from tensorflow_estimator.python.estimator.canned.parsing_utils import classifier_parse_example_spec
from tensorflow_estimator.python.estimator.canned.parsing_utils import regressor_parse_example_spec
from tensorflow_estimator.python.estimator.estimator import Estimator
from tensorflow_estimator.python.estimator.estimator import VocabInfo
from tensorflow_estimator.python.estimator.estimator import WarmStartSettings
from tensorflow_estimator.python.estimator.exporter import BestExporter
from tensorflow_estimator.python.estimator.exporter import Exporter
from tensorflow_estimator.python.estimator.exporter import FinalExporter
from tensorflow_estimator.python.estimator.exporter import LatestExporter
from tensorflow_estimator.python.estimator.extenders import add_metrics
from tensorflow_estimator.python.estimator.head.base_head import Head
from tensorflow_estimator.python.estimator.head.binary_class_head import BinaryClassHead
from tensorflow_estimator.python.estimator.head.multi_class_head import MultiClassHead
from tensorflow_estimator.python.estimator.head.multi_head import MultiHead
from tensorflow_estimator.python.estimator.head.multi_label_head import MultiLabelHead
from tensorflow_estimator.python.estimator.head.regression_head import LogisticRegressionHead
from tensorflow_estimator.python.estimator.head.regression_head import PoissonRegressionHead
from tensorflow_estimator.python.estimator.head.regression_head import RegressionHead
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import CheckpointSaverHook
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import CheckpointSaverListener
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import FeedFnHook
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import FinalOpsHook
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import GlobalStepWaiterHook
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import LoggingTensorHook
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import NanLossDuringTrainingError
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import NanTensorHook
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import ProfilerHook
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import SecondOrStepTimer
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import StepCounterHook
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import StopAtStepHook
from tensorflow_estimator.python.estimator.hooks.basic_session_run_hooks import SummarySaverHook
from tensorflow_estimator.python.estimator.hooks.session_run_hook import SessionRunArgs
from tensorflow_estimator.python.estimator.hooks.session_run_hook import SessionRunContext
from tensorflow_estimator.python.estimator.hooks.session_run_hook import SessionRunHook
from tensorflow_estimator.python.estimator.hooks.session_run_hook import SessionRunValues
from tensorflow_estimator.python.estimator.model_fn import EstimatorSpec
from tensorflow_estimator.python.estimator.run_config import RunConfig
from tensorflow_estimator.python.estimator.training import EvalSpec
from tensorflow_estimator.python.estimator.training import TrainSpec
from tensorflow_estimator.python.estimator.training import train_and_evaluate
from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "estimator", public_apis=None, deprecation=True,
      has_lite=False)
