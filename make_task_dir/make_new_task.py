import argparse
import os
import pathlib
import sys


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root_path",
        type=str,
        default=""
    )
    parser.add_argument(
        "--task_name",
        type=str,
        default=""
    )
    args = parser.parse_args()

    dir_path = os.path.join(args.root_path, args.task_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_path = os.path.join(args.root_path, args.task_name, args.task_name + '.md')
    if not os.path.exists(file_path):
        pathlib.Path(file_path).touch()


if __name__ == "__main__":
    main(sys.argv)
