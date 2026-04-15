import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from dataset import GestureDataset
from model import NeuralNetwork

dataset = GestureDataset("gesture_dataset.csv")
train_size = int(len(dataset) * 0.8)
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=True)

model = NeuralNetwork()

loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

runtrainer(50)