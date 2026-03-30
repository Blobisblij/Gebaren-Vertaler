cmake_minimum_required(VERSION 4.1)
project(MakeJSON C)

set(CMAKE_C_STANDARD 11)

set(LEAP_SDK_ROOT "C:/Program Files/Ultraleap/LeapSDK")

include_directories("${LEAP_SDK_ROOT}/include")
link_directories("${LEAP_SDK_ROOT}/lib/x64")

add_executable(MakeJSON main.c
        memoryalocation.c
        memoryalocation.h
        NamedPipes.c
        NamedPipes.h)

target_link_libraries(MakeJSON PRIVATE LeapC)
