import pytest

from utils import *
from extra.lists.linked_list import Node, LinkedList





def test_empty_node():
    pass


def test_not_empty_node():
    pass


def test_creating_linked_list():
    pass


def test_empty_list():
    EMPTY = "┌─\n│\n└─" #represents empty LinkedList
    ll = LinkedList()
    assert isinstance(ll.head, Node)
    assert ll.head.get_data() == None
    assert ll.head.next == None
    assert not isinstance(ll.head.next, Node)
    assert str(ll) == EMPTY
    assert ll.length == len(ll) == 0
    assert ll.is_empty()
    assert ll.to_list() == []
    assert [_ for _ in ll ] == []
    assert len(ll.copy()) == 0
    assert len(ll.reverse()) == 0
    #################### test count ####################
    assert ll.count(0) == 0
    assert ll.count(None) == 0
    assert ll.count(Node()) == 0
    assert ll.count(get_value()) == 0
    #################### test __contains__ ####################
    assert None in ll
    assert Node() in ll
    assert 0 not in ll
    assert get_value() not in ll
    assert Node(get_float()) not in ll
    assert LinkedList(get_value()) not in ll
    #################### test split ####################
    left_list, right_list = ll.split(0)
    assert str(left_list) == str(right_list) == EMPTY
    with pytest.raises(TypeError):
        ll.split(get_string())
        ll.split(get_float())
        ll.split(True)
    with pytest.raises(IndexError):
        ll.split(-1)
        ll.split(get_int())
    #################### test rotate ####################
    assert len(ll.rotate_left(get_pos_int())) == \
            len(ll.rotate_left(get_pos_int())) == 0
    assert len(ll.rotate_right(get_pos_int())) == \
            len(ll.rotate_right(get_pos_int())) == 0
    with pytest.raises(TypeError):
        ll.rotate_left(get_string())
        ll.rotate_right(get_float())
        ll.rotate_left([])
    with pytest.raises(IndexError):
        ll.rotate_left(get_neg_int())
        ll.rotate_right(get_neg_int())
    #################### test remove/del ####################
    ll.remove_front() #shouldn't raise any Error
    ll.remove_end() #shouldn't raise any Error
    ll.remove(get_value())
    ll.remove(get_value(), False)
    with pytest.raises(TypeError):
        ll.remove(get_value(), all=get_string(1))
    with pytest.raises(IndexError):
        del ll[0], ll[get_pos_int()], ll[get_neg_int()]
    #################### test __getitem__ ####################
    with pytest.raises(IndexError):
        _ = ll[0]
        _ = ll[get_pos_int()]
        _ = ll[get_neg_int()]
        _ == ll[0:10]
    #################### test insert/set ####################
    with pytest.raises(IndexError):
        ll.insert(get_pos_int(), get_pos_int())
        ll.insert(get_neg_int(), get_pos_int())
        ll[0] = get_float()
        ll[get_int()] = Node(get_float())
    with pytest.raises(TypeError):
        ll.insert(0, None)
        ll.insert(0, Node())


def test_empty_list_given_empty_node():
    ll = LinkedList(Node())
    assert ll.head.get_data() == None
    assert ll.length == 0
