#!/venv/bin/python3
import os


exec(open("./MakeJSON/cmake-build-debug/MakeJSON"))
pipe_path = "/tmp/Leapcam"
with open(pipe_path, "r") as pipe:
   data = pipe.read()
   print(data)

