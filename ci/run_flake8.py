import subprocess

from ci.utils import collect_sources
import sys


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
