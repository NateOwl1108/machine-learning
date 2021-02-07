class DataFrame():
  def __init__(self, data_dict, column_order):
    self.data_dict = data_dict
    self.columns = column_order
  
  def to_array(self):
    num_rows = len(self.data_dict[self.columns[0]])
    output_array =[[] for _ in range(num_rows)]
    for key in self.data_dict:
      for num_index in range(num_rows):
        output_array[num_index].append(self.data_dict[key][num_index])
    return output_array

  @classmethod
  def from_array(cls,arr, columns):
    data_dict ={}
    for col_index in range(len(arr[0])):
      data_dict[columns[col_index]] = []
      for row_index in range(len(arr)):
        data_dict[columns[col_index]].append(arr[row_index][col_index])
    return DataFrame(data_dict,columns)


  def select_columns(self, columns):
    output_dict = {}
    index = 0
    for name in columns:
      output_dict[name] = self.data_dict[name]
      index += 1
    return DataFrame(output_dict, columns)
  
  def select_rows(self, rows):
    rows =rows[::-1]
    new_dict = self.data_dict
    for indexes in rows:
      for keys in self.columns:
        new_dict[keys].pop(indexes - 1)
    return DataFrame(new_dict,self.columns)

  def apply(self,column, function):
    new_dict = dict(self.data_dict) 
    for index in range(len(self.data_dict[column])):
      new_dict[column][index] = function(self.data_dict[column][index])
    return DataFrame(new_dict, self.columns)
  
  def convert_row_from_array_to_dict(self, row):
    row_dict = {}
    for index in range(len(row)):
      row_dict[self.columns[index]] = row[index]
    return row_dict

  def select_rows_where(self,function):
    correct_rows = []
    new_dict = {}
    for key in self.columns:
      new_dict[key] = []
    for row_index in range(len(self.columns)):
      row = [] 
      for key in self.columns:
        row.append(self.data_dict[key][row_index])
      row_dict = self.convert_row_from_array_to_dict(row)
      if function(row_dict) == True:
        for key in self.columns: 
          new_dict[key].append(row_dict[key])
    return DataFrame(new_dict, self.columns)

  def order_by(self,column, ascending):
    value_dict = {}
    for index in range(len(self.data_dict[column])):
      value_dict[self.data_dict[column][index]] = []
    for index in range(len(self.data_dict[column])):
      for key in self.columns:
        value_dict[self.data_dict[column][index]].append(self.data_dict[key][index])
    sorted_list = list(self.data_dict[column])
    sorted_list.sort()
    if ascending == False:
      sorted_list = sorted_list[::-1]
    sorted_value_dict = {}
    for index in range(len(sorted_list)):
      sorted_value_dict[sorted_list[index]] = value_dict[sorted_list[index]]
  
    return_dict = {}
    for index in range(len(self.columns)):
      key = self.columns[index]
      return_dict[key] = []
      for value in sorted_value_dict:
        return_dict[key].append(sorted_value_dict[value][index])

    return DataFrame(return_dict, self.columns)
    
  def create_interaction_terms(self, column_1_name, column_2_name):
    value_array = self.to_array()
    column_1 = self.data_dict[column_1_name]
    column_2 = self.data_dict[column_2_name]
    for index in range(len(value_array)):
      value_array[index].append(column_1[index]*column_2[index])
    new_column = str(column_1_name) + " * "+ str(column_2_name)
    columns = self.columns
    columns.append(new_column)
    return DataFrame.from_array(value_array, columns)
    
  def create_dummy_variables(self, column):
    variables = []
    for list_values in self.data_dict[column]:
      for variable in list_values:
        if variable not in variables:
          variables.append(variable)
    new_dict = {}
    for key in self.data_dict:
      if key == column:
        for column_value in variables:
          new_dict[column_value] = []
      else:
        new_dict[key] = self.data_dict[key]
    for column_value in variables:
      for index in range(len(self.data_dict[column])):
        if column_value in self.data_dict[column][index]:
          new_dict[column_value].append(1)
        else:
          new_dict[column_value].append(0)
    columns = []
    for column_value in new_dict:
      columns.append(column_value)
    return DataFrame(new_dict, columns)