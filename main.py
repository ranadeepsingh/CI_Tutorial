import pandas as pd

def hello_world():
    '''
    No tutorial is complete without this
    '''
    return "Hello World"

def recommend(num_movies):
    '''
    Returns list of ${num_movies} movies
    '''
    movies_df = pd.read_csv('movies.csv', delimiter='|') # | as delimiter as movies usually have commas in their names
    return ','.join(movies_df.sample(num_movies).values[:,0].tolist()) # Sample 5 movies
