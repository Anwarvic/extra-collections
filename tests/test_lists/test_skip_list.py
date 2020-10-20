import pytest
import random
from tests import (
    get_string,
    get_value,
    get_list,
    get_pos_int,
    get_float,
    get_int,
    verify_skiplist,
)
from extra.lists.skip_list import SkipNode, SkipList


def test_skip_node():
    # can't be empty
    with pytest.raises(ValueError):
        SkipNode(None)
    with pytest.raises(TypeError):
        SkipNode(SkipNode(10))
    with pytest.raises(TypeError):
        SkipNode(get_string())
    with pytest.raises(TypeError):
        SkipNode(get_list())
    # test SkipNode
    val = get_float()
    node = SkipNode(val)
    assert node.get_data() == node._data == val
    assert node.get_next() == node._next is None
    assert node.get_down() == node._down is None


def test_empty_skiplist():
    sl = SkipList()
    assert sl.is_empty()
    assert sl.to_list() == [_ for _ in sl] == []
    assert sl.get_height() == len(sl._level_lists) == 1
    assert len(sl._level_lists[0]) == 1
    assert isinstance(sl._level_lists[0]._head, SkipNode)
    assert sl._level_lists[0]._head.get_data() == float("-inf")
    assert get_value() not in sl
    assert get_string() not in sl
    assert get_list() not in sl
    assert get_float() not in sl
    assert get_int() not in sl
    with pytest.raises(IndexError):
        sl[get_int()]
    with pytest.raises(IndexError):
        sl[:]
    # doesn't raise error
    sl.remove(get_value())
    sl.remove(get_int())
    sl.remove(get_float())
    sl.remove(get_string())
    sl.remove(get_list())
    sl.clear()


def test_skiplist_with_one_element():
    val = get_float()
    sl = SkipList()
    sl.insert(val)
    assert len(sl) == 1
    assert not sl.is_empty()
    assert sl.get_height() >= 1
    assert val in sl
    assert sl.to_list() == [_ for _ in sl] == [val]
    assert val + 1 not in sl
    # remove
    sl.remove(val)
    assert sl.is_empty()
    assert sl.to_list() == [_ for _ in sl] == []
    assert sl.get_height() == len(sl._level_lists) == 1
    assert len(sl._level_lists[0]) == 1


def test_skiplist_with_same_value():
    val = get_float()
    # ========== using insert() ==========
    sl = SkipList()
    for _ in range(get_pos_int()):
        sl.insert(val)
    assert len(sl) == 1
    assert not sl.is_empty()
    assert sl.get_height() >= 1
    assert val in sl
    assert sl.to_list() == [_ for _ in sl] == [val]
    assert val + 1 not in sl
    # remove
    sl.remove(val)
    assert sl.is_empty()
    assert sl.to_list() == [_ for _ in sl] == []
    assert sl.get_height() == len(sl._level_lists) == 1
    assert len(sl._level_lists[0]) == 1
    # ========== using from_iterable ==========
    val = get_float()
    sl = SkipList([val for _ in range(get_pos_int())])
    assert len(sl) == 1
    assert not sl.is_empty()
    assert sl.get_height() >= 1
    assert val in sl
    assert sl.to_list() == [_ for _ in sl] == [val]
    assert val + 1 not in sl
    # remove
    sl.remove(val)
    assert sl.is_empty()
    assert sl.to_list() == [_ for _ in sl] == []
    assert sl.get_height() == len(sl._level_lists) == 1
    assert len(sl._level_lists[0]) == 1


def test_skiplist_with_known_values():
    random.seed(1)
    sl = SkipList()
    sl.insert(2)
    sl.insert(2)  # do nothing
    sl.insert(0)
    sl.insert(10)
    sl.insert(100)
    sl.insert(50)
    assert not sl.is_empty()
    assert len(sl) == 5
    assert 2 in sl
    assert 10 in sl
    assert 0 in sl
    assert 100 in sl
    assert 50 in sl
    assert 20 not in sl
    assert sl.get_height() == 3
    assert sl.to_list() == [0, 2, 10, 50, 100]
    # check the structure
    assert len(sl._level_lists[0]) == 6
    assert len(sl._level_lists[1]) == 3
    assert len(sl._level_lists[2]) == 2
    assert verify_skiplist(sl)
    # remove an item
    sl.remove(2)
    assert not sl.is_empty()
    assert sl.get_height() == 2
    assert 2 not in sl
    assert 10 in sl
    assert 0 in sl
    assert 100 in sl
    assert 50 in sl
    assert 20 not in sl
    assert sl.to_list() == [0, 10, 50, 100]
    # check the structure
    assert len(sl._level_lists[0]) == 5
    assert len(sl._level_lists[1]) == 2
    assert verify_skiplist(sl)
    # clear
    sl.clear()
    assert len(sl) == 0
    assert sl.get_height() == 1
    assert sl.is_empty()


def test_skiplist_with_random_numbers():
    length = get_pos_int()
    sl = SkipList()
    # ========== insert at the end & remove by value ==========
    # insert at the end
    for i in range(length):
        sl.insert(i)
    assert len(sl) == length
    assert not sl.is_empty()
    assert sl.to_list() == [i for i in range(length)]
    assert sl.get_height() == len(sl._level_lists)
    # search
    for i in range(length):
        assert sl[i] == i
        assert i in sl
    # remove
    for i in range(length):
        sl.remove(i)
    assert sl.is_empty()
    assert len(sl) == 0
    assert sl.get_height() == 1
    assert sl.to_list() == []
    # ========== insert at the front & remove by index ==========
    # insert at the front
    for i in range(length):
        sl.insert(length - 1 - i)
    assert len(sl) == length
    assert not sl.is_empty()
    assert sl.to_list() == [i for i in range(length)]
    assert sl.get_height() == len(sl._level_lists)
    # search
    for i in range(length):
        assert sl[i] == i
        assert i in sl
    # remove
    for i in range(length):
        del sl[0]
    assert sl.is_empty()
    assert len(sl) == 0
    assert sl.get_height() == 1
    assert sl.to_list() == []


def test_skiplist_with_from_iterable():
    _set = {get_float() for i in range(get_pos_int())}
    sl = SkipList(_set)
    assert len(sl) == len(_set)
    assert not sl.is_empty()
    assert sl.to_list() == sorted(_set)
    assert sl.get_height() == len(sl._level_lists)
    # search
    for i in _set:
        assert i in sl
    # remove
    for i in _set:
        sl.remove(i)
    assert sl.is_empty()
    assert len(sl) == 0
    assert sl.get_height() == 1
    assert sl.to_list() == []
