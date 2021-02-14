from matrix import Matrix

class LinearRegressor():
  def __init__(self, dataframe, dependent_variable):
    
    self.dependent_variable = dependent_variable
    dependent_variable_column = dataframe.columns.index(dependent_variable)
    dependent_matrix = [[value] for value in dataframe.data_dict[dependent_variable]]
    data_dict = dataframe.data_dict
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
    columns = dataframe.columns
    columns.remove(dependent_variable)
   
    for index in range(len(columns)):
      self.coefficients[columns[index]] = round(matrix.elements[index+1][0],5)

  def predict(self, mini_dict):
    prediction = self.coefficients['constant']
    zero_dict = {}
    for key in self.coefficients:
      if key == 'constant':
        skip = True
      elif key in mini_dict:
        zero_dict[key] = mini_dict[key]
      else:
        zero_dict[key] = 0
      for k
    print(zero_dict)
    for key in zero_dict:
      print(prediction)
      prediction += self.coefficients[key] * zero_dict[key]
    return prediction
