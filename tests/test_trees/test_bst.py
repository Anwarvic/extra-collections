import pytest
from tests import *
from extra.trees.bst import BSTNode, BST




def test_bst_node():
    with pytest.raises(TypeError): BSTNode(None)
    with pytest.raises(TypeError): BSTNode('  ')
    with pytest.raises(TypeError): BSTNode(BST())
    with pytest.raises(TypeError): BSTNode(get_string())
    with pytest.raises(TypeError): BSTNode(get_list())
    # these shouldn't raise any erros
    for val in [get_int(), get_float()]:
        node = BSTNode(val)
        assert node.get_data() == val
        assert node.get_left() == node.get_right() == None
        assert node.get_children() == []


def test_empty_bst(bst=BST()):
    assert bst.is_empty()
    assert len(bst) == 0
    assert bst.is_empty()
    assert bst.get_height() == 0
    assert bst.to_list() == []
    assert bst.count_leaf_nodes() == 0
    with pytest.warns(UserWarning): bst.is_balanced()
    with pytest.warns(UserWarning): bst.is_perfect()
    with pytest.warns(UserWarning): bst.is_strict()
    assert bst.preorder_traverse() == []
    assert bst.postorder_traverse() == []
    assert bst.inorder_traverse() == []
    assert bst.breadth_first_traverse() == []
    assert bst.traverse() == []
    with pytest.raises(IndexError): bst.get_max()
    with pytest.raises(IndexError): bst.get_min()


def test_search_insert_remove_input(bst=BST()):
    assert None not in bst
    assert get_string() not in bst
    assert get_list() not in bst
    with pytest.raises(ValueError): bst.insert(None)
    with pytest.raises(TypeError): bst.insert(get_string())
    with pytest.raises(TypeError): bst.insert(get_list())
    
    bst.remove(None) #do nothing
    bst.remove(get_string()) #do nothing
    bst.remove(get_list()) #do nothing


def test_bst_one_value():
    bst = BST()
    val = get_int()
    bst.insert(val)
    # test structure
    assert verify_bst_rules(bst._root)
    assert bst._root.get_data() == val
    # test various methods
    assert bst.count_leaf_nodes() == 1
    assert bst.get_max() == val
    assert bst.get_min() == val
    assert bst.get_height() == 0
    assert bst.is_balanced()
    assert bst.is_perfect()
    assert bst.is_strict()
    # test __contains__
    assert val in bst
    assert 100 not in bst
    assert 1.1 not in bst
    # test __iter__ / traverse
    assert bst.to_list() == [val]
    assert bst.preorder_traverse() == [val]
    assert bst.depth_first_traverse() == [val]
    assert bst.postorder_traverse() == [val]
    assert bst.inorder_traverse() == [val]
    #test remove
    bst.remove(9) #do nothing
    bst.remove(val)
    # test empty bst
    test_empty_bst(bst)
    # validate
    test_search_insert_remove_input(bst)

    
    


def test_bst_simple():
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    # test structure
    assert verify_bst_rules(bst._root)
    assert bst._root.get_data() == 4
    assert bst._root.get_left().get_data() == 2
    assert bst._root.get_right().get_data() == 5
    assert bst._root.get_right().get_left() == None
    assert bst._root.get_right().get_right() == None
    assert bst._root.get_left().get_left().get_data() == 1
    assert bst._root.get_left().get_right().get_data() == 3
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
    assert verify_bst_rules(bst._root)
    # test empty bst
    bst.clear()
    test_empty_bst(bst)
    # validate
    test_search_insert_remove_input(bst)


def test_bst_from_iterable():
    lst = [19,7,10,12,22,30,11,25,9,20,14,12,30,22]
    bst = BST.from_iterable(lst)
    # test structure
    assert verify_bst_rules(bst._root)
    assert bst._root.get_data() == 19
    assert bst._root.get_left().get_data() == 7
    assert bst._root.get_right().get_data() == 22
    assert bst._root.get_left().get_left() == None
    assert bst._root.get_left().get_right().get_data() == 10
    # test various methods
    assert len(bst) == 11
    assert bst.count_leaf_nodes() == 5
    assert bst.get_max() == 30
    assert bst.get_min() == 7
    assert bst.get_height() == 4
    assert bst.is_balanced()
    assert not bst.is_perfect()
    assert not bst.is_strict()
    # test __contains__
    assert 11 in bst
    assert -10 not in bst
    assert 0 not in bst
    # test __iter__ / traverse
    assert bst.to_list() == [19, 7, 22, 10, 20, 30, 9, 12, 25, 11, 14]
    assert bst.preorder_traverse() == [19, 7, 10, 9, 12, 11, 14, 22, 20, 30, 25]
    assert bst.depth_first_traverse() == \
        [19, 7, 10, 9, 12, 11, 14, 22, 20, 30, 25]
    assert bst.postorder_traverse()== [9, 11, 14, 12, 10, 7, 20, 25, 30, 22, 19]
    assert bst.inorder_traverse() == [7, 9, 10, 11, 12, 14, 19, 20, 22, 25, 30]
    #test remove
    bst.remove(50) #do nothing
    bst.remove(22)
    assert len(bst) == 10
    assert 22 not in bst
    assert verify_bst_rules(bst._root)
    # test empty bst
    bst.clear()
    test_empty_bst(bst)
    # validate
    test_search_insert_remove_input(bst)



def test_bst_big_example():
    # SRC: "Data Structures and Algorithms in Python" book
    bst = BST()
    bst.insert(44)
    bst.insert(17)
    bst.insert(8)
    bst.insert(32)
    bst.insert(28)
    bst.insert(29)
    bst.insert(88)
    bst.insert(97)
    bst.insert(93)
    bst.insert(65)
    bst.insert(54)
    bst.insert(82)
    bst.insert(76)
    bst.insert(68)
    bst.insert(80)
    assert verify_bst_rules(bst._root)
    bst.remove(80)
    bst.remove(32)
    bst.remove(44)
    bst.remove(4000)
    bst.remove(65)
    assert verify_bst_rules(bst._root)
    assert bst._root.get_data() == 54
    assert len(bst) == 11
    assert bst.get_height() == 4
    assert bst.is_balanced()
    assert bst.traverse() == [8, 17, 28, 29, 54, 68, 76, 82, 88, 93, 97]
    assert bst.get_min() == 8
    assert bst.get_max() == 97
    # test empty bst
    bst.clear()
    test_empty_bst(bst)
    # validate
    test_search_insert_remove_input(bst)


