cmake_minimum_required(VERSION 4.1)
project(MakeJSON C)

set(CMAKE_C_STANDARD 11)

add_executable(MakeJSON main.c cJSON.c)
