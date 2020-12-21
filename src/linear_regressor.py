from matrix import Matrix

class LinearRegressor():
  def __init__(self, dataframe, dependent_variable = 'progress'):
    
    self.dependent_variable = dependent_variable
    data_dict = dataframe.data_dict
    independent_variable = list(dataframe.columns)
    independent_variable.remove(self.dependent_variable)
    independent_variable = independent_variable[0]
    dependent_variable_array = [[value] for value in data_dict[dependent_variable]]
    tall_matrix = [[1] for _ in range(len(data_dict[dependent_variable]))]
    for index in range(len(tall_matrix)):
      tall_matrix[index].append(data_dict[independent_variable][index])
    tall_matrix = Matrix(tall_matrix)
    wide_matrix = tall_matrix.transpose()
    wide_times_tall = wide_matrix @ tall_matrix
    inverse = wide_times_tall.two_by_two_inverse()
    inverse_times_wide = inverse @ wide_matrix
    solution = inverse_times_wide @ Matrix(dependent_variable_array)
    coefficients = []
    for index in range(len(solution.elements)):
      coefficients.append(solution.elements[index][0])
    self.coefficients = coefficients

  def predict(self, mini_dict):
    independent_variable = None
    for key in mini_dict:
      independent_variable = key
    independent_variable_value = mini_dict[independent_variable]
    prediction = self.coefficients[0]
    prediction += independent_variable_value * self.coefficients[1]
    return prediction
