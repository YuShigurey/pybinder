cmake_minimum_required(VERSION 3.12)
project(NimEXT)

set(CMAKE_CXX_STANDARD 11)

include_directories("${PROJECT_SOURCE_DIR}/test")
add_subdirectory(Test)

add_executable(NimEXT main.cpp)
target_link_libraries(NimEXT Test)