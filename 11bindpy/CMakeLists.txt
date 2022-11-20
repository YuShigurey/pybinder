cmake_minimum_required(VERSION 3.4)
project(example)

add_subdirectory(pybind11)
add_executable(example src/main.cpp)

target_link_libraries(example PRIVATE pybind11::embed)

