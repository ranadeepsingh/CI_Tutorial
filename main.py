import pandas as pd
import time
import random

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

def train_model():
    '''
    Simulate Model Training and return training time in seconds
    '''
    start_time = time.time()
    print("Training model...")
    time.sleep(random.randint(1,5)) # Simulate training time
    print("Model trained!")

    end_time = time.time()

    return round((end_time - start_time),3)

if __name__ == '__main__':

    print(hello_world())
    print(f"Model Train time: {train_model()} s")
    print(recommend(5))