from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.1"
ext_modules = [
    # pure c++ ext
    Pybind11Extension("python_example",
                      ["src/c_extension/main.cpp"],
                      # Example: passing in the version to the compiled code
                      define_macros=[('VERSION_INFO', __version__)],
                      ),
    # c++ and cgo ext
    Pybind11Extension("go_c_py_example",
                      [
                          "src/go_extension/main.cpp",
                      ],
                      # Example: passing in the version to the compiled code
                      define_macros=[('VERSION_INFO', __version__)],
                      ),
]

setup(
    name="python-pybind11-demo",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
