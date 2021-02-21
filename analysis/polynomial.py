import sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor

df = DataFrame.from_array([(0.0, 4.0),
 (0.2, 8.9),
 (0.4, 17.2),
 (0.6, 28.3),
 (0.8, 41.6),
 (1.0, 56.5),
 (1.2, 72.4),
 (1.4, 88.7),
 (1.6, 104.8),
 (1.8, 120.1),
 (2.0, 134.0),
 (2.2, 145.9),
 (2.4, 155.2),
 (2.6, 161.3),
 (2.8, 163.6),
 (3.0, 161.5),
 (3.2, 154.4),
 (3.4, 141.7),
 (3.6, 122.8),
 (3.8, 97.1),
 (4.0, 64.0),
 (4.2, 22.9),
 (4.4, -26.8),
 (4.6, -85.7),
 (4.8, -154.4)], columns = ['x', 'y'] )

df = df.create_exponential('x', 2)
df = df.create_exponential('x', 3)

linear_regressor = LinearRegressor(df, dependent_variable='y')
print(linear_regressor.coefficients)
coefficients = linear_regressor.coefficients
print(coefficients['constant'] + .2*coefficients['x'] + .04*coefficients['x^2']+ .008*coefficients['x^3'])

