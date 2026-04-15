#!/venv/bin/python3
import platform
import subprocess as sp
import platform
import sys
import os
import time
import torch

if platform.system() == "Windows":
    pipe_path = "\\\\.\\pipe\\Leapcam"

if platform.system() == "Linux":
    pipe_path = "/tmp/Leapcam"
#collects data to train the moddel with
if (sys.argv[0] == "train"):
    if (sys.argv[1] != None):
        WordOrLetterToTrain = sys.argv[1]

        with open(pipe_path, "rb") as pipe:
            lijst =[]
            lijstout = None
            totalinputdata = 0
            maxinputdata = 10000000

            while lijstout != []:
              lijstout = []
              intdata = pipe.read(60)
              for byte in intdata:
                 lijst.append(byte)
                 if len(lijst) == 4:
                    lijstout.append(int.from_bytes(lijst,byteorder ='little' , signed=True))
                    lijst = []
                    print(lijstout)
                    ListGoingOut = tuple(lijstout)
                    totalinputdata = totalinputdata + 1

#starts the datastream from the leap cam and sends the input to the moddel
if (sys.argv[0] == "run"):
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



