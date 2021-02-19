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

def steepest_descent_optimizer(n):
  lowest_cost = random_optimizer(100)
  for x in range(n):
    cost = lowest_cost['cost']
    new_location = []
    location_list = []
    lower_value = False
    lowest_value = True
    for index in range(len(lowest_cost['locations'])):
      lowest_cost['locations'][index] = list( lowest_cost['locations'][index])
    index = 0
    for queen in lowest_cost['locations']:
      previous_location_list = list(lowest_cost['locations'])
      
      up = list(previous_location_list)
      up[index][1] = queen[1] - 1
      down = list(previous_location_list)
      down[index][1] = queen[1]+1
      left = list(previous_location_list)
      left[index][0] = queen[0] -1
      right = list(previous_location_list)
      right[index][0] = queen[0]+1
      up_left = list(previous_location_list)
      up_left[index][0] = queen[0]-1
      up_left[index][1] = queen[1]-1
      up_right = list(previous_location_list)
      up_right[index][0] = queen[0]+1
      up_right[index][1] = queen[1]-1
      down_left = list(previous_location_list)
      down_left[index][0] = queen[0]-1
      down_left[index][1] = queen[1]+1
      down_right = list(previous_location_list)
      down_right[index][0] = queen[0]+1
      down_right[index][1] = queen[1]+1

      
      if up[index][1]>=0 and up[index] not in lowest_cost['locations']:
        location_list.append(up)
    
      if up_left[index][1]>=0 and up_left[index][0]>=0 and up_left[index] not in lowest_cost['locations']:
        location_list.append(up_left)

      if up_right[index][1]>=0 and up_right[index][1]<=7 and up_left[index] not in lowest_cost['locations']:
        location_list.append(up_right)

      if down[index][1]<=7 and down[index] not in lowest_cost['locations']:
        location_list.append(down)
    
      if down_left[index][1]<=7 and down_left[index][0]>=0 and down[index] not in lowest_cost['locations']:
        location_list.append(down_left)
    
      if down_left[index][1]<=7 and down_left[index][0]<=7 and down[index] not in lowest_cost['locations']:
        location_list.append(down_right)
      index += 1
    
    
    for locations in location_list:
      if calc_cost(locations) < cost:
        lowest_cost['locations'] = locations
        lowest_cost['cost'] = calc_cost(locations)
        lower_value = True
        lowest_value = False
    
    if lower_value == False:
      for locations in location_list:
        if calc_cost(locations) == cost:
          equal_location_list.append(locations)
          lowest_value = False
    if lowest_value == False:
      equal_location_list = []
      equal_location = equal_location_list[round(random(0,len(equal_location_list)))]
      lowest_cost['locations'] = equal_location
      lowest_cost['cost'] = calc_cost(equal_location)
    if lowest_value == True:
      return lowest_cost
  return lowest_cost

sdo_10 = steepest_descent_optimizer(10)
print(sdo_10)
show_board(sdo_10['locations'])
sdo_50 = steepest_descent_optimizer(50)
print(sdo_50)
show_board(sdo_50['locations'])
sdo_100 = steepest_descent_optimizer(100)
print(sdo_100)
show_board(sdo_100['locations'])
sdo_500 = steepest_descent_optimizer(500)
print(sdo_500)
show_board(sdo_500['locations'])
sdo_1000 = steepest_descent_optimizer(1000)
print(sdo_1000)
show_board(sdo_1000['locations'])
