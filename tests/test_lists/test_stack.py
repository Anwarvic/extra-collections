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
    # empty stack with max_capacity == 0
    s = Stack(max_capacity=0)
    assert s.max_capacity == 0
    assert s.container == []
    assert len(s) == 0
    assert s.is_empty()
    assert s.pop() == None
    with pytest.raises(IndexError):
        s.peek()
    with pytest.raises(OverflowError):
        s.push(get_value())



def test_stack_with_max_capacity():
    pass


def test_creating_stack_with_random_numbers():
    # stack with random values
    lst = get_list(length=100)
    s = Stack()
    for i in lst:
        s.push(i)
    assert s.container == lst
    assert len(s) == len(lst)
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

