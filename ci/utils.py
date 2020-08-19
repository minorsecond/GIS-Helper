import pathlib as path
import os.path


def collect_sources(ignore_func):
    top_path = path.Path().absolute().parent
    for root, dirname, filenames in os.walk(top_path):
        for file in filenames:
            if os.path.splitext(file)[1] == ".py":
                file_path = os.path.join(root, file)
                if not ignore_func(file_path):
                    yield file_path
