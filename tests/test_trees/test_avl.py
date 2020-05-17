import pytest
from tests import *
from extra.trees.avl import AVLNode, AVL


def test_avlnode():
    pass





def test_simple_avl_tree():
    # src: Data Structures and Algorithms in Python Book (page: 506)
    avl = AVL()
    avl.insert(44)
    avl.insert(17)
    avl.insert(78)
    avl.insert(32)
    avl.insert(50)
    avl.insert(88)
    avl.insert(48)
    avl.insert(62)
    avl.insert(54)

    verify_bst_rules(avl._root)

    # test main methods
    assert not avl.is_empty()
    assert len(avl) == 9
    assert avl.get_height() == 0
    assert avl.to_list() == []
    assert avl.count_leaf_nodes() == 4
    assert avl.is_balanced()
    assert not avl.is_perfect()
    assert not avl.is_strict()
    assert avl.to_list() == [44, 17, 62, 32, 50, 78, 48, 54, 88]
    
    assert avl.preorder_traverse() == [44, 17, 32, 62, 50, 48, 54, 78, 88]
    assert avl.postorder_traverse() == [32, 17, 48, 54, 50, 88, 78, 62, 44]
    assert avl.inorder_traverse() == [17, 32, 44, 48, 50, 54, 62, 78, 88]
    assert avl.breadth_first_traverse() == [44, 17, 62, 32, 50, 78, 48, 54, 88]
    assert avl.traverse() == [17, 32, 44, 48, 50, 54, 62, 78, 88]
    assert avl.get_max() == 88
    assert avl.get_min() == 17

    # test nodes-heights
    root = avl._root
    assert root.get_data() == 44
    assert root.get_height() == 3
    assert root.get_left().get_data() == 17
    assert root.get_left().get_height() == 1
    assert root.get_left().get_right.get_data() == 32
    assert root.get_left().get_right.get_height() == 0
    assert root.get_left().right_left() is None
    assert root.get_right().get_data() == 62
    assert root.get_right().get_height() == 2
    assert root.get_right().get_left().get_data() == 50
    assert root.get_right().get_left().get_height() == 1
    assert root.get_right().get_left().get_left().get_data() == 48
    assert root.get_right().get_left().get_left().get_height() == 0
    assert root.get_right().get_left().get_left().get_left() is None
    assert root.get_right().get_left().get_left().get_right() is None
    assert root.get_right().get_left().get_right().get_data() == 54
    assert root.get_right().get_left().get_right().get_height() == 0
    assert root.get_right().get_left().get_right().get_left() is None
    assert root.get_right().get_left().get_right().get_right() is None
    assert root.get_right().get_right().get_data() == 78
    assert root.get_right().get_right().get_height() == 1
    assert root.get_right().get_right().get_left() is None
    assert root.get_right().get_right().get_right().get_data() == 88
    assert root.get_right().get_right().get_right().get_height() == 0
    assert root.get_right().get_right().get_right().get_left() is None
    assert root.get_right().get_right().get_right().get_right() is None


