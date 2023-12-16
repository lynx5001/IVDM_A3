import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('./Data/original.csv')

#print(df.head(5))

# infos über df einholen
#print(df.loc[800:840])
#print(df.dtypes)
#print(df.info)
#print(df.select_dtypes(include=np.number).head(5))

# checken ob ich einen bool-df bekommen mit isnull()
#print(df.isnull())

# heatmap um überblick über fehlende werte zu bekommen
#sns.heatmap(df.isnull())
#plt.show()

# heatmap um ausreißer in großen daten zu sehen und einen überblick zu erhalten
#sliced_df=df.select_dtypes(include=np.number).iloc[:,1:]
#sns.heatmap(df[['Fare']])
#plt.show()

# heatmap um ausreißer in kleinen werten zu erkennen
#sns.heatmap(df[['Survived','Pclass','SibSp','Parch']])
#plt.show()

# konsolen ausgabe um zu checken ob man float nach int konvertieren kann
#print(df[['Age']].loc[0:200])