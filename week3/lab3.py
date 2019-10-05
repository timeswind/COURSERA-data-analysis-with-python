import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)

print(df.head())
print(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
df[["engine-size", "price"]].corr()
sns.regplot(x="highway-mpg", y="price", data=df)
df[['highway-mpg', 'price']].corr()
sns.regplot(x="peak-rpm", y="price", data=df)
df[['peak-rpm','price']].corr()
df[["stroke","price"]].corr() 
sns.regplot(x="stroke", y="price", data=df)
df['drive-wheels'].value_counts().to_frame()