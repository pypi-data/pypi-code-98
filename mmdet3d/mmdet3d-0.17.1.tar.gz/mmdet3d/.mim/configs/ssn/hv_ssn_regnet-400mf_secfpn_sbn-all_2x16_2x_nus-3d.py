_base_ = './hv_ssn_secfpn_sbn-all_2x16_2x_nus-3d.py'
# model settings
model = dict(
    type='MVXFasterRCNN',
    pts_backbone=dict(
        _delete_=True,
        type='NoStemRegNet',
        arch=dict(w0=24, wa=24.48, wm=2.54, group_w=16, depth=22, bot_mul=1.0),
        init_cfg=dict(
            type='Pretrained', checkpoint='open-mmlab://regnetx_400mf'),
        out_indices=(1, 2, 3),
        frozen_stages=-1,
        strides=(1, 2, 2, 2),
        base_channels=64,
        stem_channels=64,
        norm_cfg=dict(type='naiveSyncBN2d', eps=1e-3, momentum=0.01),
        norm_eval=False,
        style='pytorch'),
    pts_neck=dict(in_channels=[64, 160, 384]))
