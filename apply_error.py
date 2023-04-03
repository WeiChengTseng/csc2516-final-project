import numpy as np
import argparse
import os
import json
import copy
import pdb

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
        if s == 'train':
            for f in meta_new['frames']:
                trans_mat = np.array(f['transform_matrix'])
                pdb.set_trace()
                translation_error = 0
                trans_mat[:3, 3] += 0
        else:
            pass
        


    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    parser.add_argument('--rotation_error', type=float, default=0)
    parser.add_argument('--translation_error', type=float, default=0)

    args = parser.parse_args()

    apply_error(args)

    # python apply_error.py --path ./nerf/data/nerf_synthetic/lego