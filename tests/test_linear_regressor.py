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
#testing create create_interaction_terms
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
  '''

df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0],
    [5, 5, [],                0],
    [5, 5, ['mayo'],          0],
    [5, 5, ['jelly'],         0],
    [5, 5, ['mayo', 'jelly'], 0]],
    columns = ['beef', 'pb', 'condiments', 'rating']
)
df = df.create_dummy_variables('condiments')
df = df.create_interaction_terms('beef', 'pb')

df = df.create_interaction_terms('beef', 'mayo')
df = df.create_interaction_terms('beef', 'jelly')
df = df.create_interaction_terms('pb', 'mayo')
df = df.create_interaction_terms('pb', 'jelly')
df = df.create_interaction_terms('mayo', 'jelly')
lin_df = DataFrame(df.data_dict, df.columns)

linear_regressor = LinearRegressor(lin_df, dependent_variable='rating')

# test 8 slices of beef + mayo
observation = {'beef': 8, 'mayo': 1}
assert round(linear_regressor.predict(observation),2) == 11.34


# test 4 tbsp of pb + 8 slices of beef + mayo
observation = {'beef': 8, 'pb': 4, 'mayo': 1}
assert round(linear_regressor.predict(observation),2) == 3.62

# test 8 slices of beef + mayo + jelly
observation = {'beef': 8, 'mayo': 1, 'jelly': 1}
assert round(linear_regressor.predict(observation),2) == 2.79