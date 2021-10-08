"""Sensitivity testing, for fairness and robustness."""


from typing import Iterator, Union, List, Optional, Tuple

from instancelib.analysis.base import label_metrics, BinaryModelMetrics, MulticlassModelMetrics
from instancelib.environment.text import TextEnvironment
from instancelib.instances.base import InstanceProvider
from instancelib.instances.text import MemoryTextInstance, TextInstanceProvider
from instancelib.labels.memory import MemoryLabelProvider
from instancelib.machinelearning.base import AbstractClassifier
from instancelib.typehints import LT

from text_sensitivity.data.random.string import RandomString, combine_generators
from text_sensitivity.perturbation.base import Perturbation


def apply_perturbation(dataset: Union[InstanceProvider, TextEnvironment],
                       perturbation: Perturbation) -> Tuple[TextInstanceProvider, MemoryLabelProvider]:
    """Apply a perturbation to a dataset, getting the perturbed instances and corresponding attribute labels.

    Examples:
        Repeat each string twice:

        >>> from text_sensitivity.perturbation.sentences import repeat_k_times
        >>> apply_perturbation(env, repeat_k_times(k=2))

        Add the unrelated string 'This is unrelated.' before each instance:

        >>> from text_sensitivity.perturbation import OneToOnePerturbation
        >>> perturbation = OneToOnePerturbation.from_string(prefix='This is unrelated.')
        >>> apply_perturbation(env, perturbation)

    Args:
        dataset (Union[InstanceProvider, TextEnvironment]): Dataset to apply perturbation to (e.g. all data, train set,
            test set, set belonging to a given label, or subset of data for a (un)protected group).
        perturbation (Perturbation): Perturbation to apply, one-to-one or one-to-many.

    Returns:
        Tuple[TextInstanceProvider, MemoryLabelProvider]: Perturbed instances and corresponding attribute labels.
    """
    if isinstance(dataset, TextEnvironment):
        dataset = dataset.dataset
    if not isinstance(perturbation, Perturbation):
        perturbation = perturbation()

    new_data, attributes = [], []

    for key in dataset:
        for instances, labels in perturbation(dataset[key]):
            new_data.extend(instances) if isinstance(instances, list) else new_data.append(instances)
            attributes.extend(labels) if isinstance(labels, list) else attributes.append(labels)

    instanceprovider = TextInstanceProvider(new_data)
    instanceprovider.add_range(*dataset.dataset.get_all())
    labelprovider = MemoryLabelProvider.from_tuples(attributes)

    return instanceprovider, labelprovider


def equal_ground_truth(ground_truth, instances):
    # TODO: add ability to provide a different expectation of what will happen to the instance labels after perturbation
    for key in instances.keys():
        parent_key = key.split('|')[0] if isinstance(key, str) else str(key)
        parent_key = int(parent_key) if parent_key.isdigit() else parent_key
        yield (key, ground_truth._labeldict[parent_key])


def compare_metric(env: TextEnvironment,
                   model: AbstractClassifier,
                   perturbation: Perturbation
                   ) -> Iterator[Tuple[LT, LT, Union[BinaryModelMetrics, MulticlassModelMetrics]]]:
    """Get metrics for each ground-truth label and attribute.

    Examples:
        Compare metric of `model` performance (e.g. accuracy, precision) before and after mapping each instance in a 
        dataset to uppercase.

        >>> from text_sensitivity.perturbation.sentences import to_upper
        >>> compare_metric(env, model, to_upper)

        Compare metric when randomly adding 10 perturbed instances with typos to each instance in a dataset.

        >>> from text_sensitivity.perturbation.characters import add_typos
        >>> compare_metric(env, model, add_typos(n=10))

    Args:
        env (TextEnvironment): Environment containing original instances (`.dataset`)
            and ground-truth labels (`.labels`).
        model (AbstractClassifier): Black-box model to compare metrics on.
        perturbation (Perturbation): Peturbation to apply.

    Yields:
        Iterator[Sequence[Tuple[LT, LT, Union[BinaryModelMetrics, MulticlassModelMetrics]]]]: Original label (before
            perturbation), perturbed label (after perturbation) and metrics for label-attribute pair.
    """
    # Apply perturbations and get attributes
    instances, attributes = apply_perturbation(env, perturbation)

    # Perform prediction on original instances and perturbed instances
    model_predictions = MemoryLabelProvider.from_tuples(model.predict(instances))

    # Expectation (for now that labels should remain equal)
    ground_truth = MemoryLabelProvider.from_tuples(equal_ground_truth(env.labels, instances))

    for label in list(model_predictions.labelset):
        for attribute in list(attributes.labelset):
            metrics = label_metrics(model_predictions,
                                    ground_truth,
                                    attributes.get_instances_by_label(attribute),
                                    label)
            yield label, attribute, metrics


def compare_accuracy(*args, **kwargs):
    """Compare accuracy scores for each ground-truth label and attribute."""
    import pandas as pd
    return pd.DataFrame([(label, attribute, metrics.accuracy)
                         for label, attribute, metrics in compare_metric(*args, **kwargs)],
                        columns=['label', 'attribute', 'accuracy'])


def compare_precision(*args, **kwargs):
    """Compare precision scores for each ground-truth label and attribute."""
    import pandas as pd
    return pd.DataFrame([(label, attribute, metrics.precision)
                         for label, attribute, metrics in compare_metric(*args, **kwargs)],
                        columns=['label', 'attribute', 'precision'])


def compare_recall(*args, **kwargs):
    """Compare recall scores for each ground-truth label and attribute."""
    import pandas as pd
    return pd.DataFrame([(label, attribute, metrics.recall)
                         for label, attribute, metrics in compare_metric(*args, **kwargs)],
                        columns=['label', 'attribute', 'recall'])


def input_space_robustness(model: AbstractClassifier,
                           generators: List[RandomString],
                           n_samples: int = 100,
                           min_length: int = 0,
                           max_length: int = 100,
                           seed: Optional[int] = 0) -> Tuple[float, List[MemoryTextInstance]]:
    """Test the robustness of a machine learning model to different input types.

    Example:
        Test a pretrained black-box `model` for its robustness to 1000 random strings (length 0 to 500),
        containing whitespace characters, ASCII (upper, lower and numbers), emojis and Russian Cyrillic characters:

        >>> from text_sensitivity.data.random.string import RandomAscii, RandomCyrillic, RandomEmojis, RandomWhitespace
        >>> input_space_robustness(model, 
        >>>                        [RandomWhitespace(), RandomAscii(), RandomEmojis(base=True), RandomCyrillic('ru')],
        >>>                        n_samples=1000,
        >>>                        min_length=0,
        >>>                        max_length=500)

    Args:
        model (AbstractClassifier): Machine learning model to test.
        generators (List[RandomString]): Random character generators.
        n_samples (int, optional): Number of test samples. Defaults to 100.
        min_length (int, optional): Input minimum length. Defaults to 0.
        max_length (int, optional): Input maximum length. Defaults to 100.
        seed (Optional[int], optional): Seed for reproducibility purposes. Defaults to 0.

    Returns:
        Tuple[float, List[MemoryTextInstance]]: Percentage of success cases, list of failed instances
    """
    # Combine all generators into one
    generator = combine_generators(*generators, seed=seed)

    # Generate instances
    instances = generator.generate(n=n_samples, min_length=min_length, max_length=max_length)

    # Percentage success, instances that failed
    success: int = 0
    failures: List[List[str]] = []

    # Do not perform it batchwise but per instance, in order to return the error-throwing failures
    for i in instances:
        try:
            model.predict([instances[i]])
            success += 1
        except Exception as e:
            print(e)
            failures.append(instances[i])

    success = 1.0 if len(instances) == 0 else success / len(instances)

    return success, failures
