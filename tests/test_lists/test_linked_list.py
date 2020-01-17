import pytest

from tests import *
from extra.lists.linked_list import Node, LinkedList




def test_empty_node():
    _node = Node()
    assert _node.get_data() == _node.data == None
    assert _node.get_next() == _node.next == None
    _node = Node(None)
    assert _node.get_data() == None
    assert _node.get_next() == None
    _node.set_next(None)
    with pytest.raises(AssertionError):
        _node.set_data(None)
        _node.set_next(Node())


def test_not_empty_node():
    # Given value: str
    s = get_string()
    _node = Node(s)
    assert _node.get_data() == _node.data == s
    assert _node.get_data() != s.upper()
    assert _node.get_next() == _node.next == None
    with pytest.raises(AssertionError):
        _node.set_data(None)
        _node.set_next(Node())
        _node.set_next(get_string())
        _node.set_next(get_value())
    # Given value: has __iter__ attribute
    lst = get_list()
    _node = Node(lst)
    assert _node.get_data() == lst
    assert _node.get_next() == None
    _node.set_next(Node(get_string()))
    # Given value: LinkedList()
    ll = LinkedList.from_iterable(get_list())
    _node = Node(ll)
    assert _node.get_data() == ll
    

def test_creating_linked_list():
    # Using constructor
    val = get_value()
    ll = LinkedList(val)
    ll.head.get_data() == val
    ll.head.get_next() == ll.head.next == None
    assert len(ll) == ll.length == 1
    assert ll.to_list() == [item.get_data() for item in ll] == [val]
    # Using from_iterable (small length)
    lst = get_list()
    ll = LinkedList.from_iterable(lst)
    ll.head.get_data() == lst[0]
    assert len(ll) == ll.length == len(lst)
    assert ll.to_list() == [item.get_data() for item in ll] == lst
    # Using from_iterable (big length)
    lst = get_list(length = 10000)
    ll = LinkedList.from_iterable(lst)
    ll.head.get_data() == lst[0]
    assert len(ll) == ll.length == len(lst)
    assert ll.to_list() == [item.get_data() for item in ll] == lst
    for _ in range(100): #check the indices
        idx = get_pos_int(b=10000)
        assert ll[idx].get_data() == lst[idx]


def test_empty_list():
    assert LinkedList() == LinkedList(Node())
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
    assert len(ll.rotate_left(get_pos_int())) == 0
    assert len(ll.rotate_right(get_pos_int())) == 0
    with pytest.raises(TypeError):
        ll.rotate_left(get_string())
        ll.rotate_right(get_float())
        ll.rotate_left([])
    with pytest.raises(ValueError):
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


def test_list_with_same_value():
    length = get_pos_int()
    val = get_value()
    ll = LinkedList()
    #test add_end
    for _ in range(length):
        ll.add_end(val)
    #test add_front
    for _ in range(length):
        ll.add_front(val)
    assert ll == ll.reverse()
    assert ll == ll.copy()
    assert not ll.is_empty()
    assert len(ll) == 2*length
    assert ll.count(val) == 2*length
    assert ll.to_list() == [val]*(2*length)
    # test split
    left_list, right_list = ll.split(length)
    assert len(left_list) == len(right_list) == length
    # test clear
    left_list.clear()
    right_list.clear()
    assert len(left_list) == len(right_list) == 0
    # test remove
    for i in range(length):
        if i > length//2:
            ll.remove_end()
        else:
            ll.remove_front()
    assert len(ll) == ll.count(val) == length
    ll.remove(val, all=True)
    assert ll.is_empty()
    assert len(ll) == 0


def test_random_insertions():
    pass