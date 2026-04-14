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
#
#
#
def writingToJson(list1, list2, list3, list4, list5):
    print(list1 + list2 + list3 + list4 + list5)
def main():

    Input = input("which sign is it")
    lijstout = []
    NGT_TRANSLATOR.Program_runnen(lijstout)
    List1 = [] * 5
    List2 = [] * 5
    List3 = [] * 5
    List4 = [] * 5
    List5 = [] * 5

    for tuple in lijstout:
        grouping(tuple[0], List1)
        grouping(tuple[1], List1)
        grouping(tuple[2], List1)
        grouping(tuple[3], List1)
        grouping(tuple[4], List1)
    writingToJson(List1, List2, List3, List4, List5)

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



def writingToJson(list1, list2, list3, list4, list5):
    print(list1 + list2 + list3 + list4 + list5)
main()