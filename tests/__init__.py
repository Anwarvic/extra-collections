import random




def get_int(a=-1000, b=1000):
    return random.randint(a, b)


def get_pos_int(a=0, b=1000):
    return random.randint(a, b)


def get_neg_int(a=-1000, b=0):
    return random.randint(a, b)


def get_float(a=-1000, b=1000):
    return random.uniform(a, b)


def get_string(length=5):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    s = [ ALPHABET[get_pos_int(b=length)] for _ in range(length) ]
    return "".join(s)


def get_value():
    func = random.choice([get_int, get_float, get_string])
    return func()


def get_list(length=5, _type=None):
    if _type is None:
        return [get_value() for _ in range(length)]
    elif _type == int:
        return [get_int() for _ in range(length)]
    elif _type == float:
        return [get_float() for _ in range(length)]
    elif _type == str:
        return [get_string() for _ in range(length)]
    