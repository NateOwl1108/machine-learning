import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
from logistic_regressor import LogisticRegressor
#test 1
Test_1 = False
if Test_1 == True:
  df = DataFrame.from_array(
      [[1,0.2],
       [2,0.25],
      [3,0.5]],
      columns = ['x','y']
  )

  log_reg = LogisticRegressor(df, dependent_variable = 'y')
  assert round(log_reg.predict({'x': 5}),3) == 0.777

Test_2 =False
if Test_2 == True:
    df = DataFrame.from_array(
    [[0, 0, 1, 0], 
    [1, 0, 2, 0], 
    [2, 0, 4, 0], 
    [4, 0, 8, 0], 
    [6, 0, 9, 0], 
    [0, 2, 2, 0], 
    [0, 4, 5, 0], 
    [0, 6, 7, 0], 
    [0, 8, 6, 0],
    [2, 2, 0.1, 4],
    [3, 4, 0.1, 12]],
    columns = ['beef', 'pb', 'rating', 'interactive']
    )
    log_reg = LogisticRegressor(df,10, dependent_variable = 'rating')
    print(log_reg.predict({'beef': 5, 'pb': 0 , 'interactive':0}))
    print(log_reg.predict({'beef': 12, 'pb': 0 , 'interactive':0}))
    print(log_reg.predict({'beef': 5, 'pb': 5 , 'interactive':25}))

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
log_df = DataFrame(df.data_dict, df.columns)



logistic_regressor = LogisticRegressor(log_df,10, dependent_variable = 'rating')

# test 8 slices of beef + mayo
observation = {'beef': 8, 'mayo': 1}

assert round(logistic_regressor.predict(observation),2) == 9.72



# test 4 tbsp of pb + 8 slices of beef + mayo
observation = {'beef': 8, 'pb': 4, 'mayo': 1}

assert round(logistic_regressor.predict(observation),2) == 0.77

# test 8 slices of beef + mayo + jelly
observation = {'beef': 8, 'mayo': 1, 'jelly': 1}
assert round(logistic_regressor.predict(observation),2) == 0.79