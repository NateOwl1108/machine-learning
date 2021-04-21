
from dataframe import DataFrame
from matrix import Matrix

class PolynomialRegressor():
  def __init__(self, degree):
    self.degree = degree
  
  def fit(self, dataframe, dependent_variable):
    self.dependent_variable = dependent_variable
    copy_dataframe = DataFrame(dict(dataframe.data_dict), list(dataframe.columns))
    columns = list(copy_dataframe.columns)
    dependent_variable_index = columns.index(dependent_variable)
    columns.pop(dependent_variable_index)
    independent_variable = list(columns)[0]
    self.independent_variable = str(independent_variable)
    for degree in range(1 , self.degree + 1):
      copy_dataframe = copy_dataframe.create_exponential(independent_variable, degree)
    copy_dataframe.data_dict.pop(independent_variable)
    copy_dataframe.columns.remove(independent_variable)
    dependent_variable_column = copy_dataframe.columns.index(dependent_variable)
    dependent_matrix = [[value] for value in copy_dataframe.data_dict[dependent_variable]]
    data_dict = copy_dataframe.data_dict
    length = len(data_dict[dependent_variable])
    tall_matrix = [[1] for _ in range(length)]
    for row in range(length):
      for key in data_dict:
        if key != dependent_variable:
          tall_matrix[row].append(data_dict[key][row])
    
    tall_matrix = Matrix(tall_matrix)
    matrix = tall_matrix.transpose().matrix_multiply(tall_matrix)
    matrix = matrix.inverse() @ tall_matrix.transpose()
    matrix = matrix @ Matrix(dependent_matrix)
    self.coefficients = {'constant':round(matrix.elements[0][0],5)} 
    columns = copy_dataframe.columns
    columns.remove(dependent_variable)
    for index in range(len(columns)):
      self.coefficients[columns[index]] = round(matrix.elements[index+1][0],4)
    
  def predict(self, value):
    prediction = 0
    variable_value = value[self.independent_variable]
    for key in self.coefficients:
      if key == 'constant':
        prediction += self.coefficients[key]
      else:
        power = int(key[-1])
        variable_power = int(variable_value**power)
        prediction +=  variable_power * self.coefficients[key]
    return round(prediction,4)




  