#!/venv/bin/python3
import platform as pf
import time
import subprocess as sp

sp.Popen("MakeJSON/cmake-build-debug/MakeJSON")

systemos = pf.system()
if (systemos == "Linux"):
    pipe_path = "/tmp/Leapcam"

if (systemos == "Windows"):
    pipe_path = "\\\\.\\pipe\\Leapcam"
    time.sleep(1)
    
with open(pipe_path, "r") as pipe:
   data = pipe.read()
   print("\n")
   print(data)

