import pytest
from extra.lists.linked_list import LinkedList as LinkedList

def test_empty_list():
    ll = LinkedList()
    assert ll.head.get_data() == None