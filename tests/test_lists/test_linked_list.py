import pytest
from extra.lists.linked_list import Node, LinkedList



def test_empty_node():
    pass


def test_not_empty_node():
    pass


def test_empty_list():
    ll = LinkedList()
    assert isinstance(ll.head, Node)
    assert ll.head.get_data() == None
    assert ll.head.next == None
    assert not isinstance(ll.head.next, Node)
    assert ll.length == 0
    assert str(ll) == "┌─\n│\n└─"
    assert ll.is_empty()
    assert ll.to_list() == []



def test_empty_list_given_empty_node():
    ll = LinkedList(Node())
    assert ll.head.get_data() == None
    assert ll.length == 0
