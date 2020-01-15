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
    assert [_ for _ in ll ] == []
    assert 0 not in ll
    assert ll.count(0)
    with pytest.raises(IndexError):
        _ = ll[0]
        ll.insert(1, 20)
        del ll[0]
        del ll[10]
    # these shouldn't raise any errors
    ll.split(0)
    ll.rotate_left(0)
    ll.rotate_right(0)
    



def test_empty_list_given_empty_node():
    ll = LinkedList(Node())
    assert ll.head.get_data() == None
    assert ll.length == 0
