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
    assert 0 not in ll
    assert get_float() not in ll
    left_list, right_list = ll.split(0)
    assert str(left_list) == str(right_list) == EMPTY
    assert len(ll.rotate_left(get_pos_int())) == \
            len(ll.rotate_left(get_pos_int())) == 0
    assert len(ll.rotate_right(get_pos_int())) == \
            len(ll.rotate_right(get_pos_int())) == 0
    assert ll.count(0) == 0
    assert len(ll.copy()) == 0
    ll.remove_front() #shouldn't raise any Error
    ll.remove_end() #shouldn't raise any Error
    with pytest.raises(IndexError):
        _ = ll[0]
        _ = ll[get_pos_int()]
        _ = ll[get_neg_int()]
        _ == ll[0:10]
        ll.insert(get_pos_int(), get_pos_int())
        ll.insert(get_neg_int(), get_pos_int())
        del ll[0], ll[get_pos_int()], ll[get_neg_int()]
        ll.split(get_int())
        ll[0] = get_float()
        ll[get_int()] = Node(get_float())
    with pytest.raises(TypeError):
        ll.insert(0, None)
        ll.insert(0, Node())


def test_empty_list_given_empty_node():
    ll = LinkedList(Node())
    assert ll.head.get_data() == None
    assert ll.length == 0
