import csv, os
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
from torchvision.io import decode_image
CSV_file = "gesture_dataset.csv"
import Training_program
def save_sample(List1A, List1B, List1C, List2A, List2B, List2C, List3A, List3B, List3C, List4A, List4B, List4C, List5A, List5B, List5C, label):
    features = []
    for item in[List1A, List1B, List1C,
                List2A, List2B, List2C,
                List3A, List3B, List3C,
                List4A, List4B, List4C,
                List5A, List5B, List5C,]:
        features.extend([item[1],item[2], item[3]]) #stops laagste hoogste en gemiddelde van elke lijst in 1 lijst van 45 nummers
    rij = features + [label]
    write_header = not os.path.exists(CSV_file) # geeft aan of ja er is een header of nee er is een header

    with open(CSV_file, "a", newline="") as csvfile: #opent de csv file en zorg dat er geen lege lijnen zijn
        writer = csv.writer(csvfile)
        if write_header: # kijkt of er een header is
            header = [f"f{i}" for i in range(45)] + ["label"]
            writer.writerow(header)
        writer.writerow(rij) #schrijft de rij naar csv


class GestureDataset(Dataset):

    def __init__(self, csv_file, root_dir, transform=None):
        df = pd.read_csv(csv_file)
        self.label_map = {name:i for i, name in enumerate(df['label'].unique())} #zorgt ervoor dat elke dubble label weg gaat en elke label een nummer krijgt
        self.features = torch.tensor(df.drop("label", axis=1).values, dtype=torch.float32) #verwijderd alle labels
        self.labels = torch.tensor([self.label_map[i] for i in df["label"]], dtype=torch.long)#zorg ervoor dat alles label in CSV file nummers worden

    def __len__(self):
        return len(self.labels)
    def __getitem__(self, index):
        return self.features[index], self.labels[index]

    dataset = GestureDataset("gesture_dataset.csv")
    dataloader = Dataloader(dataset, batch_size=32, shuffle=True)

    for features, label in dataloader:
        predictions = model(features)
        loss =loss(predictions, label)
