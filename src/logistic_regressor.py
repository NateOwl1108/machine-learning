from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
import math

class LogisticRegressor():
  def __init__(self, dataframe, dependent_variable, upperbound):
    self.upperbound = upperbound
    self.dependent_variable = dependent_variable
    dependent_variable_column = dataframe.columns.index(dependent_variable)
    dependent_list = [math.log(self.upperbound/value -1) for value in dataframe.data_dict[dependent_variable]]
    dependent_transformed = dependent_variable + "_transfromed"
    new_columns = dataframe.columns
    new_columns[dependent_variable_column] = dependent_transformed
    transformed_data_dict = dataframe.data_dict

    #switching out old dependent variable list with transformed one
    transformed_data_dict[dependent_variable] = dependent_list
    transformed_data_dict[dependent_transformed] = transformed_data_dict[dependent_variable]
    del transformed_data_dict[dependent_variable]

    #Creating Dataframe from new datadict
    transformed_datafame = DataFrame(transformed_data_dict, new_columns)

    #linear regressor
    linear_regressor = LinearRegressor(transformed_datafame, dependent_transformed)
    self.coefficients = linear_regressor.coefficients

  def predict(self, mini_dict):
    transformed = self.coefficients['constant']
  
    for key in mini_dict:
      transformed += self.coefficients[key] * mini_dict[key]
    prediction = self.upperbound/(1 + math.exp(transformed) )
    return prediction
