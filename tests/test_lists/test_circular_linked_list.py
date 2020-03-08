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
    with pytest.raises(TypeError):
        CircularLinkedList.from_iterable([1, 2, None, 3])
        CircularLinkedList().add_end(LinkedList(10))
        CircularLinkedList().add_front(DoublyLinkedList(10))
        CircularLinkedList().add_front(CircularLinkedList(10))
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