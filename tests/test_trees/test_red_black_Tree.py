import pytest
from tests import verify_bst_rules
from extra.trees.red_black_tree import Color, RedBlackNode, RedBlackTree




def test_red_black_node():
    pass



def test_red_black_special_case():
    rbtree = RedBlackTree(15)
    rbtree.insert(5)
    rbtree.insert(1)
    # test tree characteristics
    assert verify_bst_rules(rbtree.root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 3
    assert rbtree.count_leaf_nodes() == 2
    assert rbtree.get_max() == 15
    assert rbtree.get_min() == 1
    assert rbtree.get_height() == 1
    assert rbtree.is_balanced()
    # check data/colors
    assert isinstance(rbtree.root, RedBlackNode)
    assert rbtree.root.get_data() == 5
    assert rbtree.root.get_color() == Color.BLACK
    assert rbtree.root.get_left().get_data() == 1
    assert rbtree.root.get_left().get_color() == Color.RED
    assert rbtree.root.get_left().get_left() is None
    assert rbtree.root.get_left().get_right() is None

    assert rbtree.root.get_right().get_data() == 15
    assert rbtree.root.get_right().get_color() == Color.RED
    assert rbtree.root.get_right().get_left() is None
    assert rbtree.root.get_right().get_right() is None


def test_red_black_tree_example1():
    # src: https://www.youtube.com/watch?v=eO3GzpCCUSg
    rbtree = RedBlackTree(8)
    rbtree.insert(5)
    rbtree.insert(15)
    rbtree.insert(12)
    rbtree.insert(19)
    rbtree.insert(9)
    rbtree.insert(13)
    rbtree.insert(23)
    rbtree.insert(10)
    # test tree characteristics
    assert verify_bst_rules(rbtree.root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 9
    assert rbtree.count_leaf_nodes() == 4
    assert rbtree.get_max() == 23
    assert rbtree.get_min() == 5
    assert rbtree.get_height() == 3
    assert rbtree.is_balanced()
    # check data/colors
    assert isinstance(rbtree.root, RedBlackNode)
    assert rbtree.root.get_data() == 12
    assert rbtree.root.get_color() == Color.BLACK
    assert rbtree.root.get_left().get_data() == 8
    assert rbtree.root.get_left().get_color() == Color.RED
    assert rbtree.root.get_left().get_left().get_data() == 5
    assert rbtree.root.get_left().get_left().get_color() == Color.BLACK
    assert rbtree.root.get_left().get_left().get_left() is None
    assert rbtree.root.get_left().get_left().get_right() is None
    assert rbtree.root.get_left().get_right().get_data() == 9
    assert rbtree.root.get_left().get_right().get_color() == Color.BLACK
    assert rbtree.root.get_left().get_left().get_left() is None
    assert rbtree.root.get_left().get_right().get_right().get_data() == 10
    assert rbtree.root.get_left().get_right().get_right().get_color() == Color.RED
    assert rbtree.root.get_left().get_right().get_right().get_left() is None
    assert rbtree.root.get_left().get_right().get_right().get_right() is None

    assert rbtree.root.get_right().get_data() == 15
    assert rbtree.root.get_right().get_color() == Color.RED
    assert rbtree.root.get_right().get_left().get_data() == 13
    assert rbtree.root.get_right().get_left().get_color() == Color.BLACK
    assert rbtree.root.get_right().get_left().get_left() is None
    assert rbtree.root.get_right().get_left().get_right() is None
    assert rbtree.root.get_right().get_right().get_data() == 19
    assert rbtree.root.get_right().get_right().get_color() == Color.BLACK
    assert rbtree.root.get_right().get_right().get_left() is None
    assert rbtree.root.get_right().get_right().get_right().get_data() == 23
    assert rbtree.root.get_right().get_right().get_right().get_color() == Color.RED
    assert rbtree.root.get_right().get_right().get_right().get_left() is None
    assert rbtree.root.get_right().get_right().get_right().get_right() is None
    

def test_red_black_tree_example2():
    # src: https://www.geeksforgeeks.org/red-black-tree-set-2-insert/
    rbtree = RedBlackTree(10)
    rbtree.insert(20)
    rbtree.insert(30)
    rbtree.insert(15)
    # test tree characteristics
    assert verify_bst_rules(rbtree.root)
    assert rbtree.is_balanced()
    assert len(rbtree) == 4
    assert rbtree.count_leaf_nodes() == 2
    assert rbtree.get_max() == 30
    assert rbtree.get_min() == 10
    assert rbtree.get_height() == 2
    assert rbtree.is_balanced()
    # check data/colors
    assert isinstance(rbtree.root, RedBlackNode)
    assert rbtree.root.get_data() == 20
    assert rbtree.root.get_color() == Color.BLACK
    assert rbtree.root.get_left().get_data() == 10
    assert rbtree.root.get_left().get_color() == Color.BLACK
    assert rbtree.root.get_left().get_left() is None
    assert rbtree.root.get_left().get_right().get_data() == 15
    assert rbtree.root.get_left().get_right().get_color() == Color.RED
    assert rbtree.root.get_left().get_right().get_left() is None
    assert rbtree.root.get_left().get_right().get_right() is None

    assert rbtree.root.get_right().get_data() == 30
    assert rbtree.root.get_right().get_color() == Color.BLACK
    assert rbtree.root.get_right().get_left() is None
    assert rbtree.root.get_right().get_right() is None

