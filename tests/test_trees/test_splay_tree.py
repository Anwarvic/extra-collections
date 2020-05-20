import pytest
from tests import verify_bst_rules
from extra.trees.bst import BSTNode
from extra.trees.splay_tree import SplayTree




def test_splay_tree_example1():
    # example from Data Structures and Algorithm in Python (page: 514)
    stree = SplayTree()
    stree._root = BSTNode(8)
    stree._root.set_left(BSTNode(3))
    stree._root.get_left().set_right(BSTNode(4))
    stree._root.get_left().get_right().set_right(BSTNode(6))
    stree._root.get_left().get_right().get_right().set_left(BSTNode(5))
    stree._root.get_left().get_right().get_right().set_right(BSTNode(7))
    stree._root.set_right(BSTNode(10))
    stree._root.get_right().set_right(BSTNode(11))
    stree._root.get_right().get_right().set_right(BSTNode(12))
    stree._root.get_right().get_right().get_right().set_right(BSTNode(16))
    stree._root.get_right().get_right().get_right().get_right().set_left(BSTNode(13))
    stree._root.get_right().get_right().get_right().get_right().set_right(BSTNode(17))
    # let's test it
    assert verify_bst_rules(stree._root)
    assert stree.is_balanced()
    assert not stree.is_perfect()
    assert not stree.is_strict()
    assert stree.get_depth() == 0
    assert stree.get_height() == 5
    assert stree.count_leaf_nodes() == 4
    assert stree.get_max() == 17
    assert stree.get_min() == 3
    assert stree.to_list() == [8, 3, 10, 4, 11, 6, 12, 5, 7, 16, 13, 17]
    for item in [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17]:
        assert item in stree
    assert 101 not in stree
    assert -8 not in stree
    assert 0 not in stree
    # insert 14
    stree.insert(14)
    assert stree._root.get_data() == 14
    assert stree.get_max() == 17
    assert stree.get_min() == 3
    assert not stree.is_balanced()
    assert not stree.is_perfect()
    assert not stree.is_strict()
    assert 14 in stree
    # find 8
    assert stree.find(8)
    assert stree._root.get_data() == 8
    assert verify_bst_rules(stree._root)
    assert stree.get_max() == 17
    assert stree.get_min() == 3
    assert stree.is_balanced()
    assert not stree.is_perfect()
    assert not stree.is_strict()
    # find 2
    assert not stree.find(5.5)
    assert stree._root.get_data() == 5
    assert verify_bst_rules(stree._root)
    assert stree.get_max() == 17
    assert stree.get_min() == 3


def test_splay_tree_example2():
    # example from Data Structures and Algorithm in Python (page: 517)
    stree = SplayTree()
    stree._root = BSTNode(8)
    stree._root.set_left(BSTNode(3))
    stree._root.get_left().set_right(BSTNode(4))
    stree._root.get_left().get_right().set_right(BSTNode(6))
    stree._root.get_left().get_right().get_right().set_left(BSTNode(5))
    stree._root.get_left().get_right().get_right().set_right(BSTNode(7))
    stree._root.set_right(BSTNode(10))
    stree._root.get_right().set_right(BSTNode(11))
    # let's test it
    assert verify_bst_rules(stree._root)
    assert not stree.is_balanced()
    assert not stree.is_perfect()
    assert not stree.is_strict()
    assert stree.get_depth() == 0
    assert stree.get_height() == 4
    assert stree.count_leaf_nodes() == 3
    assert stree.get_max() == 11
    assert stree.get_min() == 3
    assert stree.to_list() == [8, 3, 10, 4, 11, 6, 5, 7]
    for item in [8, 3, 10, 4, 11, 6, 5, 7]:
        assert item in stree
    assert 101 not in stree
    assert -8 not in stree
    assert 0 not in stree
    # remove 8
    stree.remove(8)
    assert stree._root.get_data() in {7, 10}
    assert verify_bst_rules(stree._root)
    assert 8 not in stree
    assert stree.get_max() == 11
    assert stree.get_min() == 3
    assert not stree.is_balanced()
    assert not stree.is_perfect()
    assert not stree.is_strict()


def test_splay_tree_example3():
    stree = SplayTree()
    stree._root = BSTNode(50)
    lst = []
    for i, item in enumerate([50, 20, 70, 30, 60, 80, 2, 28, 35]):
        stree.insert(item)
        lst.append(item)
        assert stree._root.get_data() == item
        assert verify_bst_rules(stree._root)
        assert stree.get_max() == max(lst)
        assert stree.get_min() == min(lst)
    # remove 30
    stree.remove(30)
    assert stree._root.get_data() in {28, 35}
    assert verify_bst_rules(stree._root)