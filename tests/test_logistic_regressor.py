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

