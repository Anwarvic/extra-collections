import random

def get_int(a=-1000, b=1000):
    return random.randint(a, b)


def get_pos_int(a=0, b=1000):
    return random.randint(a, b)


def get_neg_int(a=-1000, b=0):
    return random.randint(a, b)


def get_float(a=-1000, b=1000):
    return random.uniform(a, b)