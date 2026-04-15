#!/venv/bin/python3
import platform
import csv, os
import sys
import torch
import pandas as pd
from torch import nn
from torchvision.transforms import ToTensor
from handmodel import HandNN
from DatasetMaker import GestureDataset ,save_sample
save_sample([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"niks")
from torch.utils.data import DataLoader, random_split
from DatasetMaker import Dataset
#setting os spesific var's
if platform.system() == "Windows":
    pipe_path = "\\\\.\\pipe\\Leapcam"

if platform.system() == "Linux":
    pipe_path = "/tmp/Leapcam"

#load model
device = "cpu"
print(f"Using {device} device")
#selecteerd alle unike labels uit de csv
df = pd.read_csv("gesture_dataset.csv")
num_gestures = len({name:i for i, name in enumerate(df['label'].unique())})
#laad het model met correcte params
model = HandNN(num_gestures).to(device)
print(model)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

#collects data to train the model with
if (sys.argv[1] == "train"):
    if (sys.argv[2] != None):
        WordOrLetterToTrain = sys.argv[2]
        with open(pipe_path, "rb") as pipe:

            lijst =[]
            lijstout = None
            totalinputdata = 0
            maxinputdata = 120
        while(totalinputdata != maxinputdata):
            while lijstout != []:
              lijstout = []
              intdata = pipe.read(60)
              for byte in intdata:
                 lijst.append(byte)
                 if len(lijst) == 4:
                    lijstout.append(int.from_bytes(lijst,byteorder ='little' , signed=True))
                    lijst = []
                    print(lijstout)
                    save_sample(lijstout, WordOrLetterToTrain)
                    totalinputdata = totalinputdata + 1

        dataset = GestureDataset("gesture_dataset.csv")
        train_size = int(len(dataset) * 0.8)
        test_size = len(dataset) - train_size
        train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

        train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
        test_loader = DataLoader(test_dataset, batch_size=32, shuffle=True)


        # epochs = 15
        # for epoch in range(epochs):
        #     train(train_dataloader,model,loss_fn)
        #     torch.save(model, 'handmodel.pth')
        # else:
        #     epochs = 15
        #     for epoch in range(epochs):
        #         train(train_dataloader,model,loss_fn)
        #         torch.save(model, 'handmodel.pth')
        #


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