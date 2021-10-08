# Copyright (c) OpenMMLab. All rights reserved.
import torch
from torch import nn as nn

from mmdet3d.ops import PAConv, PAConvCUDA
from .builder import SA_MODULES
from .point_sa_module import BasePointSAModule


@SA_MODULES.register_module()
class PAConvSAModuleMSG(BasePointSAModule):
    r"""Point set abstraction module with multi-scale grouping (MSG) used in
    PAConv networks.

    Replace the MLPs in `PointSAModuleMSG` with PAConv layers.
    See the `paper <https://arxiv.org/abs/2103.14635>`_ for more details.

    Args:
        paconv_num_kernels (list[list[int]]): Number of kernel weights in the
            weight banks of each layer's PAConv.
        paconv_kernel_input (str, optional): Input features to be multiplied
            with kernel weights. Can be 'identity' or 'w_neighbor'.
            Defaults to 'w_neighbor'.
        scorenet_input (str, optional): Type of the input to ScoreNet.
            Defaults to 'w_neighbor_dist'. Can be the following values:

            - 'identity': Use xyz coordinates as input.
            - 'w_neighbor': Use xyz coordinates and the difference with center
                points as input.
            - 'w_neighbor_dist': Use xyz coordinates, the difference with
                center points and the Euclidian distance as input.

        scorenet_cfg (dict, optional): Config of the ScoreNet module, which
            may contain the following keys and values:

            - mlp_channels (List[int]): Hidden units of MLPs.
            - score_norm (str): Normalization function of output scores.
                Can be 'softmax', 'sigmoid' or 'identity'.
            - temp_factor (float): Temperature factor to scale the output
                scores before softmax.
            - last_bn (bool): Whether to use BN on the last output of mlps.
    """

    def __init__(self,
                 num_point,
                 radii,
                 sample_nums,
                 mlp_channels,
                 paconv_num_kernels,
                 fps_mod=['D-FPS'],
                 fps_sample_range_list=[-1],
                 dilated_group=False,
                 norm_cfg=dict(type='BN2d', momentum=0.1),
                 use_xyz=True,
                 pool_mod='max',
                 normalize_xyz=False,
                 bias='auto',
                 paconv_kernel_input='w_neighbor',
                 scorenet_input='w_neighbor_dist',
                 scorenet_cfg=dict(
                     mlp_channels=[16, 16, 16],
                     score_norm='softmax',
                     temp_factor=1.0,
                     last_bn=False)):
        super(PAConvSAModuleMSG, self).__init__(
            num_point=num_point,
            radii=radii,
            sample_nums=sample_nums,
            mlp_channels=mlp_channels,
            fps_mod=fps_mod,
            fps_sample_range_list=fps_sample_range_list,
            dilated_group=dilated_group,
            use_xyz=use_xyz,
            pool_mod=pool_mod,
            normalize_xyz=normalize_xyz,
            grouper_return_grouped_xyz=True)

        assert len(paconv_num_kernels) == len(mlp_channels)
        for i in range(len(mlp_channels)):
            assert len(paconv_num_kernels[i]) == len(mlp_channels[i]) - 1, \
                'PAConv number of kernel weights wrong'

        # in PAConv, bias only exists in ScoreNet
        scorenet_cfg['bias'] = bias

        for i in range(len(self.mlp_channels)):
            mlp_channel = self.mlp_channels[i]
            if use_xyz:
                mlp_channel[0] += 3

            num_kernels = paconv_num_kernels[i]

            mlp = nn.Sequential()
            for i in range(len(mlp_channel) - 1):
                mlp.add_module(
                    f'layer{i}',
                    PAConv(
                        mlp_channel[i],
                        mlp_channel[i + 1],
                        num_kernels[i],
                        norm_cfg=norm_cfg,
                        kernel_input=paconv_kernel_input,
                        scorenet_input=scorenet_input,
                        scorenet_cfg=scorenet_cfg))
            self.mlps.append(mlp)


@SA_MODULES.register_module()
class PAConvSAModule(PAConvSAModuleMSG):
    r"""Point set abstraction module with single-scale grouping (SSG) used in
    PAConv networks.

    Replace the MLPs in `PointSAModule` with PAConv layers. See the `paper
    <https://arxiv.org/abs/2103.14635>`_ for more details.
    """

    def __init__(self,
                 mlp_channels,
                 paconv_num_kernels,
                 num_point=None,
                 radius=None,
                 num_sample=None,
                 norm_cfg=dict(type='BN2d', momentum=0.1),
                 use_xyz=True,
                 pool_mod='max',
                 fps_mod=['D-FPS'],
                 fps_sample_range_list=[-1],
                 normalize_xyz=False,
                 paconv_kernel_input='w_neighbor',
                 scorenet_input='w_neighbor_dist',
                 scorenet_cfg=dict(
                     mlp_channels=[16, 16, 16],
                     score_norm='softmax',
                     temp_factor=1.0,
                     last_bn=False)):
        super(PAConvSAModule, self).__init__(
            mlp_channels=[mlp_channels],
            paconv_num_kernels=[paconv_num_kernels],
            num_point=num_point,
            radii=[radius],
            sample_nums=[num_sample],
            norm_cfg=norm_cfg,
            use_xyz=use_xyz,
            pool_mod=pool_mod,
            fps_mod=fps_mod,
            fps_sample_range_list=fps_sample_range_list,
            normalize_xyz=normalize_xyz,
            paconv_kernel_input=paconv_kernel_input,
            scorenet_input=scorenet_input,
            scorenet_cfg=scorenet_cfg)


@SA_MODULES.register_module()
class PAConvCUDASAModuleMSG(BasePointSAModule):
    r"""Point set abstraction module with multi-scale grouping (MSG) used in
    PAConv networks.

    Replace the non CUDA version PAConv with CUDA implemented PAConv for
    efficient computation. See the `paper <https://arxiv.org/abs/2103.14635>`_
    for more details.
    """

    def __init__(self,
                 num_point,
                 radii,
                 sample_nums,
                 mlp_channels,
                 paconv_num_kernels,
                 fps_mod=['D-FPS'],
                 fps_sample_range_list=[-1],
                 dilated_group=False,
                 norm_cfg=dict(type='BN2d', momentum=0.1),
                 use_xyz=True,
                 pool_mod='max',
                 normalize_xyz=False,
                 bias='auto',
                 paconv_kernel_input='w_neighbor',
                 scorenet_input='w_neighbor_dist',
                 scorenet_cfg=dict(
                     mlp_channels=[8, 16, 16],
                     score_norm='softmax',
                     temp_factor=1.0,
                     last_bn=False)):
        super(PAConvCUDASAModuleMSG, self).__init__(
            num_point=num_point,
            radii=radii,
            sample_nums=sample_nums,
            mlp_channels=mlp_channels,
            fps_mod=fps_mod,
            fps_sample_range_list=fps_sample_range_list,
            dilated_group=dilated_group,
            use_xyz=use_xyz,
            pool_mod=pool_mod,
            normalize_xyz=normalize_xyz,
            grouper_return_grouped_xyz=True,
            grouper_return_grouped_idx=True)

        assert len(paconv_num_kernels) == len(mlp_channels)
        for i in range(len(mlp_channels)):
            assert len(paconv_num_kernels[i]) == len(mlp_channels[i]) - 1, \
                'PAConv number of kernel weights wrong'

        # in PAConv, bias only exists in ScoreNet
        scorenet_cfg['bias'] = bias

        # we need to manually concat xyz for CUDA implemented PAConv
        self.use_xyz = use_xyz

        for i in range(len(self.mlp_channels)):
            mlp_channel = self.mlp_channels[i]
            if use_xyz:
                mlp_channel[0] += 3

            num_kernels = paconv_num_kernels[i]

            # can't use `nn.Sequential` for PAConvCUDA because its input and
            # output have different shapes
            mlp = nn.ModuleList()
            for i in range(len(mlp_channel) - 1):
                mlp.append(
                    PAConvCUDA(
                        mlp_channel[i],
                        mlp_channel[i + 1],
                        num_kernels[i],
                        norm_cfg=norm_cfg,
                        kernel_input=paconv_kernel_input,
                        scorenet_input=scorenet_input,
                        scorenet_cfg=scorenet_cfg))
            self.mlps.append(mlp)

    def forward(
        self,
        points_xyz,
        features=None,
        indices=None,
        target_xyz=None,
    ):
        """forward.

        Args:
            points_xyz (Tensor): (B, N, 3) xyz coordinates of the features.
            features (Tensor): (B, C, N) features of each point.
                Default: None.
            indices (Tensor): (B, num_point) Index of the features.
                Default: None.
            target_xyz (Tensor): (B, M, 3) new_xyz coordinates of the outputs.

        Returns:
            Tensor: (B, M, 3) where M is the number of points.
                New features xyz.
            Tensor: (B, M, sum_k(mlps[k][-1])) where M is the number
                of points. New feature descriptors.
            Tensor: (B, M) where M is the number of points.
                Index of the features.
        """
        new_features_list = []

        # sample points, (B, num_point, 3), (B, num_point)
        new_xyz, indices = self._sample_points(points_xyz, features, indices,
                                               target_xyz)

        for i in range(len(self.groupers)):
            xyz = points_xyz
            new_features = features
            for j in range(len(self.mlps[i])):
                # we don't use grouped_features here to avoid large GPU memory
                # _, (B, 3, num_point, nsample), (B, num_point, nsample)
                _, grouped_xyz, grouped_idx = self.groupers[i](xyz, new_xyz,
                                                               new_features)

                # concat xyz as additional features
                if self.use_xyz and j == 0:
                    # (B, C+3, N)
                    new_features = torch.cat(
                        (points_xyz.permute(0, 2, 1), new_features), dim=1)

                # (B, out_c, num_point, nsample)
                grouped_new_features = self.mlps[i][j](
                    (new_features, grouped_xyz, grouped_idx.long()))[0]

                # different from PointNet++ and non CUDA version of PAConv
                # CUDA version of PAConv needs to aggregate local features
                # every time after it passes through a Conv layer
                # in order to transform to valid input shape
                # (B, out_c, num_point)
                new_features = self._pool_features(grouped_new_features)

                # constrain the points to be grouped for next PAConv layer
                # because new_features only contains sampled centers now
                # (B, num_point, 3)
                xyz = new_xyz

            new_features_list.append(new_features)

        return new_xyz, torch.cat(new_features_list, dim=1), indices


@SA_MODULES.register_module()
class PAConvCUDASAModule(PAConvCUDASAModuleMSG):
    r"""Point set abstraction module with single-scale grouping (SSG) used in
    PAConv networks.

    Replace the non CUDA version PAConv with CUDA implemented PAConv for
    efficient computation. See the `paper <https://arxiv.org/abs/2103.14635>`_
    for more details.
    """

    def __init__(self,
                 mlp_channels,
                 paconv_num_kernels,
                 num_point=None,
                 radius=None,
                 num_sample=None,
                 norm_cfg=dict(type='BN2d', momentum=0.1),
                 use_xyz=True,
                 pool_mod='max',
                 fps_mod=['D-FPS'],
                 fps_sample_range_list=[-1],
                 normalize_xyz=False,
                 paconv_kernel_input='w_neighbor',
                 scorenet_input='w_neighbor_dist',
                 scorenet_cfg=dict(
                     mlp_channels=[8, 16, 16],
                     score_norm='softmax',
                     temp_factor=1.0,
                     last_bn=False)):
        super(PAConvCUDASAModule, self).__init__(
            mlp_channels=[mlp_channels],
            paconv_num_kernels=[paconv_num_kernels],
            num_point=num_point,
            radii=[radius],
            sample_nums=[num_sample],
            norm_cfg=norm_cfg,
            use_xyz=use_xyz,
            pool_mod=pool_mod,
            fps_mod=fps_mod,
            fps_sample_range_list=fps_sample_range_list,
            normalize_xyz=normalize_xyz,
            paconv_kernel_input=paconv_kernel_input,
            scorenet_input=scorenet_input,
            scorenet_cfg=scorenet_cfg)
