import torch
import torch.nn as nn
import torch.optim as optim

 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import pandas as pd
import matplotlib.pyplot as plt



'''0 1 2 3 4    
0= good
1= heating
2= oil leak
3= misfiring 
4= poor performance '''