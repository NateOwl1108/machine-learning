class Matrix():
    def __init__(self, matrix_values):
        self.elements = matrix_values
        self.num_rows = len(matrix_values)
        self.num_cols = len(matrix_values[0])
       
        

    def copy(self):
        return Matrix(self.elements)

    def add(self, matrix):
        new_matrix = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)] 
        for row in range(self.num_rows): 
            for col in range(self.num_cols ): 
              sum_of_elements= self.elements[row][col] + matrix.elements[row][col]
              new_matrix[row][col] = sum_of_elements

        return Matrix(new_matrix)
  
    def subtract(self, matrix):
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
    
    def get_pivot_row(self, column_index):
      for row in range(self.num_rows):
        for value in range(column_index):
          if(self.elements[row][value] != 0):
            row += 1
        if(self.elements[row][column_index] != 0):
          return row
      return 'None'
# see if all entries to left of index are zero
    def swap_rows(self, row_index1, row_index2):
      self.elements[row_index1], self.elements[row_index2] = self.elements[row_index2], self.elements[row_index1]
      return self.elements
    
    def normalize_row(self, row_index):
      non_zero=[]
      for value in range(self.num_cols):
        if(self.elements[row_index][value] != 0):
           non_zero.append(self.elements[row_index][value])
      diviser = non_zero[0]
      for col in range(self.num_cols):
        self.elements[row_index][col] = int(self.elements[row_index][col] / diviser)
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
      pivot_index = self.first_non_zero_element_index(row_index)
      row = self.elements[row_index]
      for row_below_index in range(row_index + 1, self.num_rows):
        row_below = self.elements[row_below_index]
        multiplier = row_below[pivot_index] / row[pivot_index]
        self.elements[row_below_index] = self.row_subtract(row_below, multiplier, row)
      return self.elements
    
    def clear_above(self, row_index):
      pivot_index = self.first_non_zero_element_index(row_index)
      row = self.elements[row_index]
      for row_above_index in range(row_index):
        row_above = self.elements[row_above_index]
        multiplier = row_above[pivot_index] / row[pivot_index]
        self.elements[row_above_index] = self.row_subtract(row_above, multiplier, row)
      return self.elements

