#!/venv/bin/python3
import platform
import subprocess as sp
import platform
import os
import time

#from cv2.datasets import none
#from mpmath.libmp import to_int
#from sympy import true
#from urllib3.http2.probe import acquire_and_get

if platform.system() == "Windows":
   pipe_path = "\\\\.\\pipe\\Leapcam"


if platform.system() == "Linux":
   pipe_path = "/tmp/Leapcam"



with open(pipe_path, "rb") as pipe:
   lijst =[]
   lijstout = None
   while lijstout != []:
      lijstout = []
      intdata = pipe.read(60)
      for byte in intdata:
         lijst.append(byte)
         if len(lijst) == 4:
            lijstout.append(int.from_bytes(lijst,byteorder ='little' , signed=True))
            lijst = []


      print(lijstout)
      intdata = None


