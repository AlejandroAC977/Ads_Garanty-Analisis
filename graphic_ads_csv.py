from df_ads import df
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

def show_fig():
    plt.tight_layout()
    plt.show()

plot_no = 1

#1
fig = plt.figure(figsize=(10,6))
sns.histplot(df['CTR'], bins=30, kde=True)
plt.title(f'{plot_no}. Distribution of Click Through Rate (CTR) Atraves de las Campañas')
show_fig()
plot_no += 1


#2
fig = plt.figure(figsize=(10,6))
sns.histplot(df['CPC'], bins=30, kde=True)
plt.title(f'{plot_no}. Cost Per Click (CPC) Distribucion Mostrando Eficencia de Gasto')
show_fig()
plot_no += 1

#3
fig = plt.figure(figsize=(10,6))
sns.histplot(df['ROAS'], bins=30, kde=True)
plt.title(f'{plot_no}. Return on Ad Spend (ROAS) Distribuido en Campañas')
show_fig()
plot_no += 1    

#4
fig = plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='impressions', y='clicks', hue='platform')
plt.title(f'{plot_no}. Relacion Entre Impresones y Click por Plataforma')
show_fig()
plot_no += 1

#5
fig = plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='clicks', y='conversions', hue='industry')
plt.title(f'{plot_no}. Eficencia de los clicks por Empresa')
show_fig()
plot_no += 1

#6
fig = plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='ad_spend', y='revenue', hue='platform')
plt.title(f'{plot_no}. Ganancia vs Gasto de AD por Plataforma')
show_fig()
plot_no += 1


