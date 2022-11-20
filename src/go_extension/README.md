# Shared library
go build -buildmode=c-shared -o number.dll
go build -buildmode=c-shared -o number.so

# Archive
go build -buildmode=c-archive -o number.a
gcc -o a.out _test.main.c number.a

# manually
python -m pybind11 --includes
g++ -O3 -Wall -shared -std=c++11 -fPIC -IC:\ProgramData\Anaconda3\envs\learn-tox\Include -IC:\ProgramData\Anaconda3\envs\learn-tox\lib\site-packages\pybind11\include main.cpp number.dll -o example.pyd