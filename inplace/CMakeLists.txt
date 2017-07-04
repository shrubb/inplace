project(inplace)
cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/lib")

find_package(OpenMP)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")

set(CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 11)

if (CMAKE_VERSION VERSION_LESS 3.1)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
endif()

find_package(CUDA REQUIRED)

set(CUDA_NVCC_FLAGS "${CUDA_NVCC_FLAGS} -std=c++11")
set(SOURCES gcd.cpp openmp.cpp reduced_math.cpp enact.cu introspect.cu save_array.cu permute.cu rotate.cu smem_shuffle.cu memory_shuffle.cu skinny.cu timer.cu)
cuda_add_library(inplace SHARED ${SOURCES})
#cuda_add_cublas_to_target(integral-cuda)
