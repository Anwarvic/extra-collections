import pytest
from tests import *
from extra.trees.bst import BST



def test_bstnode():
    pass


def test_bst_simple():
    bst = BST(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    # test structure
    assert bst.root.get_data() == 4
    assert bst.root.get_left().get_data() == 2
    assert bst.root.get_right().get_data() == 5
    assert bst.root.get_right().get_left() == None
    assert bst.root.get_right().get_right() == None
    assert bst.root.get_left().get_left().get_data() == 1
    assert bst.root.get_left().get_right().get_data() == 3
    # test various methods
    assert bst.count_leaf_nodes() == 3
    assert bst.get_max() == 5
    assert bst.get_min() == 1
    assert bst.get_height() == 2
    assert bst.is_balanced()
    assert not bst.is_perfect()
    assert bst.is_strict()
    # test __contains__
    assert 1 in bst
    assert 100 not in bst
    assert 1.1 not in bst
    # test __iter__ / traverse
    assert bst.to_list() == [4, 2, 5, 1, 3]
    assert bst.preorder_traverse() == [4, 2, 1, 3, 5]
    assert bst.depth_first_traverse() == [4, 2, 1, 3, 5]
    assert bst.postorder_traverse() == [1, 3, 2, 5, 4]
    assert bst.inorder_traverse() == [1, 2, 3, 4, 5]
    #test remove
    bst.remove(9) #do nothing
    bst.remove(4)
    assert len(bst) == 4
    assert 4 not in bst
    # validate
    with pytest.raises(TypeError):
        None in bst
        get_string() in bst
        get_list() in bst
        bst.insert(None)
        bst.insert(get_string())
        bst.insert(get_list())
        bst.remove(None)
        bst.remove(get_string())
        bst.remove(get_list())



def test_bst_from_iterable():
    pass