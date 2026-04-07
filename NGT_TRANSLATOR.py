#!/venv/bin/python3
import sys
import os
import time

if os.name == "Windows":
   pipe_path = "\\\\.\\pipe\\Leapcam"
   time.sleep(2)

if os.name == "Linux":
   pipe_path = "/tmp/Leapcam"

if os.name == "Windows":
   os.popen("cmake-build-debug/MakeJson.exe")

if os.name == "Linux":
   os.popen("cmake-build-debug/MakeJson")

with open(pipe_path, "r") as pipe:
   data = pipe.read()

