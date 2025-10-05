

import torch
import torch.nn as nn
import torch.optim as optim
import seaborn as sns
import xgboost as xgb 

 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.calibration import LabelEncoder

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from main import data


x,y=data.loc[ : ,(data.columns!= 'Engine Condition')],data['Engine Condition']
X_train, X_test, Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=69)
X_train,X_val,Y_train,Y_val=train_test_split(X_train,Y_train,test_size=0.5,random_state=69)


label_enc= LabelEncoder()
Y_train =label_enc.fit_transform(Y_train)
Y_val=label_enc.transform(Y_val)
Y_test=label_enc.transform(Y_test)

scalar = StandardScaler()
X_train= scalar.fit_transform(X_train)
X_val= scalar.transform(X_val)
X_test=scalar.transform(X_test)


xgb_classifier=xgb.XGBClassifier(random_state=69)
xgb_classifier.fit(X_train,Y_train)
Y_pred=xgb_classifier.predict(X_val)
test_accuracy= accuracy_score(Y_val,Y_pred)

print(f"Test Accuracy: {test_accuracy:.4f}")
print("\n Classification Report: \n", classification_report(Y_val,Y_pred))
print("Confusion Matrix: ", confusion_matrix(Y_val,Y_pred))



def Engine_Condition_Checker(db1):
    F_E_Condition=xgb_classifier.predict(db1)
    return F_E_Condition[0]
