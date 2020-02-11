import pytest
from tests import *
from extra.lists.stack import Stack



def test_creating_stack():
    # empty stack
    s = Stack()
    assert s.max_capacity == float("inf")
    assert s.container == []
    assert len(s) == 0
    assert s.is_empty()
    assert s.pop() == None
    with pytest.raises(IndexError):
        s.peek()
    

def test_creating_stack_with_random_numbers():
    # stack with random values
    lst = get_list(length=100)
    s = Stack()
    for i in lst:
        s.push(i)
    assert s.container == lst
    assert len(s) == 0
    assert s.peek() == lst[-1]
    assert s.is_empty() == False
    for _ in range(len(lst)):
        assert s.peek() == lst[-1]
        assert s.pop() == lst.pop()
    assert len(s) == 0
    assert s.is_empty()
    assert s.pop() == None
    


def test_push_method():
    pass

