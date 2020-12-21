import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor

df = DataFrame.from_array(
    [[1,0.2],
     [2,0.25],
     [3,0.5]],
    columns = ['hours worked', 'progress']
)


regressor = LinearRegressor(df, dependent_variable='progress')


coefficients = regressor.coefficients
for index in range(len(coefficients)):
  coefficients[index] = round(coefficients[index],5)
assert coefficients == [0.01667, 0.15] # meaning that the model is progress = 0.01667 + 0.15 * (hours worked)
# these coefficients are rounded, but you should not round except for
# in your assert statement



assert round(regressor.predict({'hours worked': 4}),5) == 0.61667