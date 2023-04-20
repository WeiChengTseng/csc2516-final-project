import numpy as np
import argparse
import os
import json
import copy
import pdb
import math

from scipy.spatial.transform import Rotation as R


def read_json(path):
    with open(path, 'r') as fp:
        file_json = json.load(fp)
    return file_json


def write_json(file_json, path):
    json_object = json.dumps(file_json, indent=4)
    with open(path, "w") as outfile:
        outfile.write(json_object)
    return


def apply_error(args):

    splits = ['train', 'val', 'test']
    metas = {}
    for s in splits:
        with open(os.path.join(args.path, 'transforms_{}.json'.format(s)),
                  'r') as fp:
            metas[s] = json.load(fp)

    path_new = (args.path +
                f'_r_{args.rotation_error}_t_{args.translation_error}')
    os.makedirs(path_new, exist_ok=True)

    for s in splits:
        meta_new = copy.deepcopy(metas[s])

        for idx, f in enumerate(meta_new['frames']):
            if s == 'train':
                trans_mat = np.array(f['transform_matrix'])

                # apply translation error
                theta = np.random.uniform(0, 2 * math.pi)
                phi = np.random.uniform(-0.5 * math.pi, 0.5 * math.pi)
                translation_error = np.array([
                    np.cos(theta) * np.cos(theta),
                    np.sin(theta) * np.cos(theta),
                    np.sin(phi)
                ]) * args.translation_error

                # apply rotation error
                rot_x = np.random.uniform(-math.pi,
                                          math.pi) * args.rotation_error
                rot_y = np.random.uniform(-math.pi,
                                          math.pi) * args.rotation_error
                rot_z = np.random.uniform(-math.pi,
                                          math.pi) * args.rotation_error

                rot_mat = R.from_rotvec([rot_x, rot_y, rot_z]).as_matrix()

                trans_mat[:3, :3] = rot_mat @ trans_mat[:3, :3]
                trans_mat[:3, 3] += np.array(translation_error)

                meta_new['frames'][idx]['transform_matrix'] = trans_mat.tolist(
                )

            # modify the path in original json file
            f['file_path'] = f['file_path'].replace(
                '.', f'../{os.path.basename(args.path)}')

        write_json(meta_new, os.path.join(path_new, f'transforms_{s}.json'))

    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    parser.add_argument('--rotation_error', type=float, default=0)
    parser.add_argument('--translation_error', type=float, default=0)

    args = parser.parse_args()

    apply_error(args)

    # python apply_error.py --path ./nerf/data/nerf_synthetic/lego
    # python apply_error.py --path ./nerf/data/nerf_synthetic/lego --rotation_error 0.01
    # python apply_error.py --path ./nerf/data/nerf_synthetic/lego --rotation_error 0.05
    # python apply_error.py --path ./nerf/data/nerf_synthetic/lego --rotation_error 0.05
    # python apply_error.py --path ./nerf/data/nerf_synthetic/lego --rotation_error 0.1

    # python apply_error.py --path ./nerf/data/nerf_synthetic/lego --translation_error 0.01
    # python apply_error.py --path ./nerf/data/nerf_synthetic/lego --translation_error 0.05
    # python apply_error.py --path ./nerf/data/nerf_synthetic/lego --translation_error 0.1