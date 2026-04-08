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

#trainning 
df['profit_label'] = (df['ROAS'] >= 1).astype(int)

X = df[['impressions','clicks','CTR','CPC','ad_spend','conversions','CPA']]
y = df['profit_label']
#split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#scaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#regesion logistica
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

#prediccion
y_pred = model.predict(X_test)
#resultados 
acc = accuracy_score(y_test, y_pred)
print("Model Accuracy:", round(acc*100, 2), "%")

#Matriz de Confusion
fig = plt.figure(figsize=(10,6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix - ROAS Profitability Prediction')
plt.xlabel('Predicted')
plt.ylabel('Actual')
show_fig()