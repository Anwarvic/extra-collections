import random
import pytest

from tests import *
from extra.lists.linked_list import Node, LinkedList
from extra.lists.circular_linked_list import CircularLinkedList


def test_creating_linked_list_from_constructor():
    # Using constructor
    val = get_value()
    cll = CircularLinkedList(val)
    assert isinstance(cll.head, Node)
    assert cll.head.get_data() == val
    assert cll.head.get_next() == cll.head.next == cll.head
    assert len(cll) == cll.length == 1
    assert cll.to_list() == [item.get_data() for item in cll] == [val]
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