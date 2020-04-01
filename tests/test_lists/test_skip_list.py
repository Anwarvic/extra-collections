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
    test_empty_skiplist()

