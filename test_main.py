from main import *

def test_hello_world():

    ret = hello_world()
    # Should return a string
    assert type(ret) == str
    # Should return "Hello World"
    assert ret == "Hello World"
    
def test_recommend():

    num_movies = 5
    ret = recommend(num_movies)
    # Should return a string
    assert type(ret) == str
    # Should return 20 recommendations
    assert len(ret.split(',')) == num_movies