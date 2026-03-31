#!/venv/bin/python3
import LoadData
import os
import numpy as np
import torch
import torchvision


exec(open("./MakeJSON/cmake-build-debug/MakeJSON"))
pipe_path = "/tmp/Leapcam"
moddelPath = "/moddeldata"
moddelData = LoadData(moddelPath)
with open(pipe_path, "r") as pipe:
   data = pipe.read()


