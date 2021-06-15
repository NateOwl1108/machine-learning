from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
import math

class LogisticRegressor():
  def __init__(self, dataframe,upperbound, dependent_variable):
    self.upperbound = upperbound
    self.dependent_variable = dependent_variable
    dataframe.data_dict[dependent_variable] = [0.1 if value==0 else value for value in dataframe.data_dict[dependent_variable]]
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
    independent_dict={}
    for key in self.coefficients:
      if key == 'constant':
        skip = True
      elif key in mini_dict:
        independent_dict[key] = mini_dict[key]
      elif '*' in key:
        skip = True
      else:
        independent_dict[key] = 0
    full_dict = independent_dict
    key_list = [key for key in independent_dict]
    for i in range(len(key_list)):
      for j in range(i+1,len(key_list)):
        full_dict[key_list[i] + ' * ' + key_list[j]] = full_dict[key_list[i]] * full_dict[key_list[j]]
 
    for key in full_dict:
      transformed += self.coefficients[key] * full_dict[key]
    prediction = self.upperbound/(1 + math.exp(transformed) )
    return prediction
  
  def calc_rss(self): 
    #- calculates the sum of squared error for the regressor

  def set_coefficients(self, coeffs): 
    self.coefficient = coeffs  
    #allows you to manually set the coefficients of your regressor by passing in a dictionary of coefficients

  def calc_gradient(self, delta): 
    #- computes the partial derivatives of the RSS with respect to each coefficient

  def gradient_descent(alpha, delta, num_steps, debug_mode=False): 
