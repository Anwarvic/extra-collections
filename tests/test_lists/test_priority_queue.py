import pytest
from tests import *
from extra.lists.priority_queue import PriorityNode, PriorityQueue





def test_creating_empty_priority_queue():
    # empty stack
    q = PriorityQueue()
    assert q.max_capacity == float("inf")
    assert q.min_priority == float("inf")
    assert q.max_priority == float("-inf")
    assert len(q) == 0
    assert q.is_empty()
    with pytest.warns(UserWarning):
        assert q.dequeue() == None
    with pytest.raises(IndexError):
        q.top()
    q.clear() #not to through any errors
    assert q.max_capacity == float("inf")
    assert not q.is_full()
    # empty queue with max_capacity == 0
    q = PriorityQueue(max_capacity=0)
    assert q.max_capacity == 0
    assert q.min_priority == float("inf")
    assert q.max_priority == float("-inf")
    assert len(q) == 0
    assert q.is_empty()
    with pytest.warns(UserWarning):
        assert q.dequeue() == None
    with pytest.raises(IndexError):
        q.top()
    with pytest.warns(UserWarning):
        q.enqueue(get_value() )
    q.clear() #not to through any errors
    assert q.max_capacity == 0
    assert q.is_full()


def test_queue_with_max_capacity():
    cap = get_pos_int()
    lst = get_list(length=cap)
    q = PriorityQueue(max_capacity=cap)
    assert q.max_capacity == cap
    for i in lst:
        q.enqueue(i)
    assert len(q) == cap
    assert not q.is_empty()
    assert q.is_full()
    for _ in range(cap):
        q.dequeue()
    assert len(q) == 0
    assert q.is_empty()
    assert q.is_full() == False
    q.enqueue(get_value())
    # test max capacity after clear
    q.clear()
    assert q.max_capacity == cap


