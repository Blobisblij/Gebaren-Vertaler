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
save_sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"niks")
from torch.utils.data import DataLoader, random_split
from DatasetMaker import Dataset
#setting os spesific var's
if platform.system() == "Windows":
    #pipe_path = "\\\\.\\pipe\\Leapcam"
    import win32file
    pipe_path = r"\\.\pipe\Leapcam"

if platform.system() == "Linux":
    pipe_path = "/tmp/Leapcam"

#load model
device = "cpu"
loss_fn = nn.CrossEntropyLoss()


#collects data to train the model with
if sys.argv[1] == "train":
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
        maxinputdata = 120

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

        win32file.CloseHandle(pipe)  # close after all samples collecte
        dataset = GestureDataset("gesture_dataset.csv")
        num_gestures = len({name: i for i, name in enumerate(dataset['label'].unique())})
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
            torch.save(model, 'handmodel.pth')
        else:
            epochs = 15
            for epoch in range(epochs):
                train(train_loader,model,loss_fn,optimizer)
                test(test_loader,model,loss_fn)
                torch.save(model, 'handmodel.pth')




#starts the datastream from the leap cam and sends the input to the moddel
if (sys.argv[1] == "run"):
    model = torch.load('handmodel.pth', weights_only=False)
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
                    HandNN.eval()
                    TensorLijstOut = ToTensor(lijstout)
                    with torch.no_grad():
                        prediction = HandNN(TensorLijstOut)
                        if lastprediction != prediction:
                            print(prediction)
                            lastprediction = prediction
                    lijst = []