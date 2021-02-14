from matrix import Matrix

class LinearRegressor():
  def __init__(self, dataframe, dependent_variable):
    self.dataframe = dataframe
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
      prediction += self.coefficients[key] * full_dict[key]
    return prediction
