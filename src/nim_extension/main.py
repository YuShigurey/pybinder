import ctypes

lib = ctypes.cdll.LoadLibrary("./test/test.dll")

lib.Hellow()
