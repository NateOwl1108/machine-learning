class Matrix():
    def __init__(self, matrix_values):
        self.elements = matrix_values
        self.num_rows = len(matrix_values)
        self.num_cols = len(matrix_values[0])

       
    def copy(self):
      copied_elements = [[entry for entry in row] for row in self.elements]
      return Matrix(copied_elements)

    def add(self, matrix):
        new_matrix = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)] 
        for row in range(self.num_rows): 
            for col in range(self.num_cols ): 
              sum_of_elements= self.elements[row][col] + matrix.elements[row][col]
              new_matrix[row][col] = sum_of_elements
        return Matrix(new_matrix)

    def __add__(self, matrix):
        new_matrix = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)] 
        for row in range(self.num_rows): 
            for col in range(self.num_cols ): 
              sum_of_elements= self.elements[row][col] + matrix.elements[row][col]
              new_matrix[row][col] = sum_of_elements
        return Matrix(new_matrix)
  
    def __sub__(self, matrix):
        new_matrix = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)] 
        for i in range(self.num_rows): 
            for j in range(self.num_cols): 
                sum_of_elements = self.elements[i][j] - matrix.elements[i][j]
                new_matrix[i][j] = sum_of_elements
        return Matrix(new_matrix)

    def scalar_multiply(self, scalar):
        scalar = 1 / scalar
        new_matrix = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)] 
        for row_index in range(len(self.elements)): 
            for col_index in range(len(self.elements[0])): 
              new_matrix[row_index][col_index] = self.elements[row_index][col_index] / scalar
        return Matrix(new_matrix)
    
    def __mul__(self, scalar):
        scalar = 1 / scalar
        new_matrix = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)] 
        for row_index in range(len(self.elements)): 
            for col_index in range(len(self.elements[0])): 
              new_matrix[row_index][col_index] = self.elements[row_index][col_index] / scalar
        return Matrix(new_matrix)
        
    def __rmul__(self, scalar):
        scalar = 1 / scalar
        new_matrix = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)] 
        for row_index in range(len(self.elements)): 
            for col_index in range(len(self.elements[0])): 
              new_matrix[row_index][col_index] = self.elements[row_index][col_index] / scalar
        return Matrix(new_matrix)
    
    def matrix_multiply(self,matrix):
        new_matrix = [[0 for _ in range(self.num_rows)] for _ in range(matrix.num_cols)] 
        for row_index in range(self.num_rows): 
          for col_index in range(matrix.num_cols): 
            row=self.elements[row_index]
            col=[matrix.elements[k][col_index] for k in range(self.num_cols)]
            dot_product = 0
            for i in range(len(row)):
                dot_product += row[i] * col[i]
            new_matrix[row_index][col_index] = dot_product
        return Matrix(new_matrix)
    
    def __matmul__(self,matrix):
        new_matrix = [[0 for _ in range(matrix.num_cols)] for _ in range(self.num_rows)] 
        for row_index in range(self.num_rows): 
          row=self.elements[row_index]
          for col_index in range(matrix.num_cols): 
            col=[matrix.elements[k][col_index] for k in range(self.num_cols)]
            dot_product = 0
            for i in range(len(row)):
                dot_product += round(row[i] * col[i],6)
            new_matrix[row_index][col_index] =dot_product

        return Matrix(new_matrix)

    def transpose(self):
        new_matrix = [[0 for _ in range(self.num_rows)] for _ in range(self.num_cols)] 
        for row_index in range(self.num_rows): 
          for col_index in range(self.num_cols): 
            element = self.elements[row_index][col_index]  
            new_matrix[col_index][row_index] = element 
  
        return Matrix(new_matrix)

    def is_equal(self,matrix):
      if self.num_cols != matrix.num_cols:
        return False
      else: 
        if self.num_rows != matrix.num_rows:
          return False
        else:
          for i in range(len(self.elements)): 
            for j in range(len(self.elements[0])):
              if self.elements[i][j] != matrix.elements[i][j]:
                return False
      return True
    
    def __eq__(self,matrix):
      if self.num_cols != matrix.num_cols:
        return False
      else: 
        if self.num_rows != matrix.num_rows:
          return False
        else:
          for i in range(len(self.elements)): 
            for j in range(len(self.elements[0])):
              if self.elements[i][j] != matrix.elements[i][j]:
                return False
      return True
    
    def get_pivot_row(self, column_index):
      for row in range(self.num_rows):
        for value in range(column_index):
          if(self.elements[row][value] != 0):
            row += 1
        if(self.elements[row][column_index] != 0):
          return row
      return 'None'

    def swap_rows(self, row_index1, row_index2):
      copy_of_elements = self.elements
      copy_of_elements[row_index1], copy_of_elements[row_index2] = copy_of_elements[row_index2], copy_of_elements[row_index1]
      return self.elements
    
    def normalize_row(self, row_index):
      non_zero=[]
      elements = self.elements
      for value in range(self.num_cols):
        if(self.elements[row_index][value] != 0):
           non_zero.append(self.elements[row_index][value])
      diviser = non_zero[0]
      for col in range(self.num_cols):
        self.elements[row_index][col] = self.elements[row_index][col] / diviser
      return self.elements

    def first_non_zero_element_index(self,row_index):
      row = self.elements[row_index]
      first_non_zero_index = 0
      for row_element in row:
        if row_element == 0:
          first_non_zero_index += 1
        else:
          break
      return first_non_zero_index

    def row_subtract(self,list_1, multiplier, list_2):
      result = []
      for i in range(len(list_1)):
        result.append(list_1[i] - multiplier * list_2[i])
      return result

    def clear_below(self, row_index): 
      elements = self.elements
      pivot_index = self.first_non_zero_element_index(row_index)
      row = elements[row_index]
      for row_below_index in range(row_index + 1, self.num_rows):
        row_below = elements[row_below_index]
        multiplier = row_below[pivot_index] / row[pivot_index]
        elements[row_below_index] = self.row_subtract(row_below, multiplier, row)
      return elements
    
    def clear_above(self, row_index):
      elements = self.elements
      pivot_index = self.first_non_zero_element_index(row_index)
      row = elements[row_index]
      for row_above_index in range(row_index):
        row_above = elements[row_above_index]
        multiplier = row_above[pivot_index] / row[pivot_index]
        elements[row_above_index] = self.row_subtract(row_above, multiplier, row)
      return elements

    def rref(self):
      
      row_index = 0
      find_pivot = True
      normalize = True
      clear_above = True
      clear_below = True
      for col_index in range(self.num_cols):
          pivot_row = -1
          for row in range(row_index, self.num_rows):
            if(self.elements[row][col_index] != 0):
              pivot_row = row
              can_be_reduced = True
              break
        
          if pivot_row != -1:
            if pivot_row != row_index:
              self.elements[pivot_row] , self.elements[row_index] = self.elements[row_index] , self.elements[pivot_row]

            self.normalize_row(row_index)
            self.clear_above(row_index)
            self.clear_below(row_index)
            row_index += 1

      return Matrix(self.elements)

    def augment(self, other_matrix):
      new_matrix = self.elements
      
      for row_index in range(self.num_rows):
        
        for col_index in range(other_matrix.num_cols):
          new_matrix[row_index].append(other_matrix.elements[row_index][col_index])
      
      return Matrix(new_matrix)

    def get_rows(self, row_nums):
      new_matrix = []
      
      for row_index in row_nums:
        new_matrix.append(self.elements[row_index])
      
      return Matrix(new_matrix)

    def get_columns(self, col_nums):
      new_matrix = [[] for _ in range(self.num_rows)]
      
      for col_index in col_nums:
        for row_index in range(self.num_rows):
          new_matrix[row_index].append(self.elements[row_index][col_index])
      
      return Matrix(new_matrix)
      
    def inverse(self):
      if self.num_rows != self.num_cols:
        return 'Error: cannot invert a non-square matrix'
      elif self.cofactor_method_determinant == 0:
        return 'Error: cannot invert a singular matrix'
      else:
        identity_matrix = [[0 for _ in range(self.num_rows)] for _ in range(self.num_rows)]
        copy_matrix = Matrix(self.elements)
        for i in range(self.num_rows):
          identity_matrix[i][i] = 1
        for row_index in range(self.num_rows):
          for col_index in range(self.num_cols):
            copy_matrix.elements[row_index].append(identity_matrix[row_index][col_index])
        copy_matrix = Matrix(copy_matrix.elements)
        copy_matrix.rref()
        inverse_matrix = []
        for row_index in range(self.num_rows):
            inverse_matrix.append(copy_matrix.elements[row_index][self.num_cols:])
        return Matrix(inverse_matrix)

    def cofactor_method_determinant(self):
      if self.num_cols != self.num_rows:
        return 'Error: cannot take determinant of a non-square matrix'
      else:
        sign_change = 1
        determinant = 0
        if self.num_cols == 2:
          determinant = (self.elements[0][0]*self.elements[1][1]) - (self.elements[1][0]*self.elements[0][1])
        else:
          for first_row_cols in range(self.num_cols):
            semi_matrix = []
            for row_index in range(1, self.num_rows):
              semi_matrix_row = []
              for col_index in range(first_row_cols):
                semi_matrix_row.append(self.elements[row_index][col_index])
              for col_index in range(first_row_cols + 1, self.num_cols):
                semi_matrix_row.append(self.elements[row_index][col_index])
              semi_matrix.append(semi_matrix_row)
            semi_matrix = Matrix(semi_matrix)
            determinant += sign_change * self.elements[0][first_row_cols]*semi_matrix.determinant()
            sign_change = sign_change * -1
      return determinant

    def exponent(self, power):
      output = Matrix(self.elements)
      for i in range(power-1):
        output = self.matrix_multiply(output)
      return Matrix(output.elements)
    
    def __pow__(self, power):
      output = Matrix(self.elements)
      for i in range(power-1):
        output = self.matrix_multiply(output)
      return Matrix(output.elements)
 
