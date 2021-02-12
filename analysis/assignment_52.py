import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
from logistic_regressor import LogisticRegressor

df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0],
    [5, 5, [],                0],
    [5, 5, ['mayo'],          0],
    [5, 5, ['jelly'],         0],
    [5, 5, ['mayo', 'jelly'], 0]],
    columns = ['beef', 'pb', 'condiments', 'rating']
)
df = df.create_dummy_variables('condiments')
df = df.create_interaction_terms('beef', 'pb')

df = df.create_interaction_terms('beef', 'mayo')
df = df.create_interaction_terms('beef', 'jelly')
df = df.create_interaction_terms('pb', 'mayo')
df = df.create_interaction_terms('pb', 'jelly')
df = df.create_interaction_terms('mayo', 'jelly')
new_regressor = LinearRegressor(df, dependent_variable='rating')
print('linear_regressor')
print(new_regressor.predict({'beef': 8, 'pb': 0 , 'mayo': 1, 'jelly': 0, 'beef * pb': 0, 'beef * mayo': 8, 'beef * jelly': 0, 'pb * mayo': 0, 'pb * jelly': 0, 'mayo * jelly': 0}))
print(new_regressor.predict({'beef': 0, 'pb': 4 , 'mayo': 0, 'jelly': 1, 'beef * pb': 0, 'beef * mayo': 0, 'beef * jelly': 0, 'pb * mayo': 0, 'pb * jelly': 4, 'mayo * jelly': 0}))
print(new_regressor.predict({'beef': 0, 'pb': 4 , 'mayo': 1, 'jelly': 0, 'beef * pb': 0, 'beef * mayo': 0, 'beef * jelly': 0, 'pb * mayo': 4, 'pb * jelly': 0, 'mayo * jelly': 0}))
print(new_regressor.predict({'beef': 8, 'pb': 4 , 'mayo': 1, 'jelly': 0, 'beef * pb': 32, 'beef * mayo': 8, 'beef * jelly': 0, 'pb * mayo': 4, 'pb * jelly': 0, 'mayo * jelly': 0}))
print(new_regressor.predict({'beef': 8, 'pb': 0 , 'mayo': 1, 'jelly': 1, 'beef * pb': 0, 'beef * mayo': 8, 'beef * jelly': 8, 'pb * mayo': 0, 'pb * jelly': 0, 'mayo * jelly': 1}))

df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0.1],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0.1],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0.1],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0.1],
    [5, 5, [],                0.1],
    [5, 5, ['mayo'],          0.1],
    [5, 5, ['jelly'],         0.1],
    [5, 5, ['mayo', 'jelly'], 0.1]],
    columns = ['beef', 'pb', 'condiments', 'rating']
)
df = df.create_dummy_variables('condiments')
df = df.create_interaction_terms('beef', 'pb')

df = df.create_interaction_terms('beef', 'mayo')
df = df.create_interaction_terms('beef', 'jelly')
df = df.create_interaction_terms('pb', 'mayo')
df = df.create_interaction_terms('pb', 'jelly')
df = df.create_interaction_terms('mayo', 'jelly')

log_reg = LogisticRegressor(df,10, dependent_variable = 'rating')
print('logistic_regressor')
print(log_reg.predict({'beef': 8, 'pb': 0 , 'mayo': 1, 'jelly': 0, 'beef * pb': 0, 'beef * mayo': 8, 'beef * jelly': 0, 'pb * mayo': 0, 'pb * jelly': 0, 'mayo * jelly': 0}))
print(log_reg.predict({'beef': 0, 'pb': 4 , 'mayo': 0, 'jelly': 1, 'beef * pb': 0, 'beef * mayo': 0, 'beef * jelly': 0, 'pb * mayo': 0, 'pb * jelly': 4, 'mayo * jelly': 0}))
print(log_reg.predict({'beef': 0, 'pb': 4 , 'mayo': 1, 'jelly': 0, 'beef * pb': 0, 'beef * mayo': 0, 'beef * jelly': 0, 'pb * mayo': 4, 'pb * jelly': 0, 'mayo * jelly': 0}))
print(log_reg.predict({'beef': 8, 'pb': 4 , 'mayo': 1, 'jelly': 0, 'beef * pb': 32, 'beef * mayo': 8, 'beef * jelly': 0, 'pb * mayo': 4, 'pb * jelly': 0, 'mayo * jelly': 0}))
print(log_reg.predict({'beef': 8, 'pb': 0 , 'mayo': 1, 'jelly': 1, 'beef * pb': 0, 'beef * mayo': 8, 'beef * jelly': 8, 'pb * mayo': 0, 'pb * jelly': 0, 'mayo * jelly': 1}))