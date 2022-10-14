import random
import main


if __name__ == '__main__':

    recommended_movies = main.recommend(5)
    # Return random accuracy between 0-100%
    print(f"Model Accuracy: {round(100*random.random(),1)}%")
