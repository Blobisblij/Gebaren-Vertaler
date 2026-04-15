#!/venv/bin/python3
import platform
import sys
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
from model.handmodel import NeuralNetwork, train, train_dataloader

if platform.system() == "Windows":
    pipe_path = "\\\\.\\pipe\\Leapcam"

if platform.system() == "Linux":
    pipe_path = "/tmp/Leapcam"
#load model
device = "cpu"
print(f"Using {device} device")
model = NeuralNetwork().to(device)
print(model)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

#collects data to train the model with
if (sys.argv[0] == "train"):
    if (sys.argv[1] != None):
        WordOrLetterToTrain = sys.argv[1]
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
                    ListGoingOut = tuple(lijstout)
                    totalinputdata = totalinputdata + 1
        epochs = 15
        for epoch in range(epochs):
            train(train_dataloader,model,loss_fn)
            torch.save(model, 'handmodel.pth')
        else:
            epochs = 15
            for epoch in range(epochs):
                train(train_dataloader,model,loss_fn)
                torch.save(model, 'handmodel.pth')


#starts the datastream from the leap cam and sends the input to the moddel
if (sys.argv[0] == "run"):
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
                    NeuralNetwork.eval()
                    TensorLijstOut = ToTensor(lijstout)
                    with torch.no_grad():
                        prediction = NeuralNetwork(TensorLijstOut)
                        if lastprediction != prediction:
                            print(prediction)
                            lastprediction = prediction
                    lijst = []