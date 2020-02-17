import pytest

from tests import *
from extra.lists.deque import Deque



def test_creating_deque():
    # empty stack
    dq = Deque()
    assert dq.max_capacity == float("inf")
    assert len(dq) == 0
    assert dq.is_empty()
    with pytest.warns(UserWarning):
        assert dq.dequeue() == None
        assert dq.pop_first() == None
        assert dq.pop_last() == None
    with pytest.raises(IndexError):
        dq.get_first()
        dq.get_last()
    dq.clear() #not to through any errors
    assert dq.max_capacity == float("inf")
    assert not dq.is_full()
    # empty stack with max_capacity == 0
    dq = Deque(max_capacity=0)
    assert dq.max_capacity == 0
    assert len(dq) == 0
    assert dq.is_empty()
    with pytest.warns(UserWarning):
        assert dq.dequeue() == None
        assert dq.pop_first() == None
        assert dq.pop_last() == None
    with pytest.raises(IndexError):
        assert dq.get_first() == None
        assert dq.get_last() == None
    with pytest.warns(UserWarning):
        dq.enqueue(get_value())
        dq.append_first(get_value())
        dq.append_last(get_value())
    dq.clear() #not to through any errors
    assert dq.max_capacity == 0
    assert dq.is_full()


def test_deque_with_max_capacity():
    cap = get_pos_int()
    # test append_first/pop_first
    lst = get_list(length=cap)
    dq = Deque(max_capacity=cap)
    assert dq.max_capacity == cap
    for i in lst:
        dq.append_first(i)
    assert len(dq) == cap
    assert not dq.is_empty()
    assert dq.is_full()
    for _ in range(cap):
        assert dq.get_first() == lst[-1]
        assert dq.get_last() == lst[0]
        assert dq.pop_first() == lst.pop()
    assert len(dq) == 0
    assert dq.is_empty()
    assert dq.is_full() == False
    dq.enqueue(get_value())
    # test max capacity after clear
    dq.clear()
    assert dq.max_capacity == cap

    # test append_last/pop_last
    lst = get_list(length=cap)
    dq = Deque(max_capacity=cap)
    assert dq.max_capacity == cap
    for i in lst:
        dq.append_last(i)
    assert len(dq) == cap
    assert not dq.is_empty()
    assert dq.is_full()
    for _ in range(cap):
        assert dq.get_first() == lst[0]
        assert dq.get_last() == lst[-1]
        assert dq.pop_last() == lst.pop()
    assert len(dq) == 0
    assert dq.is_empty()
    assert dq.is_full() == False
    dq.enqueue(get_value())
    # test max capacity after clear
    dq.clear()
    assert dq.max_capacity == cap


def test_deque_with_invalid_max_capacity():
    with pytest.raises(TypeError):
        Deque(max_capacity=get_list())
        Deque(max_capacity=get_string())
    with pytest.raises(ValueError):
        Deque(max_capacity=get_neg_int())
        Deque(max_capacity=get_neg_float())


def test_creating_deque_with_random_numbers():
    # stack with random values
    lst = get_list(length=100)
    dq = Deque()
    for i in lst:
        dq.append_last(i)
    assert len(dq) == len(lst)
    assert dq.get_first() == lst[0]
    assert not dq.is_empty()
    assert not dq.is_full()
    for _ in range(len(lst)):
        assert dq.get_first() == lst[0]
        assert dq.dequeue() == lst.pop(0)
    assert len(dq) == 0
    assert dq.is_empty()
    with pytest.warns(UserWarning):
        assert dq.dequeue() == None
    assert dq.is_full() == False


def test_deque_with_known_values():
    # test using dequeue() / enqueue()
    dq = Deque(max_capacity=3)
    dq.enqueue(2)
    dq.enqueue(40)
    dq.enqueue(800)
    assert len(dq) == 3
    with pytest.warns(UserWarning):
        dq.enqueue(16000)
    assert dq.get_first() == 40
    assert dq.dequeue() == 40
    assert not dq.is_empty()
    assert not dq.is_full()
    dq.clear()
    assert dq.is_empty()
    assert dq.max_capacity == 3
    assert dq.is_full() == False
    # test using append_last() / pop_first()
    dq = Deque(max_capacity=3)
    dq.append_last(2)
    dq.append_last(40)
    dq.append_last(800)
    assert len(dq) == 3
    with pytest.warns(UserWarning):
        dq.append_last(16000)
    assert dq.get_first() == 40
    assert dq.pop_first() == 40
    assert not dq.is_empty()
    assert not dq.is_full()
    dq.clear()
    assert dq.is_empty()
    assert dq.max_capacity == 3
    assert dq.is_full() == False
    # test using append_first() / pop_last()
    dq = Deque(max_capacity=3)
    dq.append_first(2)
    dq.append_first(40)
    dq.append_first(800)
    assert len(dq) == 3
    with pytest.warns(UserWarning):
        dq.append_first(16000)
    assert dq.get_last() == 40
    assert dq.pop_last() == 40
    assert not dq.is_empty()
    assert not dq.is_full()
    dq.clear()
    assert dq.is_empty()
    assert dq.max_capacity == 3
    assert dq.is_full() == False


def test_append_methods():
    dq = Deque()
    with pytest.raises(TypeError):
        dq.enqueue(None)
        dq.append_first(None)
        dq.append_last(None)
    with pytest.raises(ValueError):
        dq.enqueue('')
        dq.append_first('')
        dq.append_last('') 
    dq.enqueue(get_value())
    dq.enqueue(get_int())
    dq.enqueue(get_string())
    dq.enqueue(get_float())
    dq.enqueue(get_list())


