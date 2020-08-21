""" Tiny wrapper for mccabe module.
Iterate over all the python sources, and print results in
an easily parseable format
If you are already using pyflakes or prospector, you won't need this :)
Dependencies: mmcabe, path.py
"""

import ast
import textwrap

import mccabe
import path


def ignore(py_source):
    parts = py_source.splitall()
    # Ignore 'hidden' files
    if any(x.startswith(".") for x in parts):
        return True
    return False


def yield_sources():
    top = path.Path(".")
    for py_source in top.walkfiles("*.py"):
        py_source = py_source.relpath(top)
        if not ignore(py_source):
            yield py_source


def process(py_source, max_complexity):
    code = py_source.text()
    tree = compile(code, py_source, "exec", ast.PyCF_ONLY_AST)
    visitor = mccabe.PathGraphingAstVisitor()
    visitor.preorder(tree, visitor)
    for graph in visitor.graphs.values():
        if graph.complexity() > max_complexity:
            text = textwrap.dedent("""\
            {}:{}:{} {} {}""")
            text = text.format(py_source, graph.lineno, graph.column,
                               graph.entity, graph.complexity())
            print(text)


def main():
    max_complexity = int(5)
    print("Looking for code with complexity above", max_complexity)
    for py_source in yield_sources():
        process(py_source, max_complexity)


if __name__ == "__main__":
    main()
