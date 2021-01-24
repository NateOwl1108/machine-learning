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
    self.coefficients = {'constant':matrix.elements[0][0]}
    for index in range(len(dataframe.columns) -1):
      self.coefficients[dataframe.columns[index]] = matrix.elements[index+ 1][0]

  def predict(self, mini_dict):
    prediction = self.coefficients['constant']
    for key in mini_dict:
      prediction += self.coefficients[key] * mini_dict[key]
    return prediction
