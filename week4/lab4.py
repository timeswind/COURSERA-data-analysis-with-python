import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

from sklearn.preprocessing import PolynomialFeatures

path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)

# lm = LinearRegression()

# print(lm)

# X = df[['highway-mpg']]
# Y = df['price']

# lm.fit(X,Y)

# Yhat=lm.predict(X)  
# print(Yhat[0:5])
# print(lm.intercept_)
# print(lm.coef_)

# lm1 = LinearRegression()
# lm1.fit(df[['engine-size']], df[['price']])

# # Slope 
# print(lm1.coef_)
# # Intercept
# print(lm1.intercept_)

# #multiple linear regression
# Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
# lm.fit(Z, df['price'])


# width = 12
# height = 10
# plt.figure(figsize=(width, height))
# sns.regplot(x="highway-mpg", y="price", data=df)
# plt.ylim(0,)
# #plt.show()

# plt.figure(figsize=(width, height))
# sns.regplot(x="peak-rpm", y="price", data=df)
# plt.ylim(0,)
# #plt.show()


# #residal plot
# width = 12
# height = 10
# plt.figure(figsize=(width, height))
# sns.residplot(df['highway-mpg'], df['price'])
# #plt.show()

# #Multiple Linear Regression
# Y_hat = lm.predict(Z)
# plt.figure(figsize=(width, height))
# ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
# sns.distplot(Yhat, hist=False, color="b", label="Fitted Values" , ax=ax1)

# plt.title('Actual vs Fitted Values for Price')
# plt.xlabel('Price (in dollars)')
# plt.ylabel('Proportion of Cars')

#plt.show()
#plt.close()

#Polynomial Regression and Pipelines

def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()

x = df['highway-mpg']
y = df['price']

f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)

#PlotPolly(p, x, y, 'highway-mpg')
np.polyfit(x, y, 3)


pr=PolynomialFeatures(degree=2)

print(pr)

Z_pr=pr.fit_transform(Z)

print(Z.shape)