#!/venv/bin/python3
import platform
import subprocess as sp
import platform
import os
import time

from mpmath.libmp import to_int
from sympy import true
from urllib3.http2.probe import acquire_and_get

if platform.system() == "Windows":
   pipe_path = "\\\\.\\pipe\\Leapcam"


if platform.system() == "Linux":
   pipe_path = "/tmp/Leapcam"

if platform.system() == "Windows":
   sp.Popen("./MakeJSON/cmake-build-debug/MakeJson.exe")

#if platform.system() == "Linux":
#   sp.Popen("MakeJSON/cmake-build-debug/MakeJSON")

with open(pipe_path, "rb") as pipe:
   while true:
      intdata = pipe.read(60)
      print(intdata)

