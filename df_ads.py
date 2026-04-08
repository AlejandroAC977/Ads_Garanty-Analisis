import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv(r'C:\Users\alejandro\Documents\ads_garanty_DC\csv\global_ads_performance_dataset.csv')

if __name__ == "__main__":
    print(df.head())
    print(df.groupby("country")["clicks"].max())
    print(df.sort_values("clicks", ascending=False))
    
