import timeit


cython_setup = """\
from yarl.quoting import _quote as quote
from yarl.quoting import _unquote as unquote
from yarl import URL
"""

python_setup = """\
from yarl.quoting import _py_quote as quote
from yarl.quoting import _py_unquote as unquote
from yarl import URL
"""


print("Cython quote: {:.3f} sec".format(
    timeit.timeit("quote(s)", cython_setup+"s='/path/to'")))


print("Python quote: {:.3f} sec".format(
    timeit.timeit("quote(s)", python_setup+"s='/path/to'")))


print("Cython unquote: {:.3f} sec".format(
    timeit.timeit("unquote(s)", cython_setup+"s='/path/to'")))


print("Python unquote: {:.3f} sec".format(
    timeit.timeit("unquote(s)", python_setup+"s='/path/to'")))


print("Cython URL with is_relative: {:.3f} sec".format(
    timeit.timeit("URL(s, is_relative=True)", cython_setup+"s='/path/to'")))


print("Cython URL without is_relative: {:.3f} sec".format(
    timeit.timeit("URL(s)", cython_setup+"s='/path/to'")))


print("Python URL with is_relative: {:.3f} sec".format(
    timeit.timeit("URL(s, is_relative=True)", python_setup+"s='/path/to'")))


print("Python URL without is_relative: {:.3f} sec".format(
    timeit.timeit("URL(s)", python_setup+"s='/path/to'")))
