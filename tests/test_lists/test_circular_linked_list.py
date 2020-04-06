import random
import pytest

from tests import *
from extra.lists.linked_list import Node, LinkedList
from extra.lists.circular_linked_list import CircularLinkedList
from extra.lists.doubly_linked_list import DoublyNode, DoublyLinkedList


def test_creating_circular_linked_list_from_constructor():
    # Using constructor
    val = get_value()
    cll = CircularLinkedList(val)
    assert isinstance(cll.head, Node)
    assert cll.head.get_data() == val
    assert cll.head.get_next() == cll.head.next == cll.head
    assert len(cll) == cll.length == 1
    assert cll.to_list() == [item.get_data() for item in cll] == [val]
    # Using Node (should raise a Warning!)
    cll = CircularLinkedList( DoublyNode(get_value()) )
    # Using Node
    val = get_value()
    node = Node(val)
    node.set_next(Node(get_value()))
    cll = CircularLinkedList(node)
    assert isinstance(cll.head, Node)
    cll.head.get_data() == val
    cll.head.get_next() == cll.head.next == cll.head
    assert len(cll) == cll.length == 1
    assert cll.to_list() == [item.get_data() for item in cll] == [val]


def test_creating_circular_linked_list_from_iterable():
    # Using from_iterable (small length)
    lst = get_list()
    cll = CircularLinkedList.from_iterable(lst)
    assert cll.head.get_data() == lst[0]
    assert len(cll) == cll.length == len(lst)
    assert cll.to_list() == [item.get_data() for item in cll] == lst
    # Using from_iterable (has None)
    with pytest.raises(TypeError): CircularLinkedList.from_iterable([1, 2, None, 3])
    with pytest.raises(TypeError): CircularLinkedList().add_end(LinkedList(10))
    with pytest.raises(TypeError): CircularLinkedList().add_front(DoublyLinkedList(10))
    with pytest.raises(TypeError): CircularLinkedList().add_front(CircularLinkedList(10))
    # Using from_iterable (big length)
    lst = get_list(length = 10000)
    cll = CircularLinkedList.from_iterable(lst)
    assert cll.head.get_data() == lst[0]
    assert len(cll) == cll.length == len(lst)
    assert cll.to_list() == [item.get_data() for item in cll] == lst
    for _ in range(100): #check random indices
        idx = get_pos_int(b=10000-1)
        assert cll[idx].get_data() == lst[idx]
    # Using Linked List
    lst = get_list()
    tmp_cll = CircularLinkedList.from_iterable(lst)
    cll = CircularLinkedList.from_iterable(tmp_cll)
    # assert cll == tmp_cll
    assert len(cll) == cll.length == len(lst)
    assert cll.to_list() == [item.get_data() for item in cll] == lst


def test_empty_circular_linked_list():
    EMPTY = "┌─\n│\n└─" #represents empty LinkedList
    cll = CircularLinkedList.from_iterable([])
    assert isinstance(cll.head, Node)
    assert cll.head.get_data() == None
    assert cll.head.next == cll.head
    assert isinstance(cll.head.next, Node)
    assert str(cll) == EMPTY
    assert cll.length == len(cll) == 0
    assert cll.is_empty()
    assert cll.to_list() == []
    assert [_ for _ in cll ] == []
    assert len(cll.copy()) == 0
    assert len(cll.reverse()) == 0
    #################### test operators ####################
    assert CircularLinkedList() == CircularLinkedList(Node())
    assert cll == cll.copy()
    assert cll == cll.reverse()
    assert CircularLinkedList() != CircularLinkedList(get_value())
    assert CircularLinkedList() < CircularLinkedList(get_value())
    assert CircularLinkedList() <= CircularLinkedList(get_value())
    assert CircularLinkedList(get_value()) > CircularLinkedList()
    assert CircularLinkedList(get_value()) >= CircularLinkedList()
    #################### test count ####################
    assert cll.count(0) == 0
    assert cll.count(None) == 0
    assert cll.count(Node()) == 0
    assert cll.count(get_value()) == 0
    #################### test __contains__ ####################
    assert None in cll
    assert Node() in cll
    assert 0 not in cll
    assert get_value() not in cll
    assert Node(get_float()) not in cll
    # assert LinkedList(get_value()) not in ll
    #################### test split ####################
    left_list, right_list = cll.split(0)
    assert str(left_list) == str(right_list) == EMPTY
    with pytest.raises(TypeError): cll.split(get_string())
    with pytest.raises(TypeError): cll.split(get_float())
    with pytest.raises(TypeError): cll.split(True)
    with pytest.raises(IndexError): cll.split(-1)
    cll.split(get_pos_int()) #shouldn't raise anything
    with pytest.raises(IndexError): cll.split(get_neg_int())
    #################### test rotate ####################
    assert cll.rotate_left(get_pos_int(), inplace=False) == cll
    assert cll.rotate_right(get_pos_int(), inplace=False) == cll
    assert len(cll.rotate_left(get_pos_int(), inplace=False)) == 0
    assert len(cll.rotate_right(get_pos_int(), inplace=False)) == 0
    with pytest.raises(TypeError): cll.rotate_left(get_string())
    with pytest.raises(TypeError): cll.rotate_right(get_float())
    with pytest.raises(TypeError): cll.rotate_left([])
    with pytest.raises(ValueError): cll.rotate_left(get_neg_int())
    with pytest.raises(ValueError): cll.rotate_right(get_neg_int())
    #################### test remove/del ####################
    cll.remove_front() #shouldn't raise any Error
    cll.remove_end() #shouldn't raise any Error
    cll.remove(get_value())
    cll.remove(get_value(), False)
    with pytest.raises(TypeError): cll.remove(get_value(), all=get_string(1))
    del cll[0] #shouldn't raise anything
    del cll[get_pos_int()] #shouldn't raise anything
    with pytest.raises(IndexError): del cll[get_neg_int()]
    #################### test __getitem__ ####################
    with pytest.raises(IndexError): _ = cll[0]
    with pytest.raises(IndexError): _ = cll[get_pos_int()]
    with pytest.raises(IndexError): _ = cll[get_neg_int()]
    with pytest.raises(IndexError): CircularLinkedList() == cll[0:10]
    #################### test insert/set ####################
    cll.insert(get_pos_int(), get_value()) #shouldn't raise anything
    with pytest.raises(IndexError): cll.insert(get_neg_int(), get_value())
    cll[0] = get_float() #shouldn't raise anything
    cll[get_int()] = Node(get_float()) #shouldn't raise anything
    with pytest.raises(TypeError): cll.insert(0, None)
    with pytest.raises(TypeError): cll.insert(0, Node())


def test_circular_linked_list_with_one_element():
    val = get_value()
    cll = CircularLinkedList()
    cll.insert(0, val)
    assert isinstance(cll.head, Node)
    assert cll.head.get_data() == val
    assert cll.head.get_next() == cll.head
    assert len(cll) == 1
    assert not cll.is_empty()
    assert val in cll
    assert [item.get_data() for item in cll] == [val]
    assert cll.to_list() == [val]
    assert cll == cll.copy()
    assert cll == cll.reverse()
    #################### test rotate ####################
    assert cll == cll.rotate_left(get_pos_int(), inplace=False)
    assert cll == cll.rotate_right(get_pos_int(), inplace=False)
    #################### test operators ####################
    assert cll != CircularLinkedList()
    assert cll > CircularLinkedList()
    assert cll >= CircularLinkedList()
    assert CircularLinkedList() < cll
    assert CircularLinkedList() <= cll
    #################### test add/remove ####################
    new_value = get_value()
    cll.add_front(new_value)
    assert new_value == cll.remove_front().get_data()
    cll.add_end(new_value)
    assert new_value == cll.remove_end().get_data()
    assert cll == CircularLinkedList(val)
    #################### test insert/split ####################
    with pytest.raises(IndexError): cll.insert(-1, get_value())
    cll.insert(2, get_value()) #shouldn't raise anything
    cll.split(get_pos_int()) #shouldn't raise anything
