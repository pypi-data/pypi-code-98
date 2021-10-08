# Copyright 2018 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""TensorFlow Probability Optimizer python package."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_probability.python.internal import all_util
# from tensorflow_probability.substrates.numpy.optimizer import convergence_criteria
from tensorflow_probability.substrates.numpy.optimizer import linesearch
from tensorflow_probability.substrates.numpy.optimizer.bfgs import minimize as bfgs_minimize
from tensorflow_probability.substrates.numpy.optimizer.bfgs_utils import converged_all
from tensorflow_probability.substrates.numpy.optimizer.bfgs_utils import converged_any
# from tensorflow_probability.substrates.numpy.optimizer.differential_evolution import minimize as differential_evolution_minimize
# from tensorflow_probability.substrates.numpy.optimizer.differential_evolution import one_step as differential_evolution_one_step
from tensorflow_probability.substrates.numpy.optimizer.lbfgs import minimize as lbfgs_minimize
from tensorflow_probability.substrates.numpy.optimizer.nelder_mead import minimize as nelder_mead_minimize
from tensorflow_probability.substrates.numpy.optimizer.nelder_mead import nelder_mead_one_step
# from tensorflow_probability.substrates.numpy.optimizer.proximal_hessian_sparse import minimize as proximal_hessian_sparse_minimize
# from tensorflow_probability.substrates.numpy.optimizer.proximal_hessian_sparse import minimize_one_step as proximal_hessian_sparse_one_step
# from tensorflow_probability.substrates.numpy.optimizer.sgld import StochasticGradientLangevinDynamics
# from tensorflow_probability.substrates.numpy.optimizer.variational_sgd import VariationalSGD


_allowed_symbols = [
    'converged_all',
    'converged_any',
    'bfgs_minimize',
    'differential_evolution_minimize',
    'differential_evolution_one_step',
    'lbfgs_minimize',
    'nelder_mead_minimize',
    'nelder_mead_one_step',
    'proximal_hessian_sparse_minimize',
    'proximal_hessian_sparse_one_step',
    'linesearch',
    # 'StochasticGradientLangevinDynamics',
    # 'convergence_criteria',
    # 'VariationalSGD',
]

all_util.remove_undocumented(__name__, _allowed_symbols)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# This file is auto-generated by substrates/meta/rewrite.py
# It will be surfaced by the build system as a symlink at:
#   `tensorflow_probability/substrates/numpy/optimizer/__init__.py`
# For more info, see substrate_runfiles_symlinks in build_defs.bzl
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
