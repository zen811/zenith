import torch
import torch.nn as nn
import torch.optim as optim

 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(".\engine data.csv")
print(data)