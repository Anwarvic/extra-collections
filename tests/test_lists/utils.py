import random




def get_int(a=-1000, b=1000):
    return random.randint(a, b)


def get_pos_int(a=0, b=1000):
    return random.randint(a, b)


def get_neg_int(a=-1000, b=0):
    return random.randint(a, b)


def get_float(a=-1000, b=1000):
    return random.uniform(a, b)


ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def get_string(length=5):
    s = []
    for _ in range(length):
        s += ALPHABET[get_pos_int(b=length)]
    return "".join(s)


def get_value():
    func = random.choice([get_int, get_float, get_string])
    return func()