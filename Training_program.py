#!/venv/bin/python3
import platform
import subprocess as sp
import platform
import os
import time

import NGT_TRANSLATOR
# in de lijsten
# plek 0 is laagste
# plek 1 is hoogste
#plek 3 is gemiddelde
#plek vier is de hoeveelheid getallen in het huidige gemiddelde
#plek 5 is het totaal
if platform.system() == "Windows":
    pipe_path = "\\\\.\\pipe\\Leapcam"

if platform.system() == "Linux":
    pipe_path = "/tmp/Leapcam"
#
#
def loopen():
    with open(pipe_path, "rb") as pipe:
        lijst = []
        lijstout = None
        while lijstout != []:
            lijstout = []
            intdata = pipe.read(60)
            for byte in intdata:
                lijst.append(byte)
                if len(lijst) == 4:
                    lijstout.append(int.from_bytes(lijst, byteorder='little', signed=True))
            lijst = []
            main(lijstout)
        intdata = None
def main(Hoofdlijst):

    List1A = [] * 5
    List1B = [] * 5
    List1C = [] * 5
    List2A = [] * 5
    List2B = [] * 5
    List2C = [] * 5
    List3A = [] * 5
    List3B = [] * 5
    List3C = [] * 5
    List4A = [] * 5
    List4B = [] * 5
    List4C = [] * 5
    List5A = [] * 5
    List5B = [] * 5
    List5C = [] * 5

    for tuple in Hoofdlijst:
        grouping(tuple[0], List1A)
        grouping(tuple[1], List1B)
        grouping(tuple[2], List1C)
        grouping(tuple[3], List2A)
        grouping(tuple[4], List2B)
        grouping(tuple[5], List2C)
        grouping(tuple[6], List3A)
        grouping(tuple[7], List3B)
        grouping(tuple[8], List3C)
        grouping(tuple[9], List4A)
        grouping(tuple[10], List4B)
        grouping(tuple[11], List4C)
        grouping(tuple[12], List5A)
        grouping(tuple[13], List5B)
        grouping(tuple[14], List5C)


def grouping (input, list):
    if list == None:
        krijgHoogste(input,None)
        KrijgLaagste(input, None)
        krijgGemiddelde(input, None)
    else:
        krijgHoogste(input,list)
        KrijgLaagste(input, list)
        krijgGemiddelde(input, list)


def krijgGemiddelde(input, list):
    if list[3] == None:
        list[3] = input
        list[4] = 1
        list[5] = input
    else:
        list[4] = list[4] +1
        list[5] = list[5] + input
        list[3] = (list[5] / list[4])

def KrijgLaagste(input, list):
    if list[1] == None:
        list[1] = input
    else:
        if input < list[1]:
            list[1] = input

def krijgHoogste(input, list):
    if list[2] == None:
        list[2] = input
    else:
        if input > list[2]:
            list[2] = input

loopen()