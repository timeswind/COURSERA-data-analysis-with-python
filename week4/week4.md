#WEEK 4 Model Development

Model is mathmetic functions

Linear Regression

Predictor x, target Y

Y = b0+b1x


Multiple Linear Regression(MLR)

Y = b0 + b1x1+b2x2…



Import linear_model from scikit-learn

Lm.fit(array of predictor, target)
lm.predit()

Regression Plot
Seaborn.regplot()

Residual Plot
seaborn.residplot()

Distribution plot
Seaborn.distplot()

Polynomial Regression

Special case for linear regression

f = np.polyfit(x,y,3) (polynomial of 3rd order)
p= np.polydl(f) <— Model

Polynomialfeatures from skitleran
Pre-processing data

Normalizaton -> Polynomial transform -> Linear Regression