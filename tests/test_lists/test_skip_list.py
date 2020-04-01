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


