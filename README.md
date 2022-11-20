# build python pacakge

poetry build

# build c extension

python setup.py bdist_wheel

or 

mkdir build
cd build
cmake ..
cmake --build . --config Release --target check