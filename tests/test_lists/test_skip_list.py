import pytest
from tests import *
from extra.lists.skip_list import SkipNode, SkipList




def test_skip_node():
    # can't be empty
    with pytest.raises(TypeError): SkipNode(None)
    with pytest.raises(TypeError): SkipNode(SkipNode(10))
    with pytest.raises(TypeError): SkipNode(get_string())
    with pytest.raises(TypeError): SkipNode(get_list())
    # test SkipNode
    val = get_float()
    _node = SkipNode(val)
    assert _node.get_data() == _node.data == val
    assert _node.get_next() == _node.next == None
    assert _node.get_down() == _node.down == None


def test_empty_skiplist():
    sl = SkipList()
    assert sl.is_empty()
    assert sl.to_list() == [_ for _ in sl] == []
    assert sl.num_levels == len(sl.level_lists) == 1
    assert len(sl.level_lists[0]) == 1
    assert isinstance(sl.level_lists[0].head, SkipNode)
    assert sl.level_lists[0].head.get_data() == float("-inf")
    assert get_value() not in sl
    assert get_string() not in sl
    assert get_list() not in sl
    assert get_float() not in sl
    assert get_int() not in sl
    with pytest.raises(IndexError): sl[get_int()]
    with pytest.raises(NotImplementedError): sl[:]
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
    assert sl.num_levels >= 1
    assert val in sl
    assert sl.to_list() == [_ for _ in sl] == [val]
    assert val+1 not in sl
    # remove
    sl.remove(val)
    assert sl.is_empty()
    assert sl.to_list() == [_ for _ in sl] == []
    assert sl.num_levels == len(sl.level_lists) == 1
    assert len(sl.level_lists[0]) == 1


def test_skiplist_with_same_value():
    val = get_float()
    #################### using insert() ####################
    sl = SkipList()
    for _ in range(get_pos_int()):
        sl.insert(val)
    assert len(sl) == 1
    assert not sl.is_empty()
    assert sl.num_levels >= 1
    assert val in sl
    assert sl.to_list() == [_ for _ in sl] == [val]
    assert val+1 not in sl
    # remove
    sl.remove(val)
    assert sl.is_empty()
    assert sl.to_list() == [_ for _ in sl] == []
    assert sl.num_levels == len(sl.level_lists) == 1
    assert len(sl.level_lists[0]) == 1
    #################### using from_iterable ####################
    val = get_float()
    sl = SkipList.from_iterable([val for _ in range(get_pos_int())])
    assert len(sl) == 1
    assert not sl.is_empty()
    assert sl.num_levels >= 1
    assert val in sl
    assert sl.to_list() == [_ for _ in sl] == [val]
    assert val+1 not in sl
    # remove
    sl.remove(val)
    assert sl.is_empty()
    assert sl.to_list() == [_ for _ in sl] == []
    assert sl.num_levels == len(sl.level_lists) == 1
    assert len(sl.level_lists[0]) == 1

    
def test_skiplist_with_known_values():
    random.seed(1)
    sk = SkipList()
    sk.insert(2)
    sk.insert(2) #do nothing
    sk.insert(0)
    sk.insert(10)
    sk.insert(100)
    sk.insert(50)
    assert not sk.is_empty()
    assert len(sk) == 5
    assert 2 in sk
    assert 10 in sk
    assert 0 in sk
    assert 100 in sk
    assert 50 in sk
    assert 20 not in sk
    assert sk.num_levels == 3
    assert sk.to_list() == [0, 2, 10, 50, 100]
    # check the structure
    assert len(sk.level_lists[0]) == 6
    assert len(sk.level_lists[1]) == 3
    assert len(sk.level_lists[2]) == 2
    assert verify_skiplist(sk)
    # remove an item
    sk.remove(2)
    assert not sk.is_empty()
    assert sk.num_levels == 2
    assert 2 not in sk
    assert 10 in sk
    assert 0 in sk
    assert 100 in sk
    assert 50 in sk
    assert 20 not in sk
    assert sk.to_list() == [0, 10, 50, 100]
    # check the structure
    assert len(sk.level_lists[0]) == 5
    assert len(sk.level_lists[1]) == 2
    assert verify_skiplist(sk)
    # clear
    sk.clear()
    assert len(sk) == 0
    assert sk.num_levels == 1
    assert sk.is_empty()


def test_skiplist_with_random_numbers():
    length = get_pos_int()
    sk = SkipList()
    for i in range(length):
        sk.insert(i)
    assert len(sk) == length
    assert not sk.is_empty()
    assert sk.to_list() == [i for i in range(length)]
    assert sk.num_levels == len(sk.level_lists)
    # search
    for i in range(length):
        assert sk[i] == i
        assert i in sk
    # remove
    for i in range(length):
        sk.remove(i)
    assert sk.is_empty()
    assert len(sk) == 0
    assert sk.num_levels == 1
    assert sk.to_list() == []


def test_skiplist_with_from_iterable():
    pass