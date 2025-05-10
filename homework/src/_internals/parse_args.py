import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder")
    parser.add_argument("output_folder")
    args = parser.parse_args()
    # input_folder = sys.argv[1]
    # output_folder = sys.argv[2]
    return args.input_folder, args.output_folder
