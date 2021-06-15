import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
import math
import matplotlib.pyplot as plt 

df = DataFrame.from_array(
    [(0.0, 7.0),
 (0.2, 5.6),
 (0.4, 3.56),
 (0.6, 1.23),
 (0.8, -1.03),
 (1.0, -2.89),
 (1.2, -4.06),
 (1.4, -4.39),
 (1.6, -3.88),
 (1.8, -2.64),
 (2.0, -0.92),
 (2.2, 0.95),
 (2.4, 2.63),
 (2.6, 3.79),
 (2.8, 4.22),
 (3.0, 3.8),
 (3.2, 2.56),
 (3.4, 0.68),
 (3.6, -1.58),
 (3.8, -3.84),
 (4.0, -5.76),
 (4.2, -7.01),
 (4.4, -7.38),
 (4.6, -6.76),
 (4.8, -5.22)],
    columns = ['x', 'y']
)
#add different columns
df = df.apply_add('x', lambda x: math.sin(x), 'sin(x)')
df = df.apply_add('x', lambda x: math.cos(x), 'cos(x)')
df = df.apply_add('x', lambda x: math.sin(2*x), 'sin(2*x)')
df = df.apply_add('x', lambda x: math.cos(2*x), 'cos(2*x)')
#save x and y values
x_values=list(df.data_dict['x'])
y_values=list(df.data_dict['y'])


#delete x values

df = df.del_column('x')
#find coefficients
linear_regressor = LinearRegressor(df, dependent_variable='y')
coefficients = linear_regressor.coefficients
print(coefficients)

def apply_function(x,function):
  return function(x)
print('x_values')
print(x_values)
print('x_values length', len(x_values))
new_y_values = []
for x in x_values:
  new_y_values.append(apply_function(x, lambda x: coefficients['sin(x)'] * math.sin(x) + coefficients['cos(x)']*math.cos(x) + coefficients['sin(2*x)'] * math.sin(2*x) + coefficients['cos(2*x)']*math.cos(2*x)))
  print('y_values')
  print(new_y_values)
  print('length of new_y_values', len(new_y_values))

plt.subplot(1,1,1)
plt.plot(x_values,y_values)

plt.subplot(2,1,2)
plt.plot(x_values,new_y_values)
plt.savefig('Signal Seperation.png')
plt.show()



