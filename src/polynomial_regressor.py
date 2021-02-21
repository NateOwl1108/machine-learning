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