import random




def get_int(a=-1000, b=1000):
    return random.randint(a, b)


def get_pos_int(a=1, b=1000):
    return random.randint(a, b)


def get_neg_int(a=-1000, b=-1):
    return random.randint(a, b)


def get_float(a=-1000, b=1000):
    return random.uniform(a, b)

def get_pos_float(a=1, b=1000):
    return random.uniform(a, b)


def get_neg_float(a=-1000, b=-1):
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


#helper function
def verify_bst_rules(start_node):
    """
    This is a helpful function to check if the BST rule is applied over all
    nodes of the tree. By the BST rule, I mean that each subtree on the left
    is lower than the parent; and the subtree on the right is greater than the
    parent
    """ 
    if start_node == None:
        return True
    left_child = start_node.get_left()
    right_child = start_node.get_right()
    if not (left_child is None or left_child.get_data()<start_node.get_data())\
        or \
        not(right_child is None or right_child.get_data()>start_node.get_data()):
        return False
    return verify_bst_rules(left_child) and verify_bst_rules(right_child)
