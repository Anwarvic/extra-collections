import pytest
from tests import *
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
    verify_bst_rules(stree.root)

    # stree.insert(14)
    # # stree.find(13)
    # print(stree)
    # print(stree.is_balanced())
    # stree.find(8)
    # print(stree)
    # print(stree.is_balanced())