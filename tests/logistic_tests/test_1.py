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
