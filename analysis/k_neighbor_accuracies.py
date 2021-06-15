import sys
sys.path.append('src')
from k_nearest_neighbors_classifier import KNearestNeighborsClassifier
import pandas as pd 

data= [['Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
['Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
['Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
['Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
['Sugar'       ,     0.02     ,       0.08     ,      0.45     ,     0.45      ],
['Sugar'       ,     0.10     ,       0.15     ,      0.35     ,     0.40      ],
['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ],
['Shortbread'  ,     0.05     ,       0.12     ,      0.28     ,     0.55      ],
['Shortbread'  ,     0.14     ,       0.27     ,      0.31     ,     0.28      ],
['Shortbread'  ,     0.15     ,       0.23     ,      0.30     ,     0.32      ],
['Shortbread'  ,     0.20     ,       0.10     ,      0.30     ,     0.40      ]]
data_columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]
df = pd.DataFrame(
    data,
    columns = data_columns
    )
accuracies = []

def all_ks_accuracies(df):

  #looping through all values of k
  for k_value in range(1,len(df)):
    num_correct = 0
    #looping throught all the rows of the dataframe
    for row_num in range(len(df)):
      # Remove one row from the dataframe
      copy_df = df.copy()

      row = copy_df.iloc[row_num]
      for column in df:
        del df[column][row_num]
      
      #fit the new dataframe to KNearestNeighborsClassifier 
      knn = KNearestNeighborsClassifier(k = k_value)
      knn.fit(copy_df, dependent_variable = 'Cookie Type')

      #classify row
      knn_classify = knn.classify(row)
      if knn_classify == row['Cookie Type']:
        num_correct += 1
        print('correct', row_num)
      else:
        print('incorrect', row_num)
    accuracies.append(num_correct/len(df))
  return accuracies


import math
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import MaxNLocator

accuracies= [0] + all_ks_accuracies(df)
k_values = [k for k in range(len(df))]
print(k_values)

plt.plot(k_values,accuracies, color = 'blue', linewidth = 1)
plt.savefig('K values accuracies.png')
#Why is the accuracy low when k is very low?
#because the data is overfit
#Why is the accuracy low when k is very high?
#Because the data is underfit.
