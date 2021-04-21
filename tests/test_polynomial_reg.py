import sys
sys.path.append('src')
from dataframe import DataFrame
from polynomial_regressor import PolynomialRegressor

df = DataFrame.from_array(
    [(0,1), (1,2), (2,5), (3,10), (4,20), (5,30)],
    columns = ['x', 'y']
)

constant_regressor = PolynomialRegressor(degree=0)
constant_regressor.fit(df, dependent_variable='y')
print(constant_regressor.coefficients)
{'constant': 11.3333}
print(constant_regressor.predict({'x': 2}))
11.3333

linear_regressor = PolynomialRegressor(degree=1)

linear_regressor.fit(df, dependent_variable='y')
print(linear_regressor.coefficients)
{'constant': -3.2381, 'x': 5.8286}
print(linear_regressor.predict({'x': 2}))
8.4190



quadratic_regressor = PolynomialRegressor(degree=2)
quadratic_regressor.fit(df, dependent_variable='y')
print(quadratic_regressor.coefficients)
{'constant': 1.1071, 'x': -0.6893, 'x^2': 1.3036}
print(round(quadratic_regressor.predict({'x': 2}),4))
4.9429


cubic_regressor = PolynomialRegressor(degree=3)
cubic_regressor.fit(df, dependent_variable='y')
print(cubic_regressor.coefficients)
{'constant': 1.1349, 'x': -0.8161, 'x^2': 1.3730, 'x^3': -0.0093}
print(round(cubic_regressor.predict({'x': 2}),4))
4.9206



quintic_regressor = PolynomialRegressor(degree=5)
quintic_regressor.fit(df, dependent_variable='y')
print(quintic_regressor.coefficients)
{'constant': 1.0000, 'x': -2.9500, 'x^2': 6.9583, 'x^3': -3.9583, 'x^4': 1.0417, 'x^5': -0.0917}
print(quintic_regressor.predict({'x': 2}))
5.0000