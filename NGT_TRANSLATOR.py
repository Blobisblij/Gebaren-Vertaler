#!/venv/bin/python3
import platform
import csv, os
import sys
import torch
import pandas as pd
from torch import nn
from torchvision.transforms import ToTensor
from handmodel import HandNN, train, test
from DatasetMaker import GestureDataset ,save_sample
from torch.utils.data import DataLoader, random_split
from DatasetMaker import Dataset

import win32file
#setting os spesific var's
if platform.system() == "Windows":
    #pipe_path = "\\\\.\\pipe\\Leapcam"
    pipe_path = r"\\.\pipe\Leapcam"

if platform.system() == "Linux":
    pipe_path = "/tmp/Leapcam"

#load model
device = "cpu"
loss_fn = nn.CrossEntropyLoss()


#collects data to train the model with
if sys.argv[1] == "collect":
    if sys.argv[2] != None:
        WordOrLetterToTrain = sys.argv[2]

        # open pipe the windows way
        pipe = win32file.CreateFile(
            pipe_path,
            win32file.GENERIC_READ,
            0, None,
            win32file.OPEN_EXISTING,
            0, None
        )

        lijst = []
        totalinputdata = 0
        maxinputdata = 500

        while totalinputdata < maxinputdata:
            lijstout = []
            hr, intdata = win32file.ReadFile(pipe, 60)  # read 60 bytes
            for byte in intdata:
                lijst.append(byte)
                if len(lijst) == 4:
                    lijstout.append(int.from_bytes(lijst, byteorder='little', signed=True))
                    lijst = []
            if len(lijstout) == 15:
                print(lijstout)
                save_sample(lijstout, WordOrLetterToTrain)
                totalinputdata += 1

        win32file.CloseHandle(pipe)  # close after all samples collect
        print(F"Collected {totalinputdata} samples for  {WordOrLetterToTrain}")
if sys.argv[1] == "train":
        dataset = GestureDataset("gesture_dataset.csv")
        num_gestures = len(dataset.label_map)
        # laad het model met correcte params
        model = HandNN(num_gestures).to(device)
        optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

        train_size = int(len(dataset) * 0.8)
        test_size = len(dataset) - train_size
        train_dataset, test_dataset = random_split(dataset, [train_size, test_size])


        train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
        test_loader = DataLoader(test_dataset, batch_size=32, shuffle=True)


        epochs = 15
        for epoch in range(epochs):
            train(train_loader,model,loss_fn,optimizer)
            test(test_loader,model,loss_fn)

        torch.save(model.state_dict(), 'handmodel.pth')

        # else:
        #     epochs = 15
        #     for epoch in range(epochs):
        #         train(train_loader,model,loss_fn,optimizer)
        #         test(test_loader,model,loss_fn)
        #         torch.save(model, 'handmodel.pth')




#starts the datastream from the leap cam and sends the input to the moddel
if (sys.argv[1] == "run"):
    dataset = GestureDataset("gesture_dataset.csv")
    num_gestures = len(dataset.label_map)
    model = HandNN(num_gestures).to(device)
    model.load_state_dict(torch.load('handmodel.pth'))
    model.eval()
    index_to_label = {i: name for name, i in dataset.label_map.items()}
    lastprediction = 0

    # open pipe the windows way
    pipe = win32file.CreateFile(
        pipe_path,
        win32file.GENERIC_READ,
        0, None,
        win32file.OPEN_EXISTING,
        0, None
    )
    lijst = []
    while True:
        lijstout = []
        hr, intdata = win32file.ReadFile(pipe, 60)
        for byte in intdata:
            lijst.append(byte)
            if len(lijst) == 4:
                lijstout.append(int.from_bytes(lijst,byteorder ='little' , signed=True))
                lijst = []
        if len(lijstout) == 15:
            TensorLijstOut = torch.tensor(lijstout, dtype=torch.float32)

            with torch.no_grad():
                output = model(TensorLijstOut)
                gesture_index =torch.argmax(output).item()
                prediction = index_to_label[gesture_index]
                if lastprediction != prediction:
                    print(prediction)
                    lastprediction = prediction
    win32file.CloseHandle(pipe)
