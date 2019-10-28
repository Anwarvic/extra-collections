"""
num_levels in SkipList is Log(n)

"""
import random

#helper function
def flip_coin():
    return random.choice(['head','tail'])


class Node:
    def __init__(self, value):
        assert type(value) in {int, float}, "SkipList contains numbers only!!"
        pass




class SkipList:
    def __init__(self, value=None):
        pass
    
    def search(self, item):
        #Search is done, with high probability, in O(log(n))
        pass

    def insert(self, item):
        #insertion is done in O(log(n))
        pass

    def remove(self, item):
        #removal is done in O(log(n))
        pass
