# with other dependency

try:
    import numpy
except ImportError as e:
    print("no numpy found")


def add(a, b):
    print("add, but in numpy")
    return numpy.add(a, b)
