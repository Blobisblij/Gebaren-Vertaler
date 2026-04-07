#!/venv/bin/python3
import platform
import subprocess as sp
import platform
import os
import time

from cv2.datasets import none
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
   lijst =[]
   lijstout = [none]
   while lijstout != []:
      lijstout = []
      intdata = pipe.read(56)
      for byte in intdata:
         lijst.append(byte)
         if len(lijst) == 4:
            lijstout.append(int.from_bytes(lijst,byteorder ='little' , signed=True))
            lijst = []


      print(lijstout)
      intdata = none


