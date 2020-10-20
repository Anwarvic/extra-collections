import pytest
import random

from extra.trees.avl import AVLNode, AVL


def test_avl_node(helper):
    with pytest.raises(TypeError):
        AVLNode(None)
    with pytest.raises(TypeError):
        AVLNode("  ")
    with pytest.raises(TypeError):
        AVLNode(AVL())
    with pytest.raises(TypeError):
        AVLNode(helper.get_string())
    with pytest.raises(TypeError):
        AVLNode(helper.get_list())
    # these shouldn't raise any erros
    for val in [helper.get_int(), helper.get_float()]:
        node = AVLNode(val)
        assert node.get_data() == val
        assert node.get_left() == node.get_right() is None
        assert node.get_children() == []
        assert node._height == 0
        assert node.get_children_heights() == [0, 0]
        assert node.is_balanced()
        with pytest.raises(TypeError):
            node.set_height(helper.get_string())
        with pytest.raises(TypeError):
            node.set_height(helper.get_float())
        with pytest.raises(ValueError):
            node.set_height(helper.get_neg_int())


def test_empty_avl(avl=AVL()):
    assert avl.is_empty()
    assert len(avl) == 0
    assert avl.get_height() == 0
    assert avl.to_list() == []
    assert avl.count_leaf_nodes() == 0
    with pytest.warns(UserWarning):
        avl.is_balanced()
    with pytest.warns(UserWarning):
        avl.is_perfect()
    with pytest.warns(UserWarning):
        avl.is_strict()
    assert avl.preorder_traverse() == []
    assert avl.postorder_traverse() == []
    assert avl.inorder_traverse() == []
    assert avl.breadth_first_traverse() == []
    assert avl.traverse() == []
    with pytest.raises(IndexError):
        avl.get_max()
    with pytest.raises(IndexError):
        avl.get_min()


def test_avl_one_value(helper):
    avl = AVL()
    val = helper.get_int()
    avl.insert(val)
    # test structure
    assert helper.verify_bst_rules(avl._root)
    assert avl._root.get_data() == val
    # test various methods
    assert avl.count_leaf_nodes() == 1
    assert avl.get_max() == val
    assert avl.get_min() == val
    assert avl.get_height() == 0
    assert avl.is_balanced()
    assert avl.is_perfect()
    assert avl.is_strict()
    # test __contains__
    assert val in avl
    assert 100 not in avl
    assert 1.1 not in avl
    # test __iter__ / traverse
    assert avl.to_list() == [val]
    assert avl.preorder_traverse() == [val]
    assert avl.depth_first_traverse() == [val]
    assert avl.postorder_traverse() == [val]
    assert avl.inorder_traverse() == [val]
    # test remove
    with pytest.warns(UserWarning):
        avl.remove(9)
    avl.remove(val)
    # test empty avl
    test_empty_avl(avl)
    # validate
    test_search_insert_remove_input(helper, avl)


def test_simple_avl_tree(helper):
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

    helper.verify_bst_rules(avl._root)

    # test main methods
    assert not avl.is_empty()
    assert len(avl) == 9
    assert avl.get_height() == 3
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
    assert root.get_left().get_right().get_data() == 32
    assert root.get_left().get_right().get_height() == 0
    assert root.get_left().get_left() is None
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
    # clear
    avl.clear()
    test_empty_avl(avl)


def test_avl_big_example(helper):
    # src: https://www.youtube.com/watch?v=7m94k2Qhg68
    avl = AVL()
    avl.insert(43)
    avl.insert(18)
    avl.insert(22)
    avl.insert(9)
    avl.insert(21)
    avl.insert(6)
    avl.insert(8)
    avl.insert(20)
    avl.insert(63)
    avl.insert(50)
    avl.insert(62)
    avl.insert(51)

    helper.verify_bst_rules(avl._root)

    # test main methods
    assert not avl.is_empty()
    assert len(avl) == 12
    assert avl.get_height() == 3
    assert avl.count_leaf_nodes() == 6
    assert avl.is_balanced()
    assert not avl.is_perfect()
    assert not avl.is_strict()
    assert avl.to_list() == [22, 18, 50, 8, 21, 43, 62, 6, 9, 20, 51, 63]

    assert avl.preorder_traverse() == \
        [22, 18, 8, 6, 9, 21, 20, 50, 43, 62, 51, 63]
    assert avl.postorder_traverse() == \
        [6, 9, 8, 20, 21, 18, 43, 51, 63, 62, 50, 22]
    assert avl.inorder_traverse() == \
        [6, 8, 9, 18, 20, 21, 22, 43, 50, 51, 62, 63]
    assert avl.breadth_first_traverse() == \
        [22, 18, 50, 8, 21, 43, 62, 6, 9, 20, 51, 63]
    assert avl.traverse() == [6, 8, 9, 18, 20, 21, 22, 43, 50, 51, 62, 63]
    assert avl.get_max() == 63
    assert avl.get_min() == 6

    # test nodes-heights
    root = avl._root
    assert root.get_data() == 22
    assert root.get_height() == 3
    assert root.get_left().get_data() == 18
    assert root.get_left().get_height() == 2
    assert root.get_left().get_left().get_data() == 8
    assert root.get_left().get_left().get_height() == 1
    assert root.get_left().get_left().get_left().get_data() == 6
    assert root.get_left().get_left().get_left().get_height() == 0
    assert root.get_left().get_left().get_left().get_left() is None
    assert root.get_left().get_left().get_left().get_right() is None
    assert root.get_left().get_left().get_right().get_data() == 9
    assert root.get_left().get_left().get_right().get_height() == 0
    assert root.get_left().get_left().get_right().get_left() is None
    assert root.get_left().get_left().get_right().get_right() is None
    assert root.get_left().get_right().get_data() == 21
    assert root.get_left().get_right().get_height() == 1
    assert root.get_left().get_right().get_right() is None
    assert root.get_left().get_right().get_left().get_data() == 20
    assert root.get_left().get_right().get_left().get_height() == 0
    assert root.get_left().get_right().get_left().get_left() is None
    assert root.get_left().get_right().get_left().get_right() is None

    assert root.get_right().get_data() == 50
    assert root.get_right().get_height() == 2
    assert root.get_right().get_left().get_data() == 43
    assert root.get_right().get_left().get_height() == 0
    assert root.get_right().get_left().get_left() is None
    assert root.get_right().get_left().get_right() is None
    assert root.get_right().get_right().get_data() == 62
    assert root.get_right().get_right().get_height() == 1
    assert root.get_right().get_right().get_left().get_data() == 51
    assert root.get_right().get_right().get_left().get_height() == 0
    assert root.get_right().get_right().get_right().get_data() == 63
    assert root.get_right().get_right().get_right().get_height() == 0
    assert root.get_right().get_right().get_right().get_left() is None
    assert root.get_right().get_right().get_right().get_right() is None

    # clear
    avl.clear()
    test_empty_avl(avl)


def test_search_insert_remove_input(helper, avl=AVL()):
    assert None not in avl
    assert helper.get_string() not in avl
    assert helper.get_list() not in avl
    with pytest.raises(ValueError):
        avl.insert(None)
    with pytest.raises(TypeError):
        avl.insert(helper.get_string())
    with pytest.raises(TypeError):
        avl.insert(helper.get_list())

    with pytest.warns(UserWarning):
        avl.remove(None)
    with pytest.warns(UserWarning):
        avl.remove(helper.get_string())
    with pytest.warns(UserWarning):
        avl.remove(helper.get_list())


def test_left_rotation(helper):
    avl = AVL()
    avl.insert(0)
    avl.insert(5)
    avl.insert(10)

    helper.verify_bst_rules(avl._root)

    # test main methods
    assert not avl.is_empty()
    assert len(avl) == 3
    assert avl.get_height() == 1
    assert avl.count_leaf_nodes() == 2
    assert avl.is_balanced()
    assert avl.is_perfect()
    assert avl.is_strict()
    assert avl.to_list() == [5, 0, 10]

    assert avl.preorder_traverse() == [5, 0, 10]
    assert avl.postorder_traverse() == [0, 10, 5]
    assert avl.inorder_traverse() == [0, 5, 10]
    assert avl.breadth_first_traverse() == [5, 0, 10]
    assert avl.traverse() == [0, 5, 10]
    assert avl.get_max() == 10
    assert avl.get_min() == 0

    # test nodes-heights
    root = avl._root
    assert root.get_data() == 5
    assert root.get_height() == 1
    assert root.get_left().get_data() == 0
    assert root.get_left().get_height() == 0
    assert root.get_left().get_left() is None
    assert root.get_left().get_right() is None
    assert root.get_right().get_data() == 10
    assert root.get_right().get_height() == 0
    assert root.get_right().get_left() is None
    assert root.get_right().get_right() is None

    # clear
    avl.clear()
    test_empty_avl(avl)


def test_right_rotation(helper):
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(0)

    helper.verify_bst_rules(avl._root)

    # test main methods
    assert not avl.is_empty()
    assert len(avl) == 3
    assert avl.get_height() == 1
    assert avl.count_leaf_nodes() == 2
    assert avl.is_balanced()
    assert avl.is_perfect()
    assert avl.is_strict()
    assert avl.to_list() == [5, 0, 10]

    assert avl.preorder_traverse() == [5, 0, 10]
    assert avl.postorder_traverse() == [0, 10, 5]
    assert avl.inorder_traverse() == [0, 5, 10]
    assert avl.breadth_first_traverse() == [5, 0, 10]
    assert avl.traverse() == [0, 5, 10]
    assert avl.get_max() == 10
    assert avl.get_min() == 0

    # test nodes-heights
    root = avl._root
    assert root.get_data() == 5
    assert root.get_height() == 1
    assert root.get_left().get_data() == 0
    assert root.get_left().get_height() == 0
    assert root.get_left().get_left() is None
    assert root.get_left().get_right() is None
    assert root.get_right().get_data() == 10
    assert root.get_right().get_height() == 0
    assert root.get_right().get_left() is None
    assert root.get_right().get_right() is None

    # clear
    avl.clear()
    test_empty_avl(avl)


def test_left_right_rotation(helper):
    avl = AVL()
    avl.insert(10)
    avl.insert(5)
    avl.insert(7)

    helper.verify_bst_rules(avl._root)

    # test main methods
    assert not avl.is_empty()
    assert len(avl) == 3
    assert avl.get_height() == 1
    assert avl.count_leaf_nodes() == 2
    assert avl.is_balanced()
    assert avl.is_perfect()
    assert avl.is_strict()
    assert avl.to_list() == [7, 5, 10]

    assert avl.preorder_traverse() == [7, 5, 10]
    assert avl.postorder_traverse() == [5, 10, 7]
    assert avl.inorder_traverse() == [5, 7, 10]
    assert avl.breadth_first_traverse() == [7, 5, 10]
    assert avl.traverse() == [5, 7, 10]
    assert avl.get_max() == 10
    assert avl.get_min() == 5

    # test nodes-heights
    root = avl._root
    assert root.get_data() == 7
    assert root.get_height() == 1
    assert root.get_left().get_data() == 5
    assert root.get_left().get_height() == 0
    assert root.get_left().get_left() is None
    assert root.get_left().get_right() is None
    assert root.get_right().get_data() == 10
    assert root.get_right().get_height() == 0
    assert root.get_right().get_left() is None
    assert root.get_right().get_right() is None

    # clear
    avl.clear()
    test_empty_avl(avl)


def test_right_left_rotation(helper):
    avl = AVL()
    avl.insert(2)
    avl.insert(10)
    avl.insert(5)

    helper.verify_bst_rules(avl._root)

    # test main methods
    assert not avl.is_empty()
    assert len(avl) == 3
    assert avl.get_height() == 1
    assert avl.count_leaf_nodes() == 2
    assert avl.is_balanced()
    assert avl.is_perfect()
    assert avl.is_strict()
    assert avl.to_list() == [5, 2, 10]

    assert avl.preorder_traverse() == [5, 2, 10]
    assert avl.postorder_traverse() == [2, 10, 5]
    assert avl.inorder_traverse() == [2, 5, 10]
    assert avl.breadth_first_traverse() == [5, 2, 10]
    assert avl.traverse() == [2, 5, 10]
    assert avl.get_max() == 10
    assert avl.get_min() == 2

    # test nodes-heights
    root = avl._root
    assert root.get_data() == 5
    assert root.get_height() == 1
    assert root.get_left().get_data() == 2
    assert root.get_left().get_height() == 0
    assert root.get_left().get_left() is None
    assert root.get_left().get_right() is None
    assert root.get_right().get_data() == 10
    assert root.get_right().get_height() == 0
    assert root.get_right().get_left() is None
    assert root.get_right().get_right() is None

    # clear
    avl.clear()
    test_empty_avl(avl)


def test_remove_avl(helper):
    # src: Data Structures and Algorithms in Python Book (page: 508)
    avl = AVL([44, 62, 17, 32, 50, 78, 48, 54, 88])
    avl.remove(17)
    avl.remove(50)
    avl.remove(62)

    helper.verify_bst_rules(avl._root)

    # test main methods
    assert not avl.is_empty()
    assert len(avl) == 6
    assert avl.get_height() == 2
    assert avl.count_leaf_nodes() == 3
    assert avl.is_balanced()
    assert not avl.is_perfect()
    assert not avl.is_strict()
    assert avl.to_list() == [54, 44, 78, 32, 48, 88]

    assert avl.preorder_traverse() == [54, 44, 32, 48, 78, 88]
    assert avl.postorder_traverse() == [32, 48, 44, 88, 78, 54]
    assert avl.inorder_traverse() == [32, 44, 48, 54, 78, 88]
    assert avl.breadth_first_traverse() == [54, 44, 78, 32, 48, 88]
    assert avl.traverse() == [32, 44, 48, 54, 78, 88]
    assert avl.get_max() == 88
    assert avl.get_min() == 32

    # test nodes-heights
    root = avl._root
    assert root.get_data() == 54
    assert root.get_height() == 2
    assert root.get_left().get_data() == 44
    assert root.get_left().get_height() == 1
    assert root.get_left().get_left().get_data() == 32
    assert root.get_left().get_left().get_height() == 0
    assert root.get_left().get_left().get_left() is None
    assert root.get_left().get_left().get_right() is None
    assert root.get_left().get_right().get_data() == 48
    assert root.get_left().get_right().get_height() == 0
    assert root.get_left().get_right().get_left() is None
    assert root.get_left().get_right().get_right() is None

    assert root.get_right().get_data() == 78
    assert root.get_right().get_height() == 1
    assert root.get_right().get_left() is None
    assert root.get_right().get_right().get_data() == 88
    assert root.get_right().get_right().get_height() == 0
    assert root.get_right().get_right().get_left() is None
    assert root.get_right().get_right().get_right() is None

    # clear
    avl.clear()
    test_empty_avl(avl)


def test_random_avl(helper):
    length = 100
    avl = AVL()
    for _ in range(length):
        avl.insert(helper.get_int())
        assert avl.is_balanced()
    lst = avl.to_list()
    random.shuffle(lst)
    for num in lst:
        avl.remove(num)
        assert avl.is_balanced()
