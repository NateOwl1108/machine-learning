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
    