import pytest
from tests import verify_bst_rules
from extra.trees.bst import BSTNode
from extra.trees.splay_tree import SplayTree




def test_splay_tree_example1():
    # example from Data Structures and Algorithm in Python (page: 514)
    stree = SplayTree(8)
    stree.root.set_left(BSTNode(3))
    stree.root.get_left().set_right(BSTNode(4))
    stree.root.get_left().get_right().set_right(BSTNode(6))
    stree.root.get_left().get_right().get_right().set_left(BSTNode(5))
    stree.root.get_left().get_right().get_right().set_right(BSTNode(7))
    stree.root.set_right(BSTNode(10))
    stree.root.get_right().set_right(BSTNode(11))
    stree.root.get_right().get_right().set_right(BSTNode(12))
    stree.root.get_right().get_right().get_right().set_right(BSTNode(16))
    stree.root.get_right().get_right().get_right().get_right().set_left(BSTNode(13))
    stree.root.get_right().get_right().get_right().get_right().set_right(BSTNode(17))
    # let's test it
    assert verify_bst_rules(stree.root)
    assert stree.is_balanced()
    assert not stree.is_perfect()
    assert not stree.is_strict()
    assert len(stree) == 12
    assert stree.get_depth() == stree.get_height() == 5
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
    assert stree.root.get_data() == 14
    assert len(stree) == 13
    assert stree.get_max() == 17
    assert stree.get_min() == 3
    assert not stree.is_balanced()
    assert not stree.is_perfect()
    assert not stree.is_strict()
    assert 14 in stree
    # find 8
    assert stree.find(8)
    assert stree.root.get_data() == 8
    assert verify_bst_rules(stree.root)
    assert len(stree) == 13
    assert stree.get_max() == 17
    assert stree.get_min() == 3
    assert stree.is_balanced()
    assert not stree.is_perfect()
    assert not stree.is_strict()
    # find 2
    assert not stree.find(5.5)
    assert stree.root.get_data() == 5
    assert verify_bst_rules(stree.root)
    assert len(stree) == 13
    assert stree.get_max() == 17
    assert stree.get_min() == 3


