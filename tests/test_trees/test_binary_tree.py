import pytest
from tests import *
from extra.trees.binary_tree import BinaryTreeNode, BinaryTree




def test_binary_treenode():
    with pytest.raises(ValueError): BinaryTreeNode(None)
    with pytest.raises(TypeError): BinaryTreeNode(BinaryTreeNode(get_int()))
    # make sure white-spaces are normalized
    assert BinaryTreeNode('\nap\nple\n').get_data() == "\\nap\\nple\\n"
    # the following shouldn't raise anything
    for val in [get_int(), get_float(), get_string(), get_list()]:
        node = BinaryTreeNode(val)
        assert node.get_data() == val
        assert node.get_left() == node.get_right() == None
        assert node.get_children() == []


def test_empty_binary_tree(btree=BinaryTree()):
    assert len(btree) == 0
    assert btree.is_empty()
    assert btree.get_height() == 0
    assert btree.to_list() == []
    assert btree.count_leaf_nodes() == 0
    with pytest.warns(UserWarning): btree.is_balanced()
    with pytest.warns(UserWarning): btree.is_perfect()
    with pytest.warns(UserWarning): btree.is_strict()
    assert btree.preorder_traverse() == []
    assert btree.postorder_traverse() == []
    assert btree.inorder_traverse() == []
    assert btree.breadth_first_traverse() == []
    assert btree.traverse() == []


def test_binary_tree():
    # create tree using BinaryTreeNode
    root = BinaryTreeNode("GrandFather")
    root.set_left(BinaryTreeNode("Father"))
    root.get_left().set_left(BinaryTreeNode("Me"))
    root.get_left().set_right(BinaryTreeNode("Sibling"))
    root.set_right(BinaryTreeNode("Uncle"))
    root.get_right().set_left(BinaryTreeNode("Cousin"))
    root.get_right().set_right(BinaryTreeNode("Cousin"))
    btree = BinaryTree()
    btree._root = root
    #test tree structure
    assert btree._root.get_data() == "GrandFather"
    assert btree._root.get_left().get_data() == "Father"
    assert btree._root.get_left().get_left().get_data() == "Me"
    assert btree._root.get_left().get_right().get_data() == "Sibling"
    assert btree._root.get_left().get_left().get_left() is None
    assert btree._root.get_left().get_left().get_right() is None
    assert btree._root.get_left().get_right().get_left() is None
    assert btree._root.get_left().get_right().get_right() is None
    assert btree._root.get_right().get_data() == "Uncle"
    assert btree._root.get_right().get_left().get_data() == "Cousin"
    assert btree._root.get_right().get_right().get_data() == "Cousin"
    assert btree._root.get_right().get_left().get_left() is None
    assert btree._root.get_right().get_left().get_right() is None
    assert btree._root.get_right().get_right().get_left() is None
    assert btree._root.get_right().get_right().get_right() is None
    # test various functions
    assert not btree.is_empty()
    assert btree.get_depth() == 0
    assert btree.get_height() == 2
    assert btree.is_balanced()
    assert btree.is_perfect()
    assert btree.is_strict()
    assert len(btree) == 7
    assert btree.count_leaf_nodes() == 4
    assert [item for item in btree] == btree.to_list() == \
        ["GrandFather", "Father", "Uncle", "Me", "Sibling", "Cousin", "Cousin"]
    assert btree.preorder_traverse() == btree.depth_first_traverse() == \
        ["GrandFather", "Father", "Me", "Sibling", "Uncle", "Cousin", "Cousin"]
    assert btree.postorder_traverse() == \
        ["Me", "Sibling", "Father", "Cousin", "Cousin", "Uncle", "GrandFather"]
    assert btree.inorder_traverse() == \
        ["Me", "Father", "Sibling", "GrandFather", "Cousin", "Uncle", "Cousin"]
    assert btree.breadth_first_traverse() == \
        ["GrandFather", "Father", "Uncle", "Me", "Sibling", "Cousin", "Cousin"]
    with pytest.raises(ValueError): btree.traverse(get_string())
    with pytest.raises(TypeError): btree.traverse(get_list())
    with pytest.raises(TypeError): btree.traverse(get_int())
    with pytest.raises(TypeError): btree.traverse(get_float())
    # clear this binary tree
    btree.clear()
    test_empty_binary_tree(btree)


def test_binary_tree_with_numbers():
    btree = BinaryTree()
    btree._root = BinaryTreeNode(1)
    btree._root.set_left(BinaryTreeNode(2))
    btree._root.set_right(BinaryTreeNode(3))
    btree._root.get_right().set_left(BinaryTreeNode(6))
    btree._root.get_right().set_right(BinaryTreeNode(7))
    btree._root.get_left().set_left(BinaryTreeNode(4))
    btree._root.get_left().set_right(BinaryTreeNode(5))
    assert not btree.is_empty()
    assert len(btree) == 7
    assert btree.get_height() == 2
    assert btree._root.get_left().get_data() == 2
    assert btree._get_depth(btree._root.get_left()) == 1
    assert btree.to_list() == [1, 2, 3, 4, 5, 6, 7]
    assert btree.count_leaf_nodes() == 4
    assert btree.is_balanced()
    assert btree.is_perfect()
    assert btree.is_strict()
    assert btree.preorder_traverse() == [1, 2, 4, 5, 3, 6, 7]
    assert btree.postorder_traverse() == [4, 5, 2, 6, 7, 3, 1]
    assert btree.inorder_traverse() == [4, 2, 5, 1, 6, 3, 7]
    assert btree.breadth_first_traverse() == [1, 2, 3, 4, 5, 6, 7]
    assert btree.traverse() == [4, 2, 5, 1, 6, 3, 7]
    # clear this binary tree
    btree.clear()
    test_empty_binary_tree(btree)


def test_parse():
    lst = ["S", ["NP", ["DET", "There"]], ["S", ["VP", ["VERB", "is"],
        ["VP", ["NP", ["DET", "no"], ["NOUN", "asbestos"]],
        ["VP", ["PP", ["ADP","in"], ["NP", ["PRON", "our"]]],
        ["ADVP", ["ADV","now"]]]]]]]
    btree = BinaryTree.parse(lst)
    assert not btree.is_empty()
    assert len(btree) == 24
    assert btree.count_leaf_nodes() == 7
    assert not btree.is_balanced()
    assert not btree.is_perfect()
    assert not btree.is_strict()
    assert btree.get_depth() == 0
    assert btree.get_height() == 8
    # clear this binary tree
    btree.clear()
    test_empty_binary_tree(btree)

