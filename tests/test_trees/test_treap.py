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


def test_treap_simple():
    treap = Treap(4)
    treap.insert(2)
    treap.insert(1)
    treap.insert(3)
    treap.insert(5)
    # test structure
    assert verify_bst_rules(treap.root)
    assert verify_treap_priority(treap.root)
    # test various methods
    assert len(treap) == 5
    assert treap.get_max() == 5
    assert treap.get_min() == 1
    # test __contains__
    assert 1 in treap
    assert 100 not in treap
    assert 1.1 not in treap
    # test __iter__ / traverse
    #test remove
    treap.remove(9) #do nothing
    treap.remove(4)
    assert len(treap) == 4
    assert 4 not in treap
    assert verify_bst_rules(treap.root)
    assert verify_treap_priority(treap.root)
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


def test_treap_from_iterable():
    lst = [50, 30, 70, 20, 40, 80, 0]
    treap = Treap.from_iterable(lst, seed="extra")
    # test structure
    assert verify_bst_rules(treap.root)
    assert verify_treap_priority(treap.root)
    assert treap.root.get_data() == 30
    assert treap.root.get_priority() == 87
    assert treap.root.get_left().get_data() == 20
    assert treap.root.get_left().get_priority() == 57
    assert treap.root.get_left().get_left().get_data() == 0
    assert treap.root.get_left().get_left().get_priority() == 5
    assert treap.root.get_left().get_right() is None
    
    assert treap.root.get_right().get_data() == 70
    assert treap.root.get_right().get_priority() == 57
    assert treap.root.get_right().get_left().get_data() == 50
    assert treap.root.get_right().get_left().get_priority() == 3
    assert treap.root.get_right().get_left().get_left().get_data() == 40
    assert treap.root.get_right().get_left().get_left().get_priority() == 2
    assert treap.root.get_right().get_left().get_right() is None
    assert treap.root.get_right().get_right().get_data() == 80
    assert treap.root.get_right().get_right().get_priority() == 13
    assert treap.root.get_right().get_right().get_left() is None
    assert treap.root.get_right().get_right().get_right() is None

    # test various methods
    assert len(treap) == 7
    assert treap.count_leaf_nodes() == 3
    assert treap.get_max() == 80
    assert treap.get_min() == 0
    assert treap.get_height() == 3
    assert treap.is_balanced()
    assert not treap.is_perfect()
    assert not treap.is_strict()
    # test __contains__
    assert 30 in treap
    assert 0 in treap
    assert -10 not in treap
    # test __iter__ / traverse
    assert treap.to_list() == [30, 20, 70, 0, 50, 80, 40]
    assert treap.preorder_traverse() == [30, 20, 0, 70, 50, 40, 80]
    assert treap.depth_first_traverse() == \
        [30, 20, 0, 70, 50, 40, 80]
    assert treap.postorder_traverse()== [0, 20, 40, 50, 80, 70, 30]
    assert treap.inorder_traverse() == [0, 20, 30, 40, 50, 70, 80]
    #test remove
    treap.remove(500) #do nothing
    treap.remove(30)
    assert len(treap) == 6
    assert 30 not in treap
    assert verify_bst_rules(treap.root)
    assert verify_treap_priority(treap.root)


def test_treap_with_random_numbers():
    length = get_pos_int()
    lst = [get_float() for _ in range(length)]
    treap = Treap.from_iterable(lst)
    assert verify_bst_rules(treap.root)
    assert verify_treap_priority(treap.root)
    assert len(treap) == len(lst)
    assert treap.get_max() == max(lst)
    assert treap.get_min() == min(lst)
    for item in lst[1:]:
        assert item in treap
        treap.remove(item)
        assert verify_bst_rules(treap.root)
        assert verify_treap_priority(treap.root)
        assert item not in treap
    assert len(treap) == 1
    with pytest.raises(IndexError): treap.remove(treap.root.get_data())