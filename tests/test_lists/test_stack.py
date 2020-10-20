import pytest
from extra.lists.stack import Stack


def test_creating_stack(helper):
    # empty stack
    s = Stack()
    assert s._max_capacity == float("inf")
    assert s._container == []
    assert len(s) == 0
    assert s.is_empty()
    assert s.is_full() is False
    with pytest.warns(UserWarning):
        assert s.pop() is None
    with pytest.raises(IndexError):
        s.peek()
    s.clear()  # not to through any errors
    assert s._max_capacity == float("inf")
    # empty stack with max_capacity == 0
    s = Stack(max_capacity=0)
    assert s._max_capacity == 0
    assert s._container == []
    assert len(s) == 0
    assert s.is_empty()
    assert s.is_full()
    with pytest.warns(UserWarning):
        assert s.pop() is None
    with pytest.raises(IndexError):
        s.peek()
    with pytest.raises(OverflowError):
        s.push(helper.get_value())
    s.clear()  # not to through any errors
    assert s._max_capacity == 0


def test_stack_with_max_capacity(helper):
    cap = helper.get_pos_int()
    lst = helper.get_list(length=cap)
    s = Stack(max_capacity=cap)
    assert s._max_capacity == cap
    for i in lst:
        s.push(i)
    assert s._container == lst
    assert len(s) == cap
    assert not s.is_empty()
    assert s.is_full()
    with pytest.raises(OverflowError):
        s.push(helper.get_value())
    for _ in range(cap):
        assert s.peek() == lst[-1]
        assert s.pop() == lst.pop()
    assert len(s) == 0
    assert s.is_empty()
    assert s.is_full() is False
    s.push(helper.get_value())
    # test max capacity after clear
    s.clear()
    assert s._max_capacity == cap


def test_stack_with_invalid_max_capacity(helper):
    with pytest.raises(TypeError):
        Stack(max_capacity=helper.get_list())
    with pytest.raises(TypeError):
        Stack(max_capacity=helper.get_string())
    with pytest.raises(ValueError):
        Stack(max_capacity=helper.get_neg_int())
    with pytest.raises(ValueError):
        Stack(max_capacity=helper.get_neg_float())


def test_creating_stack_with_random_numbers(helper):
    # stack with random values
    lst = helper.get_list(length=100)
    s = Stack()
    for i in lst:
        s.push(i)
    assert s._container == lst
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
        assert s.pop() is None
    assert s.is_full() is False


def test_stack_with_known_values():
    s = Stack(max_capacity=3)
    s.push(2)
    s.push(40)
    s.push(800)
    assert len(s) == 3
    assert s._container == [2, 40, 800]
    with pytest.raises(OverflowError):
        s.push(16000)
    assert s.peek() == 800
    assert s.pop() == 800
    assert s._container == [2, 40]
    assert not s.is_empty()
    assert not s.is_full()
    s.clear()
    assert s.is_empty()
    assert s._max_capacity == 3
    assert s.is_full() is False


def test_push_method(helper):
    s = Stack()
    with pytest.raises(ValueError):
        s.push(None)
    s.push("")
    s.push(helper.get_value())
    s.push(helper.get_int())
    s.push(helper.get_string())
    s.push(helper.get_float())
    s.push(helper.get_list())
