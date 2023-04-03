import numpy as np
import argparse
import os
import json


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
        
        if s == 'train':
            pass
        else:
            pass
        


    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    parser.add_argument('--rotation_error', type=float)
    parser.add_argument('--translation_error', type=float)

    args = parser.parse_args()

    apply_error(args)

    # python apply_error.py --path ./nerf/data/nerf_synthetic/lego