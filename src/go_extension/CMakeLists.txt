cmake_minimum_required(VERSION 3.12)
project(GoEXT)

set(CMAKE_CXX_STANDARD 11)

include_directories("${PROJECT_SOURCE_DIR}/test")
add_subdirectory(Test)
#add_subdirectory(extern/pybind11)
add_executable(GoEXT main.cpp)
target_link_libraries(GoEXT number)


