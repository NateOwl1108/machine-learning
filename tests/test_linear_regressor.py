import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
'''
df = DataFrame.from_array(
    [[1,0.2],
     [2,0.25],
     [3,0.5]],
    columns = ['hours worked', 'progress']
)


regressor = LinearRegressor(df, dependent_variable='progress')


coefficients = regressor.coefficients
coefficients_value_list = []

for key in coefficients:
  coefficients_value_list.append(round(coefficients[key],5))
assert coefficients_value_list == [0.01667, 0.15] 

assert round(regressor.predict({'hours worked': 4}),5) == 0.61667
'''
problem_47 = True
if problem_47 == True:
  df = DataFrame.from_array(
    [[0, 0, 1], 
    [1, 0, 2], 
    [2, 0, 4], 
    [4, 0, 8], 
    [6, 0, 9], 
    [0, 2, 2], 
    [0, 4, 5], 
    [0, 6, 7], 
    [0, 8, 6],
    [2, 2, 0],
    [3, 4, 0]],
    columns = ['beef', 'pb', 'rating'])


  df = df.create_interaction_terms('beef', 'pb')
  
  assert df.columns == ['beef', 'pb', 'rating', 'beef * pb']
  assert df.to_array() == [[0, 0, 1, 0], 
    [1, 0, 2, 0], 
    [2, 0, 4, 0], 
    [4, 0, 8, 0], 
    [6, 0, 9, 0], 
    [0, 2, 2, 0], 
    [0, 4, 5, 0], 
    [0, 6, 7, 0], 
    [0, 8, 6, 0],
    [2, 2, 0, 4],
    [3, 4, 0, 12]]

  new_regressor = LinearRegressor(df, dependent_variable='rating')
  coefficients = new_regressor.coefficients
  prediction = new_regressor.predict({'beef':5, 'pb':0, 'beef * pb': 0})
  print(prediction)
  prediction = new_regressor.predict({'beef':5, 'pb':5, 'beef * pb': 25})
  print(prediction)
