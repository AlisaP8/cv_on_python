import os


def print_directory_contents(path):
    for path_dir in os.listdir(path):
        print(path_dir)
        x = os.path.join(path, path_dir)
        if os.path.isdir(x):
            print_directory_contents(x)
