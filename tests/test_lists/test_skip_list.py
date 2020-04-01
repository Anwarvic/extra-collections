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
    assert sl.num_levels == len(sl.level_lists) == 1
    assert len(sl.level_lists[0]) == 1
    assert isinstance(sl.level_lists[0].head, SkipNode)
    assert sl.level_lists[0].head.get_data() == float("-inf")


