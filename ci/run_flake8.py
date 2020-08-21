import subprocess

import pathlib as path
import os.path
import sys


def collect_sources(ignore_func):
    top_path = path.Path().absolute().parent
    for root, dirname, filenames in os.walk(top_path):
        for file in filenames:
            if os.path.splitext(file)[1] == ".py":
                file_path = os.path.join(root, file)
                if not ignore_func(file_path):
                    yield file_path


def ignore(p):
    """ Ignore hidden and test files """
    if p.startswith("."):
        return True
    if 'test' in p:
        return True
    return False


def run_pyflakes():
    cmd = ["flake8"]
    cmd.extend(collect_sources(ignore_func=ignore))

    return subprocess.call(cmd)


if __name__ == "__main__":
    rc = run_pyflakes()
    sys.exit(rc)
