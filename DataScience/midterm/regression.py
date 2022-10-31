import torch
import torch.nn as nn
import torch.nn.functional as F
import pickle
import matplotlib.pyplot as plt
from numpy import dot
from numpy.linalg import norm
import numpy as np


data = pickle.load(open("mid_animal_data_pub.pkl", "rb"))

x_train = torch.from_numpy(data["train_vectors"])
y_train = torch.from_numpy(data["train_labels"])

model = nn.Linear(1000, 5)

optim = torch.optim.Adam(model.parameters(), lr=1)

for epoch in range(10001):
    z = model(x_train)
    cost = F.corss_entropy(z, y_train)

    optim.zero_grad()
    cost.backward()
    optim.step()

    with torch.no_grad():
        if epoch % 1000 == 0:
            print(f"epoch: {epoch}, cost: {cost.item()}")