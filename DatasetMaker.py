import csv, os
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
from torchvision.io import decode_image
CSV_file = "gesture_dataset.csv"

def save_sample(features, label):

    rij = {"1":features[0],
           "2":features[1],
           "3":features[2],
           "4":features[3],
           "5":features[4],
           "6":features[5],
           "7":features[6],
           "8":features[7],
           "9":features[8],
           "10":features[9],
           "11":features[10],
           "12":features[11],
           "13":features[12],
           "14":features[13],
           "15":features[14],
           "label": label}
    #write_header = not os.path.exists(CSV_file) # geeft aan of ja er is een header of nee er is een header

    with open(CSV_file, "a", newline="") as csvfile: #opent de csv file en zorg dat er geen lege lijnen zijn
        fieldnames = ['1',
                      '2',
                      '3',
                      '4',
                      '5',
                      '6',
                      '7',
                      '8',
                      '9',
                      '10',
                      '11',
                      '12',
                      '13',
                      '14',
                      '15',
                      'label'
                      ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(rij) #schrijft de rij naar csv


class GestureDataset(Dataset):

    def __init__(self, csv_file):
        df = pd.read_csv(csv_file)
        self.label_map = {name:i for i, name in enumerate(df['label'].unique())} #zorgt ervoor dat elke dubble label weg gaat en elke label een nummer krijgt
        self.features = torch.tensor(df.drop("label", axis=1).values, dtype=torch.float32) #verwijderd alle labels
        self.labels = torch.tensor([self.label_map[i] for i in df["label"]], dtype=torch.long)#zorg ervoor dat alles label in CSV file nummers worden

    def __len__(self):
        return len(self.labels)
    def __getitem__(self, index):
        return self.features[index], self.labels[index]

if os.path.exists(CSV_file) and os.path.getsize(CSV_file) > 0:
    dataset = GestureDataset(CSV_file)
else:
    raise ValueError("Dataset missing or empty")