import pandas as pd

class KNearestNeighborsClassifier():

  def __init__(self, k):
    self.k = k 

  def fit(self, df, dependent_variable):
    self.df = df
    self.dependent_variable = dependent_variable
    x=0

  def compute_distances(self, observation):
    cookie_list = []
    for i in range(len(self.df[self.dependent_variable])):
      differences = 0
      distance = 0
      for cookie in self.df:
        if cookie != self.dependent_variable:
          differences += (observation[cookie] -self.df[cookie][i])**2
        else:
          cookie_list.append([self.df[cookie][i]])
      distance = differences**.5
      cookie_list[i].insert(0,distance)

    return pd.DataFrame(cookie_list, columns = ['distance', self.dependent_variable])

 



  def nearest_neighbors(self,observation):
    distance = self.compute_distances(observation)
    self.nearest_distance_df = distance.sort_values(by = 'distance')
    return self.nearest_distance_df

  def classify(self,observation):
    nearest = self.nearest_neighbors(observation)
    keys = {}
    for i in range(0, self.k):
      if nearest[self.dependent_variable][i] not in keys:
        keys[nearest[self.dependent_variable][i]] = {}

        keys[nearest[self.dependent_variable][i]]['total'] = 1

        keys[nearest[self.dependent_variable][i]] ['distance'] = float(nearest['distance'][i])
      else:
        keys[nearest[self.dependent_variable][i]]['total'] += 1
        new_dis = float(keys[nearest[self.dependent_variable][i]]['distance'])
        new_dis += nearest['distance'][i]  
        keys[nearest[self.dependent_variable][i]]['distance'] = new_dis
    greatest = 0
    distance = None
    classify = None
    for key in keys:
      if keys[key]['total'] > greatest:
        greatest = keys[key]['total']
        classify = key
        distance = keys[key]['distance']
      if keys[key]['total'] == greatest:
        if keys[key]['distance'] < distance:
          greatest = keys[key]['total']
          classify = key
          distance = keys[key]['distance']
      
    return classify



  


