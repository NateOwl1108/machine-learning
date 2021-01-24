from random import random
def show_board(locations):
  board = [['.' for _ in range(8)] for _ in range(8)] 
  for index in range(len(locations)):
    board[locations[index][0]][locations[index][1]] = str(index)
  for row in board:
    row_string = '  '.join(row)
    print(row_string)

def calc_cost(locations):
  cost = 0
  length =  len(locations)
  for point in range(length):
    for other_points in range(length):
      if other_points != point:
        #same row
        if locations[point][0] == locations[other_points][0] :
          cost+= 1
        if locations[point][1] == locations[other_points][1]:
          cost+= 1
        if abs(locations[point][0] - locations[other_points][0]) == abs(locations[point][1] - locations[other_points][1]):
          cost+=1
  return cost/2
def random_location(locations):
  x = round(7*random())
  y = round(7*random())
  for location in locations:
    if location == (x,y):
      random_location(locations)
  return (x,y)

def random_optimizer(n):
  lowest_cost ={}
  lowest_cost['locations']=[]
  lowest_cost['cost']=999999
  for i in range(n):
    locations = [(round(7*random()),round(7*random()))]
    for l in range(7):
      location = random_location(locations)
      locations.append(location)
    if calc_cost(locations) < lowest_cost['cost']:
      lowest_cost['locations']=locations
      lowest_cost['cost'] = calc_cost(locations)
  return lowest_cost
      
        
locations = [(0,0), (6,1), (2,2), (5,3), (4,4), (7,5), (1,6),(2,6)]
show_board(locations)
print(calc_cost(locations))
print(random_optimizer(10))
print(random_optimizer(50))
print(random_optimizer(100))
print(random_optimizer(500))
print(random_optimizer(1000))