import pytest
from tests import *
from extra.trees.treap import TreapNode, Treap




def test_treap_node():
    with pytest.raises(TypeError): TreapNode(None)
    with pytest.raises(TypeError): TreapNode('  ')
    with pytest.raises(TypeError): TreapNode(Treap(get_int()))
    with pytest.raises(TypeError): TreapNode(TreapNode(get_int()))
    with pytest.raises(TypeError): TreapNode(get_string())
    with pytest.raises(TypeError): TreapNode(get_list())
    # check priority
    with pytest.raises(TypeError): TreapNode(get_int(), get_string())
    with pytest.raises(TypeError): TreapNode(get_int(), get_list())
    # these shouldn't raise any erros
    for val in [get_int(), get_float()]:
        priority = get_int()
        node = TreapNode(val, priority)
        assert node.get_data() == val
        assert node.get_priority() == priority
        assert node.get_left() == node.get_right() == None
        assert node.get_children() == []
        with pytest.raises(AssertionError): node.set_priority(get_string())
        with pytest.raises(AssertionError): node.set_priority(get_list())