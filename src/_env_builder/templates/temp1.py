def print_template():
    print("""
[tox]
envlist = py38,py39,py310

[testenv]
deps = pytest
commands = pytest
    """)