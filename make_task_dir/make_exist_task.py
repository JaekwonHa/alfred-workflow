import os
import shutil
import sys
import argparse


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root_path",
        type=str,
        default=""
    )
    args = parser.parse_args()

    file_list = os.listdir(args.root_path)

    for file in file_list:
        path = os.path.join(args.root_path, file)
        if os.path.isfile(path):
            if file.endswith(".md"):
                dir_path = path.replace('.md', '')
                print(f"make: {dir_path}")
                # print(f"move: {path}. {os.path.join(dir_path, file)}")
                os.makedirs(dir_path)
                shutil.move(path, os.path.join(dir_path, file))


if __name__ == "__main__":
    main(sys.argv)
