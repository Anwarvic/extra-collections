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
        s.push(get_value() )


def test_stack_with_max_capacity():
    cap = get_pos_int()
    lst = get_list(length=cap)
    s = Stack(max_capacity= cap)
    assert s.max_capacity == cap
    for i in lst:
        s.push(i)
    assert s.container == lst
    assert len(s) == cap
    assert not s.is_empty()
    with pytest.raises(OverflowError):
        s.push(get_value())
    for i in range(cap):
        assert s.pop() == lst.pop()
    assert len(s) == 0
    assert s.is_empty()
    s.push(get_value())


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
    s = Stack()
    with pytest.raises(TypeError):
        s.push(None)
    with pytest.raises(ValueError):
        s.push('')
    s.push(get_value())
    s.push(get_int())
    s.push(get_string())
    s.push(get_float())
    s.push(get_list())


