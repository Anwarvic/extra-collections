import pytest
from tests import get_string, get_value, get_list, get_pos_int, get_neg_int, \
    get_neg_float
from extra.lists.priority_queue import PriorityQueue


def test_creating_empty_priority_queue():
    # empty priority queue
    q = PriorityQueue()
    assert q._max_capacity == float("inf")
    assert q._min_priority == float("inf")
    assert q._max_priority == float("-inf")
    assert len(q) == 0
    assert q.is_empty()
    with pytest.warns(UserWarning):
        assert q.dequeue() is None
    with pytest.raises(IndexError):
        q.top()
    q.clear()  # not to through any errors
    assert q._max_capacity == float("inf")
    assert not q.is_full()
    # empty queue with max_capacity == 0
    q = PriorityQueue(max_capacity=0)
    assert q._max_capacity == 0
    assert q._min_priority == float("inf")
    assert q._max_priority == float("-inf")
    assert len(q) == 0
    assert q.is_empty()
    with pytest.warns(UserWarning):
        assert q.dequeue() is None
    with pytest.raises(IndexError):
        q.top()
    with pytest.warns(UserWarning):
        q.enqueue(get_value())
    q.clear()  # not to through any errors
    assert q._max_capacity == 0
    assert q.is_full()


def test_queue_with_max_capacity():
    cap = get_pos_int()
    lst = get_list(length=cap)
    q = PriorityQueue(max_capacity=cap)
    assert q._max_capacity == cap
    for i in lst:
        q.enqueue(i)
    assert len(q) == cap
    assert not q.is_empty()
    assert q.is_full()
    for _ in range(cap):
        q.dequeue()
    assert len(q) == 0
    assert q.is_empty()
    assert q.is_full() is False
    q.enqueue(get_value())
    # test max capacity after clear
    q.clear()
    assert q._max_capacity == cap


def test_queue_with_invalid_max_capacity():
    with pytest.raises(TypeError):
        PriorityQueue(max_capacity=get_list())
    with pytest.raises(TypeError):
        PriorityQueue(max_capacity=get_string())
    with pytest.raises(ValueError):
        PriorityQueue(max_capacity=get_neg_int())
    with pytest.raises(ValueError):
        PriorityQueue(max_capacity=get_neg_float())


def test_creating_queue_with_random_values_given_priority():
    # queue with random values with ascending priority
    lst = get_list(length=100)
    q = PriorityQueue()
    for i, item in enumerate(lst):
        q.enqueue(item, priority=i)
    assert len(q) == len(lst)
    assert not q.is_empty()
    assert not q.is_full()
    for _ in range(len(lst)):
        # dequeue() the highest priority
        assert q.dequeue() == lst.pop()
    assert len(q) == 0
    assert q.is_empty()
    with pytest.warns(UserWarning):
        assert q.dequeue() is None
    assert q.is_full() is False

    # queue with random values with descending priority
    lst = get_list(length=100)
    q = PriorityQueue()
    for i, item in enumerate(lst):
        q.enqueue(item, priority=len(lst) - i)
    assert len(q) == len(lst)
    assert not q.is_empty()
    assert not q.is_full()
    for _ in range(len(lst)):
        # dequeue() the lowest priority
        assert q.dequeue(lowest_priority=True) == lst.pop()
    assert len(q) == 0
    assert q.is_empty()
    with pytest.warns(UserWarning):
        assert q.dequeue() is None
    assert q.is_full() is False


def test_creating_queue_with_random_values_random_priority():
    # queue with random values with ascending priority
    lst = get_list(length=1000)
    q = PriorityQueue()
    for item in lst:
        q.enqueue(item)
    assert len(q) == len(lst)
    assert not q.is_empty()
    assert not q.is_full()
    for _ in range(len(lst)):
        assert q.top() is not None
        q.dequeue()
    assert len(q) == 0
    assert q.is_empty()
    with pytest.warns(UserWarning):
        assert q.dequeue() is None
    assert q.is_full() is False


def test_queue_with_known_values():
    q = PriorityQueue(max_capacity=3)
    q.enqueue(2)
    q.enqueue(40)
    q.enqueue(800)
    assert len(q) == 3
    with pytest.warns(UserWarning):
        q.enqueue(16000)
    assert q.top() == 40
    assert not q.is_empty()
    assert q.is_full()
    q.clear()
    assert q.is_empty()
    assert q._max_capacity == 3
    assert q.is_full() is False
