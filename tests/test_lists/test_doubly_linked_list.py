import pytest

from tests import *
from extra.lists.linked_list import Node, LinkedList
from extra.lists.doubly_linked_list import DoublyNode, DoublyLinkedList




def test_empty_doubly_node():
    _node = DoublyNode()
    assert _node.get_data() == _node.data == None
    assert _node.get_next() == _node.next == None
    assert _node.get_prev() == _node.prev == None
    _node = DoublyNode(None)
    assert _node.get_data() == None
    assert _node.get_next() == None
    assert _node.get_prev() == None
    _node.set_next(None)
    _node.set_prev(None)
    with pytest.raises(AssertionError):
        _node.set_data(None)
        _node.set_next(Node())
        _node.set_prev(Node())
        _node.set_next(DoublyNode())
        _node.set_prev(DoublyNode())


def test_not_empty_doubly_node():
    # Given value: str
    s = get_string()
    _node = DoublyNode(s)
    assert _node.get_data() == _node.data == s
    assert _node.get_data() != s.upper()
    assert _node.get_next() == _node.next == None
    assert _node.get_prev() == _node.prev == None
    with pytest.raises(AssertionError):
        _node.set_data(None)
        _node.set_next(DoublyNode())
        _node.set_prev(DoublyNode())
        _node.set_next(get_string())
        _node.set_prev(get_string())
        _node.set_next(get_value())
        _node.set_prev(get_value())
    # Given value: has __iter__ attribute
    lst = get_list()
    _node = DoublyNode(lst)
    assert _node.get_data() == lst
    assert _node.get_next() is None
    assert _node.get_prev() is None
    _node.set_next(DoublyNode(get_string()))
    _node.set_prev(DoublyNode(get_string()))
    # Given value: LinkedList()
    dl = LinkedList.from_iterable(get_list())
    _node = DoublyNode(dl)
    assert _node.get_data() == dl
    assert _node.get_next() is None
    assert _node.get_prev() is None
    # Given value: LinkedList()
    dl = DoublyLinkedList.from_iterable(get_list())
    _node = DoublyNode(dl)
    assert _node.get_data() == dl
    assert _node.get_next() is None
    assert _node.get_prev() is None
    

def test_creating_doubly_linked_list_from_constructor():
    # Using constructor
    val = get_value()
    dl = DoublyLinkedList(val)
    dl.head.get_data() == dl.tail.get_data() == val
    dl.head.get_next() == dl.head.next is None
    dl.head.get_prev() == dl.head.prev is None
    dl.tail.get_next() == dl.head.next is None
    dl.tail.get_prev() == dl.head.prev is None
    assert len(dl) == dl.length == 1
    assert dl.to_list() == [item.get_data() for item in dl] == [val]
    # Using Node
    dl = DoublyLinkedList( Node(get_value()) )
    # Using DoublyNode
    val = get_value()
    node = DoublyNode(val)
    node.set_next(DoublyNode(get_value()))
    node.set_prev(DoublyNode(get_value()))
    dl = DoublyLinkedList(node)
    dl.head.get_data() == val
    dl.head.get_next() == dl.head.next is None
    dl.head.get_prev() == dl.head.prev is None
    assert len(dl) == dl.length == 1
    assert dl.to_list() == [item.get_data() for item in dl] == [val]


def test_creating_doubly_linked_list_from_iterable():
    # Using from_iterable (small length)
    lst = get_list()
    dl = DoublyLinkedList.from_iterable(lst)
    assert dl.head.get_data() == lst[0]
    assert dl.tail.get_data() == lst[-1]
    assert len(dl) == dl.length == len(lst)
    assert dl.to_list() == [item.get_data() for item in dl] == lst
    # Using from_iterable (has None)
    with pytest.raises(TypeError):
        DoublyLinkedList.from_iterable([1, 2, None, 3])
        DoublyLinkedList().add_end(LinkedList(10))
        DoublyLinkedList().add_front(DoublyLinkedList(10))
    # Using from_iterable (big length)
    lst = get_list(length = 10000)
    dl = DoublyLinkedList.from_iterable(lst)
    assert dl.head.get_data() == lst[0]
    assert dl.tail.get_data() == lst[-1]
    assert len(dl) == dl.length == len(lst)
    assert dl.to_list() == [item.get_data() for item in dl] == lst
    for _ in range(100): #check random indices
        idx = get_pos_int(b=10000)
        assert dl[idx].get_data() == lst[idx]
    # Using Linked List
    lst = get_list()
    tmp_dl = DoublyLinkedList.from_iterable(lst)
    dl = DoublyLinkedList.from_iterable(tmp_dl)
    assert dl == tmp_dl
    assert len(dl) == dl.length == len(lst)
    assert dl.to_list() == [item.get_data() for item in dl] == lst


def test_empty_doubly_linked_list():
    EMPTY = "┌─\n│\n└─" #represents empty Doubly LinkedList
    dl = DoublyLinkedList()
    assert isinstance(dl.head, DoublyNode)
    assert dl.head.get_data() == dl.tail.get_data() is None
    assert dl.head.next == dl.head.prev == None
    assert not isinstance(dl.head.next, DoublyNode)
    assert not isinstance(dl.head.prev, DoublyNode)
    assert not isinstance(dl.tail.prev, DoublyNode)
    assert not isinstance(dl.tail.prev, DoublyNode)
    assert str(dl) == EMPTY
    assert dl.length == len(dl) == 0
    assert dl.is_empty()
    assert dl.to_list() == []
    assert [_ for _ in dl ] == []
    assert len(dl.copy()) == 0
    assert len(dl.reverse()) == 0
    #################### test operators ####################
    assert LinkedList() == DoublyLinkedList(DoublyNode())
    assert dl == dl.copy()
    assert dl == dl.reverse()
    assert LinkedList() != LinkedList(get_value())
    assert LinkedList() < LinkedList(get_value())
    assert LinkedList() <= LinkedList(get_value())
    assert LinkedList(get_value()) > LinkedList()
    assert LinkedList(get_value()) >= LinkedList()
    #################### test count ####################
    assert dl.count(0) == 0
    assert dl.count(None) == 0
    assert dl.count(Node()) == 0
    assert dl.count(DoublyNode()) == 0
    assert dl.count(get_value()) == 0
    #################### test __contains__ ####################
    assert None in dl
    assert Node() in dl
    assert DoublyNode() in dl
    assert 0 not in dl
    assert get_value() not in dl
    assert Node(get_float()) not in dl
    assert DoublyNode(get_float()) not in dl
    # assert LinkedList(get_value()) not in dl
    # assert DoublyLinkedList(get_value()) not in dl
    #################### test split ####################
    left_list, right_list = dl.split(0)
    assert str(left_list) == str(right_list) == EMPTY
    with pytest.raises(TypeError):
        dl.split(get_string())
        dl.split(get_float())
        dl.split(True)
    with pytest.raises(IndexError):
        dl.split(-1)
        dl.split(get_int())
    #################### test rotate ####################
    assert dl.rotate_left(get_pos_int(), inplace=False) == dl
    assert dl.rotate_right(get_pos_int(), inplace=False) == dl
    assert len(dl.rotate_left(get_pos_int(), inplace=False)) == 0
    assert len(dl.rotate_right(get_pos_int(), inplace=False)) == 0
    with pytest.raises(TypeError):
        dl.rotate_left(get_string())
        dl.rotate_right(get_float())
        dl.rotate_left([])
    with pytest.raises(ValueError):
        dl.rotate_left(get_neg_int())
        dl.rotate_right(get_neg_int())
    #################### test remove/del ####################
    dl.remove_front() #shouldn't raise any Error
    dl.remove_end() #shouldn't raise any Error
    dl.remove(get_value())
    dl.remove(get_value(), False)
    with pytest.raises(TypeError):
        dl.remove(get_value(), all=get_string())
    with pytest.raises(IndexError):
        del dl[0], dl[get_pos_int()], dl[get_neg_int()]
    #################### test __getitem__ ####################
    with pytest.raises(IndexError):
        _ = dl[0]
        _ = dl[get_pos_int()]
        _ = dl[get_neg_int()]
        _ == dl[0:10]
    #################### test insert/set ####################
    with pytest.raises(IndexError):
        dl.insert(get_pos_int(), get_pos_int())
        dl.insert(get_neg_int(), get_pos_int())
        dl[0] = get_float()
        dl[get_int()] = Node(get_float())
    with pytest.raises(TypeError):
        dl.insert(0, None)
        dl.insert(0, Node())
        dl.insert(0, DoublyNode())


# def test_list_with_same_value():
#     length = get_pos_int()
#     val = get_value()
#     dl = LinkedList()
#     #test add_end
#     for _ in range(length):
#         dl.add_end(val)
#     #test add_front
#     for _ in range(length):
#         dl.add_front(val)
#     assert dl == dl.reverse()
#     assert dl == dl.copy()
#     assert not dl.is_empty()
#     assert len(dl) == 2*length
#     assert dl.count(val) == 2*length
#     assert dl.to_list() == [val]*(2*length)
#     # test split
#     left_list, right_list = dl.split(length)
#     assert len(left_list) == len(right_list) == length
#     # test clear
#     left_list.clear()
#     right_list.clear()
#     assert len(left_list) == len(right_list) == 0
#     # test remove
#     for i in range(length):
#         if i > length//2:
#             dl.remove_end()
#         else:
#             dl.remove_front()
#     assert len(dl) == dl.count(val) == length
#     dl.remove(val, adl=True)
#     assert dl.is_empty()
#     assert len(dl) == 0


# def test_list_with_one_element():
#     val = get_value()
#     dl = LinkedList()
#     dl.insert(0, val)
#     assert dl.head.get_data() == val
#     assert dl.head.get_next() == None
#     assert len(dl) == 1
#     assert not dl.is_empty()
#     assert val in dl
#     assert [item.get_data() for item in dl] == [val]
#     assert dl.to_list() == [val]
#     assert dl == dl.copy()
#     assert dl == dl.reverse()
#     #################### test rotate ####################
#     assert dl == dl.rotate_left(get_pos_int(), inplace=False)
#     assert dl == dl.rotate_right(get_pos_int(), inplace=False)
#     #################### test operators ####################
#     assert dl != LinkedList()
#     assert dl > LinkedList()
#     assert dl >= LinkedList()
#     assert LinkedList() < dl
#     assert LinkedList() <= dl
#     #################### test add/remove ####################
#     new_value = get_value()
#     dl.add_front(new_value)
#     dl.remove_front()
#     dl.add_end(new_value)
#     dl.remove_end()
#     assert dl == LinkedList(val)
#     #################### test insert/split ####################
#     with pytest.raises(IndexError):
#         dl.insert(2, get_value())
#         dl.insert(-1, get_value())
#         dl.split(get_pos_int(a=2))


# def test_list_with_values():
#     dl = LinkedList()
#     dl.add_front(10)
#     dl.add_front(5)
#     assert dl.to_list() == [5, 10]
#     dl.remove(20)
#     dl.remove_front()
#     assert dl == LinkedList(10)
#     dl.remove_end()
#     assert dl == LinkedList() 
#     dl.insert(0, 100)
#     dl.insert(1, 200)
#     dl.insert(1, 100)
#     assert 100 in dl and 200 in dl
#     assert dl == LinkedList.from_iterable([100, 100, 200])
#     assert dl.copy().to_list() == [100, 100, 200]
#     assert dl.reverse() == LinkedList.from_iterable([200, 100, 100])
#     dl.remove(100)
#     rev = dl.reverse()
#     assert dl == rev == LinkedList(200)
#     dl.clear()
#     assert not rev.is_empty()
#     assert dl.is_empty()
#     ###################################################
#     dl = LinkedList()
#     dl.add_front(6)
#     dl.add_end(20)
#     dl.insert(1, 10)
#     dl.insert(2, 77)
#     dl.insert(4, 43)
#     dl.insert(0, 2)
#     assert 43 in dl
#     assert dl[1:4].to_list() == [6, 10, 77]
#     assert dl.copy().to_list() == [2, 6, 10, 77, 20, 43]
#     del dl[len(dl)-1]
#     assert dl.reverse().to_list() == [20, 77, 10, 6, 2]
#     assert dl.length == len(dl) == 5
#     dl.clear()
#     assert dl.is_empty()


# def test_relational_operators():
#     dlist1 = LinkedList.from_iterable([1, '2', 3.14])
#     dlist2 = LinkedList.from_iterable([1, '2', 5.14])
#     assert dlist1 == dlist1
#     assert dlist1 != dlist2
#     assert dlist1 < dlist2
#     assert dlist1 <= dlist2
#     assert dlist2 > dlist2
#     assert dlist2 >= dlist2
#     # slicing lists
#     assert dlist1[:-1] == dlist2[:-1]
#     assert dlist1[-1:] != dlist2[-1:]
    


def test_rotate():
    # rotate when inplace = False
    dl = DoublyLinkedList.from_iterable([1, 2, 3, 4, 5, 6])
    rotated = dl.rotate_right(1, inplace=False)
    assert isinstance(rotated.head, DoublyNode)
    assert isinstance(rotated.tail, DoublyNode)
    assert rotated.to_list() == [6, 1, 2, 3, 4 ,5]
    assert rotated.head.get_data() == 6
    assert rotated.head.get_prev() is None
    assert rotated.tail.get_data() == 5
    assert rotated.tail.get_next() is None
    assert rotated[4].get_data() == 4
    rotated = dl.rotate_left(3, inplace=False)
    assert isinstance(rotated.head, DoublyNode)
    assert isinstance(rotated.tail, DoublyNode)
    assert rotated.to_list() == [4 ,5, 6, 1, 2, 3]
    assert rotated.head.get_data() == 3
    assert rotated.head.get_prev() is None
    assert rotated.tail.get_data() == 3
    assert rotated.head.get_next() is None
    assert rotated[-2].get_data() == 2
    assert dl.to_list() == [1, 2, 3, 4, 5, 6]
    # rotate when inplace = True
    dl.rotate_right(1)
    assert isinstance(dl.head, DoublyNode)
    assert isinstance(dl.tail, DoublyNode)
    assert dl.to_list() == [6, 1, 2, 3, 4 ,5]
    assert dl.head.get_data() == 6
    assert dl.head.get_prev() is None
    assert dl.tail.get_data() == 5
    assert dl.tail.get_next() is None
    assert dl[4].get_data() == 4
    dl.rotate_left(3)
    assert isinstance(rotated.head, DoublyNode)
    assert isinstance(rotated.tail, DoublyNode)
    assert dl.to_list() == [3, 4 ,5, 6, 1, 2]
    assert dl.head.get_data() == 3
    assert dl.head.get_prev() is None
    assert dl.tail.get_data() == 2
    assert dl.tail.get_next() is None
    assert dl[-1].get_data() == 5


def test_split():
    dl = DoublyLinkedList.from_iterable([1, 2, 3, 4, 5, 6])
    left_list, right_list = dl.split(5)
    assert isinstance(left_list, DoublyLinkedList)
    assert isinstance(right_list, DoublyLinkedList)
    assert left_list.to_list() == [1, 2, 3, 4, 5]
    assert left_list.head.get_data() == 1
    assert right_list.head.get_prev() is None
    assert right_list.tail.get_data() == 5
    assert right_list.tail.get_next() is None

    assert right_list.reverse() == LinkedList(6)
    assert left_list.head.get_data() == right_list.tail.get_data()
    assert right_list.head.get_next() == right_list.head.get_prev() is None
    assert right_list.tail.get_next() == right_list.tail.get_prev() is None

    dl.add_front(0)
    assert dl.length == len(dl) == 7
    assert dl.to_list == list(range(7))

