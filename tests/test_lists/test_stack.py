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
    assert s.is_full() == False
    with pytest.warns(UserWarning):
        assert s.pop() == None
    with pytest.raises(IndexError):
        s.peek()
    s.clear() #not to through any errors
    assert s.max_capacity == float("inf")
    # empty stack with max_capacity == 0
    s = Stack(max_capacity=0)
    assert s.max_capacity == 0
    assert s.container == []
    assert len(s) == 0
    assert s.is_empty()
    assert s.is_full()
    with pytest.warns(UserWarning):
        assert s.pop() == None
    with pytest.raises(IndexError):
        s.peek()
    with pytest.raises(OverflowError):
        s.push(get_value() )
    s.clear() #not to through any errors
    assert s.max_capacity == 0


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
    assert s.is_full()
    with pytest.raises(OverflowError):
        s.push(get_value())
    for _ in range(cap):
        assert s.peek() == lst[-1]
        assert s.pop() == lst.pop()
    assert len(s) == 0
    assert s.is_empty()
    assert s.is_full() == False
    s.push(get_value())
    # test max capacity after clear
    s.clear()
    assert s.max_capacity == cap


def test_stack_with_invalid_max_capacity():
    with pytest.raises(TypeError):
        Stack(max_capacity=get_list())
        Stack(max_capacity=get_string())
    with pytest.raises(ValueError):
        Stack(max_capacity=get_neg_int())
        Stack(max_capacity=get_neg_float())


def test_creating_stack_with_random_numbers():
    # stack with random values
    lst = get_list(length=100)
    s = Stack()
    for i in lst:
        s.push(i)
    assert s.container == lst
    assert len(s) == len(lst)
    assert s.peek() == lst[-1]
    assert not s.is_empty()
    assert not s.is_full()
    for _ in range(len(lst)):
        assert s.peek() == lst[-1]
        assert s.pop() == lst.pop()
    assert len(s) == 0
    assert s.is_empty()
    with pytest.warns(UserWarning):
        assert s.pop() == None
    assert s.is_full() == False


def test_stack_with_known_values():
    s = Stack(max_capacity=3)
    s.push(2)
    s.push(40)
    s.push(800)
    assert len(s) == 3
    assert s.container == [2, 40, 800]
    with pytest.raises(OverflowError):
        s.push(16000)
    assert s.peek() == 800
    assert s.pop() == 800
    assert s.container == [2, 40]
    assert not s.is_empty()
    assert not s.is_full()
    s.clear()
    assert s.is_empty()
    assert s.max_capacity == 3
    assert s.is_full() == False


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

