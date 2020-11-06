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


data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sarah'])

assert df1.data_dict == {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

print(df1.columns)
assert df1.columns == ['Pete', 'John', 'Sarah']

print(df1.to_array())
assert df1.to_array() == [[1, 2, 3],
 [0, 1, 1],
 [1, 0, 4],
 [0, 2, 0]]

print(df1.data_dict)
df2 = df1.select_columns(['Sarah', 'Pete'])

print(df2.to_array())
assert df2.to_array() == [[3, 1],
 [1, 0],
 [4, 1],
 [0, 0]]

print(df2.columns)
assert df2.columns == ['Sarah', 'Pete']

print(df1.data_dict)
df3 = df1.select_rows([1,3])

print(df3.to_array())
assert df3.to_array() == [[0, 1, 1],
 [0, 2, 0]]