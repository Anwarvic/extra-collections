import pytest
from extra.lists.linked_list import LinkedList

def test_empty_list():
    ll = LinkedList()
    assert ll.head == None