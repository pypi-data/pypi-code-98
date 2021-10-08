# Copyright 2019 The FastEstimator Authors. All Rights Reserved.
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
# ==============================================================================
from typing import Any, Dict, List, TypeVar

import tensorflow as tf
import torch

import fastestimator as fe
from fastestimator.backend.roll import roll
from fastestimator.op.tensorop.loss.loss import LossOp

Tensor = TypeVar('Tensor', tf.Tensor, torch.Tensor)


class MixLoss(LossOp):
    """Loss class to compute mix-up and cutmix losses.

    This class should be used in conjunction with MixUpBatch and CutMixBatch to perform mix-up training, which helps to
    reduce over-fitting, stabilize GAN training, and harden against adversarial attacks. See
    https://arxiv.org/abs/1710.09412 for details.

    Args:
        loss: A loss object which we use to calculate the underlying loss of MixLoss. This should be an object of type
            fe.op.tensorop.loss.loss.LossOp.
        lam: The key of the lambda value generated by MixUpBatch or CutMixBatch.
        average_loss: Whether the final loss should be averaged or not.

    Raises:
        ValueError: If the provided `loss` has multiple outputs.
    """
    def __init__(self, loss: LossOp, lam: str, average_loss: bool = True):
        self.loss = loss
        self.loss.average_loss = False
        if len(loss.outputs) != 1:
            raise ValueError("MixLoss only supports lossOps which have a single output.")
        super().__init__(inputs=[lam] + loss.inputs,
                         outputs=loss.outputs,
                         mode=loss.mode,
                         ds_id=loss.ds_id,
                         average_loss=average_loss)
        self.out_list = False

    @property
    def pred_key_idx(self) -> int:
        return self.loss.pred_key_idx + 1

    @property
    def true_key_idx(self) -> int:
        return self.loss.true_key_idx + 1

    def forward(self, data: List[Tensor], state: Dict[str, Any]) -> Tensor:
        lam, *args = data
        loss1 = self.loss.forward(args, state)

        args[self.loss.true_key_idx] = roll(args[self.loss.true_key_idx], shift=1, axis=0)
        loss2 = self.loss.forward(args, state)

        loss = lam * loss1 + (1.0 - lam) * loss2

        if self.average_loss:
            loss = fe.backend.reduce_mean(loss)

        return loss
