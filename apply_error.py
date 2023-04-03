import numpy as np
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    parser.add_argument('--rotation_error', type=float)
    parser.add_argument('--translation_error', type=float)