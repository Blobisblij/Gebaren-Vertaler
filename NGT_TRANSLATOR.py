#!/venv/bin/python3
import platform

import platform
import os
import time

if platform.system() == "Windows":
   pipe_path = "\\\\.\\pipe\\Leapcam"
   time.sleep(2)

if platform.system() == "Linux":
   pipe_path = "/tmp/Leapcam"

if platform.system() == "Windows":
   os.popen("MakeJSON/cmake-build-debug/MakeJson.exe")

if platform.system() == "Linux":
   os.popen("MakeJSON/cmake-build-debug/MakeJSON")

with open(pipe_path, "r") as pipe:
   data = pipe.read()

