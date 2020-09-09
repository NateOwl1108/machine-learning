class Matrix():
  def __init__(self, matrix_values):
    self.elements=matrix_values

  def copy(self):
    return Matrix(self.elements)
  
  def add(self,value):
      new_matrix=[[0,0],[0,0]]
      for i in range(2): 
        for j in range(2): 
          new_matrix[i][j] = self.elements[i][j] + value.elements[i][j]
          
      return Matrix(new_matrix)
  
  def subtract(self,values):
    new_matrix=[[0,0],[0,0]]
    for i in range(2): 
        for j in range(2): 
            new_matrix[i][j] = self.elements[i][j] - values.elements[i][j]
    return Matrix(new_matrix)

  def scalar_multiply(self,scalar):
    new_matrix=[[0,0],[0,0]]
    for i in range(len(self.elements[0])): 
        for j in range(len(self.elements[1])): 
            new_matrix[i][j] =  self.elements[i][j] * scalar
    return Matrix(new_matrix)
    

  def matrix_multiply(self,matrix):
    new_matrix=[[0,0],[0,0]]
    for i in range(len(self.elements[0])): 
        for j in range(len(matrix.elements[0])): 
          for k in range(len(matrix.elements[1])):  
            new_matrix[i][j] += self.elements[i][k] * matrix.elements[k][j]
    return Matrix(new_matrix)

