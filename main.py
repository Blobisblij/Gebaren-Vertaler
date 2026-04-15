import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from DatasetMaker import GestureDataset
from handmodel import runtraining
from handmodel import HandNN

#dataset = GestureDataset("gesture_dataset.csv")
#train_size = int(len(dataset) * 0.8)
#test_size = len(dataset) - train_size
#train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

#train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
#test_loader = DataLoader(test_dataset, batch_size=32, shuffle=True)


#runtraining(50, train_loader, test_loader)