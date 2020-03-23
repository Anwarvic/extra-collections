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


def test_treap_one_value():
    val = get_int()
    treap = Treap(val)
    # test structure
    assert verify_bst_rules(treap.root)
    assert verify_treap_priority(treap.root)
    assert treap.root.get_data() == val
    # test various methods
    assert treap.count_leaf_nodes() == 1
    assert treap.get_max() == val
    assert treap.get_min() == val
    assert treap.get_height() == 0
    assert treap.is_balanced()
    assert treap.is_perfect()
    assert treap.is_strict()
    # test __contains__
    assert val in treap
    assert 100 not in treap
    assert 1.1 not in treap
    # test __iter__ / traverse
    assert treap.to_list() == [val]
    assert treap.preorder_traverse() == [val]
    assert treap.depth_first_traverse() == [val]
    assert treap.postorder_traverse() == [val]
    assert treap.inorder_traverse() == [val]
    #test remove
    treap.remove(9) #do nothing
    with pytest.raises(IndexError): treap.remove(val)
    # validate
    with pytest.raises(TypeError): None in treap
    with pytest.raises(TypeError): get_string() in treap
    with pytest.raises(TypeError): get_list() in treap
    with pytest.raises(TypeError): treap.insert(None)
    with pytest.raises(TypeError): treap.insert(get_string())
    with pytest.raises(TypeError): treap.insert(get_list())
    with pytest.raises(TypeError): treap.insert(get_int(), get_string())
    with pytest.raises(TypeError): treap.insert(get_int(), get_list())
    with pytest.raises(TypeError): treap.remove(None)
    with pytest.raises(TypeError): treap.remove(get_string())
    with pytest.raises(TypeError): treap.remove(get_list())
