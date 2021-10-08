from dataclasses import dataclass
from typing import (
    Callable,
    Optional,
)

from fedot.core.composer.composer import ComposerRequirements
from fedot.core.composer.gp_composer.gp_composer import GPComposer, GPComposerBuilder
from fedot.core.data.data import InputData
from fedot.core.optimisers.gp_comp.gp_optimiser import GPGraphOptimiserParameters
from fedot.core.optimisers.gp_comp.operators.mutation import MutationTypesEnum
from fedot.core.pipelines.pipeline import Pipeline
from fedot.core.repository.tasks import Task


@dataclass
class GPComposerRequirements(ComposerRequirements):
    pop_size: Optional[int] = 50
    num_of_generations: Optional[int] = 50
    crossover_prob: Optional[float] = None
    mutation_prob: Optional[float] = None


class FixedStructureComposer(GPComposer):
    def __init__(self, optimiser=None, metrics: Optional[Callable] = None,
                 composer_requirements: GPComposerRequirements = None,
                 initial_pipeline: Optional[Pipeline] = None):
        super().__init__(optimiser=optimiser, metrics=metrics, composer_requirements=composer_requirements,
                         initial_pipeline=initial_pipeline)

    def compose_pipeline(self, data: InputData, is_visualise: bool = False,
                         is_tune: bool = False, on_next_iteration_callback: Optional[Callable] = None) -> Pipeline:
        return super().compose_pipeline(data, is_visualise, is_tune, on_next_iteration_callback)


class FixedStructureComposerBuilder(GPComposerBuilder):
    def __init__(self, task: Task):
        super().__init__(task=task)
        self._composer = FixedStructureComposer()
        fixed_structure_optimiser_parameters = GPGraphOptimiserParameters(mutation_types=[MutationTypesEnum.simple])
        self.optimiser_parameters = fixed_structure_optimiser_parameters

    def set_default_composer_params(self):
        super().set_default_composer_params()
        self._composer.composer_requirements.crossover_prob = 0.0
