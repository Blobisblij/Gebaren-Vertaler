#!/venv/bin/python3
import os
import sys
import subprocess as sp

print("hoi")
sp.Popen("MakeJSON/cmake-build-debug/MakeJSON")
pipe_path = "/tmp/Leapcam"
with open(pipe_path, "r") as pipe:
   data = pipe.read()
   print(data)

