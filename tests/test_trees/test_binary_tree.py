import pytest
from tests import *
from extra.trees.binary_tree import BinaryTreeNode, BinaryTree


def test_binary_treenode():
    pass


def test_binary_tree():
    # create tree using BinaryTreeNode
    root = BinaryTreeNode("GrandFather")
    root.set_left(BinaryTreeNode("Father"))
    root.get_left().set_left(BinaryTreeNode("Me"))
    root.get_left().set_right(BinaryTreeNode("Sibling"))
    root.set_right(BinaryTreeNode("Uncle"))
    root.get_right().set_left(BinaryTreeNode("Cousin"))
    root.get_right().set_right(BinaryTreeNode("Cousin"))
    btree = BinaryTree(root)
    #test tree structure
    assert btree.root.get_data() == "GrandFather"
    assert btree.root.get_left().get_data() == "Father"
    assert btree.root.get_left().get_left().get_data() == "Me"
    assert btree.root.get_left().get_right().get_data() == "Sibling"
    assert btree.root.get_left().get_left().get_left() is None
    assert btree.root.get_left().get_left().get_right() is None
    assert btree.root.get_left().get_right().get_left() is None
    assert btree.root.get_left().get_right().get_right() is None
    assert btree.root.get_right().get_data() == "Uncle"
    assert btree.root.get_right().get_left().get_data() == "Cousin"
    assert btree.root.get_right().get_right().get_data() == "Cousin"
    assert btree.root.get_right().get_left().get_left() is None
    assert btree.root.get_right().get_left().get_right() is None
    assert btree.root.get_right().get_right().get_left() is None
    assert btree.root.get_right().get_right().get_right() is None
    # test various functions
    assert btree.get_depth() == btree.get_height() == 2
    assert btree.is_balanced()
    assert btree.is_perfect()
    assert btree.is_strict()
    assert len(btree) == 7
    assert btree.count_leaf_nodes() == 4
    assert [item.get_data() for item in btree] == btree.to_list() == \
        ["GrandFather", "Father", "Uncle", "Me", "Sibling", "Cousin", "Cousin"]
    assert btree.preorder_traverse() == btree.depth_first_traverse() == \
        ["GrandFather", "Father", "Me", "Brother", "Uncle", "Cousin", "Cousin"]
    assert btree.postorder_traverse() == \
        ["Me", "Brother", "Father", "Cousin", "Cousin", "Uncle", "GrandFather"]
    assert btree.inorder_traverse() == \
        ["Me", "Father", "Brother", "GrandFather", "Cousin", "Uncle", "Cousin"]
    assert btree.breadth_first_traverse() == \
        ["GrandFather", "Father", "Uncle", "Me", "Sibling", "Cousin", "Cousin"]
    assert btree.get_nodes() == [["GrandFather"],
                                 ["Father", "Uncle"],
                                 ["Me", "Sibling", "Cousin", "Cousin"]]
    with pytest.raises(TypeError):
        BinaryTree(None)
        BinaryTree("    ")
    with pytest.raises(ValueError):
        btree.traverse(get_string())
        btree.traverse(get_list())
        btree.traverse(get_value())
        btree.traverse(get_float())


def test_parse():
    pass

