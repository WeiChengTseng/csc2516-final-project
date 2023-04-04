_base_ = '../default.py'

expname = 'lego_r_0.01_t_0'
basedir = './logs/nerf_synthetic'

data = dict(
    # datadir='./data/nerf_synthetic/lego',
    datadir='../nerf/data/nerf_synthetic/lego_r_0.01_t_0',
    dataset_type='blender',
    white_bkgd=True,
)

