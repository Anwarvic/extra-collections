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
    with pytest.raises(AssertionError): _node.set_data(None)
    with pytest.raises(AssertionError): _node.set_next(Node())
    with pytest.raises(AssertionError): _node.set_prev(Node())
    with pytest.raises(AssertionError): _node.set_next(DoublyNode())
    with pytest.raises(AssertionError): _node.set_prev(DoublyNode())


def test_not_empty_doubly_node():
    # Given value: str
    s = get_string()
    _node = DoublyNode(s)
    assert _node.get_data() == _node.data == s
    assert _node.get_data() != s.upper()
    assert _node.get_next() == _node.next == None
    assert _node.get_prev() == _node.prev == None
    with pytest.raises(AssertionError): _node.set_data(None)
    with pytest.raises(AssertionError): _node.set_next(DoublyNode())
    with pytest.raises(AssertionError): _node.set_prev(DoublyNode())
    with pytest.raises(AssertionError): _node.set_next(get_string())
    with pytest.raises(AssertionError): _node.set_prev(get_string())
    with pytest.raises(AssertionError): _node.set_next(get_value())
    with pytest.raises(AssertionError): _node.set_prev(get_value())
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
    # Using Node (should shows a Warning!)
    with pytest.warns(UserWarning): DoublyLinkedList(Node())
    with pytest.warns(UserWarning): DoublyLinkedList(Node(get_value()))
    dl = DoublyLinkedList( DoublyNode(get_value()) )
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
    with pytest.raises(TypeError): DoublyLinkedList.from_iterable([1, 2, None, 3])
    with pytest.raises(TypeError): DoublyLinkedList().add_end(LinkedList(10))
    with pytest.raises(TypeError): DoublyLinkedList().add_front(DoublyLinkedList(10))
    # Using from_iterable (big length)
    lst = get_list(length = 10000)
    dl = DoublyLinkedList.from_iterable(lst)
    assert dl.head.get_data() == lst[0]
    assert dl.tail.get_data() == lst[-1]
    assert len(dl) == dl.length == len(lst)
    assert dl.to_list() == [item.get_data() for item in dl] == lst
    for _ in range(100): #check random indices
        idx = get_pos_int(b=10000-1)
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
    with pytest.warns(UserWarning): DoublyLinkedList(Node())
    # with pytest.raises(TypeError): DoublyLinkedList(LinkedList())
    with pytest.raises(TypeError): LinkedList() == DoublyLinkedList(DoublyNode())
    with pytest.raises(TypeError): LinkedList() != DoublyLinkedList(DoublyNode())
    with pytest.raises(TypeError): LinkedList() > DoublyLinkedList(DoublyNode())
    with pytest.raises(TypeError): LinkedList() >= DoublyLinkedList(DoublyNode())
    with pytest.raises(TypeError): LinkedList() < DoublyLinkedList(DoublyNode())
    with pytest.raises(TypeError): LinkedList() <= DoublyLinkedList(DoublyNode())
    assert DoublyLinkedList() == DoublyLinkedList(DoublyNode())
    assert dl == dl.copy()
    assert dl == dl.reverse()
    assert DoublyLinkedList() != DoublyLinkedList(get_value())
    assert DoublyLinkedList() < DoublyLinkedList(get_value())
    assert DoublyLinkedList() <= DoublyLinkedList(get_value())
    assert DoublyLinkedList(get_value()) > DoublyLinkedList()
    assert DoublyLinkedList(get_value()) >= DoublyLinkedList()
    #################### test count ####################
    assert dl.count(0) == 0
    assert dl.count(None) == 0
    assert dl.count(Node()) == 0
    assert dl.count(DoublyNode()) == 0
    assert dl.count(get_value()) == 0
    #################### test __contains__ ####################
    assert None in dl
    assert Node() not in dl
    assert DoublyNode() in dl
    assert 0 not in dl
    assert get_value() not in dl
    assert DoublyNode(get_float()) not in dl
    assert Node(get_value()) not in dl
    with pytest.raises(TypeError): assert LinkedList(get_value()) not in dl
    with pytest.raises(TypeError): assert DoublyLinkedList(get_value()) not in dl
    #################### test split ####################
    left_list, right_list = dl.split(0)
    assert str(left_list) == str(right_list) == EMPTY
    with pytest.raises(TypeError): dl.split(get_string())
    with pytest.raises(TypeError): dl.split(get_float())
    with pytest.raises(TypeError): dl.split(True)
    with pytest.raises(IndexError): dl.split(-1)
    with pytest.raises(IndexError): dl.split(get_int())
    #################### test rotate ####################
    assert dl.rotate_left(get_pos_int(), inplace=False) == dl
    assert dl.rotate_right(get_pos_int(), inplace=False) == dl
    assert len(dl.rotate_left(get_pos_int(), inplace=False)) == 0
    assert len(dl.rotate_right(get_pos_int(), inplace=False)) == 0
    with pytest.raises(TypeError): dl.rotate_left(get_string())
    with pytest.raises(TypeError): dl.rotate_right(get_float())
    with pytest.raises(TypeError): dl.rotate_left([])
    with pytest.raises(ValueError): dl.rotate_left(get_neg_int())
    with pytest.raises(ValueError): dl.rotate_right(get_neg_int())
    #################### test remove/del ####################
    dl.remove_front() #shouldn't raise any Error
    dl.remove_end() #shouldn't raise any Error
    dl.remove(get_value())
    dl.remove(get_value(), False)
    with pytest.raises(TypeError): dl.remove(get_value(), all=get_string())
    with pytest.raises(IndexError):
        del dl[0], dl[get_pos_int()], dl[get_neg_int()]
    #################### test __getitem__ ####################
    with pytest.raises(IndexError): _ = dl[0]
    with pytest.raises(IndexError): _ = dl[get_pos_int()]
    with pytest.raises(IndexError): _ = dl[get_neg_int()]
    with pytest.raises(IndexError): _ = dl[0:10]
    #################### test insert/set ####################
    with pytest.raises(IndexError): dl.insert(get_pos_int(), get_pos_int())
    with pytest.raises(IndexError): dl.insert(get_neg_int(), get_pos_int())
    with pytest.raises(IndexError): dl[0] = get_float()
    with pytest.raises(IndexError): dl[get_int()] = Node(get_float())
    with pytest.raises(TypeError): dl.insert(0, None)
    with pytest.raises(TypeError): dl.insert(0, Node())
    with pytest.raises(TypeError): dl.insert(0, Node(get_value()))
    with pytest.raises(TypeError): dl.insert(0, DoublyNode())


def test_list_with_one_element():
    val = get_value()
    dl = DoublyLinkedList()
    dl.insert(0, val)
    assert dl.head.get_data() == val
    assert dl.tail.get_data() == val
    assert dl.head.get_next() is None
    assert dl.head.get_prev() is None
    assert dl.tail.get_next() is None
    assert dl.tail.get_prev() is None
    assert len(dl) == 1
    assert not dl.is_empty()
    assert val in dl
    assert [item.get_data() for item in dl] == [val]
    assert dl.to_list() == [val]
    assert dl == dl.copy()
    assert dl == dl.reverse()
    #################### test rotate ####################
    assert dl == dl.rotate_left(get_pos_int(), inplace=False)
    assert dl == dl.rotate_right(get_pos_int(), inplace=False)
    #################### test operators ####################
    assert dl != DoublyLinkedList()
    assert dl > DoublyLinkedList()
    assert dl >= DoublyLinkedList()
    assert DoublyLinkedList() < dl
    assert DoublyLinkedList() <= dl
    with pytest.raises(TypeError): assert dl != LinkedList()
    with pytest.raises(TypeError): assert dl > LinkedList()
    with pytest.raises(TypeError): assert dl >= LinkedList()
    with pytest.raises(TypeError): assert LinkedList() < dl
    with pytest.raises(TypeError): assert LinkedList() <= dl
    #################### test add/remove ####################
    new_value = get_value()
    dl.add_front(new_value)
    dl.remove_front()
    dl.add_end(new_value)
    dl.remove_end()
    assert dl == DoublyLinkedList(val)
    #################### test insert/split ####################
    with pytest.raises(IndexError): dl.insert(2, get_value())
    with pytest.raises(IndexError): dl.insert(-1, get_value())
    with pytest.raises(IndexError): dl.split(get_pos_int(a=2))


def test_list_with_same_value():
    length = get_pos_int()
    val = get_value()
    dl = DoublyLinkedList()
    #test add_end
    for _ in range(length):
        dl.add_end(val)
    #test add_front
    for _ in range(length):
        dl.add_front(val)
    assert dl == dl.reverse()
    assert dl == dl.copy()
    assert not dl.is_empty()
    assert len(dl) == 2*length
    assert dl.count(val) == 2*length
    assert dl.to_list() == [val]*(2*length)
    # test split
    left_list, right_list = dl.split(length)
    assert len(left_list) == len(right_list) == length
    # test clear
    left_list.clear()
    right_list.clear()
    assert len(left_list) == len(right_list) == 0
    # test remove
    for i in range(length):
        if i > length//2:
            dl.remove_end()
        else:
            dl.remove_front()
    assert len(dl) == dl.count(val) == length
    dl.remove(val, all=True)
    assert dl.is_empty()
    assert len(dl) == 0


def test_list_with_known_values():
    dl = DoublyLinkedList()
    dl.add_front(10)
    dl.add_front(5)
    assert dl.to_list() == [5, 10]
    dl.remove(20)
    dl.remove_front()
    assert dl == DoublyLinkedList(10)
    dl.remove_end()
    assert dl == DoublyLinkedList() 
    dl.insert(0, 100)
    dl.insert(1, 200)
    dl.insert(1, 100)
    assert 100 in dl and 200 in dl
    assert dl == DoublyLinkedList.from_iterable([100, 100, 200])
    assert dl.copy().to_list() == [100, 100, 200]
    assert dl.reverse() == DoublyLinkedList.from_iterable([200, 100, 100])
    dl.remove(100)
    rev = dl.reverse()
    assert dl == rev == DoublyLinkedList(200)
    dl.clear()
    assert not rev.is_empty()
    assert dl.is_empty()
    ###################################################
    dl = DoublyLinkedList()
    dl.add_front(6)
    dl.add_end(20)
    dl.insert(1, 10)
    dl.insert(2, 77)
    dl.insert(4, 43)
    dl.insert(0, 2)
    assert 43 in dl
    assert dl[1:4].to_list() == [6, 10, 77]
    assert dl.copy().to_list() == [2, 6, 10, 77, 20, 43]
    del dl[len(dl)-1]
    assert dl.reverse().to_list() == [20, 77, 10, 6, 2]
    assert dl.length == len(dl) == 5
    dl.clear()
    assert dl.is_empty()


def test_list_with_random_numbers():
    # test add_end() and remove_end()
    lst = get_list(length=100)
    dl = DoublyLinkedList()
    for i in lst:
        dl.add_end(i)
    assert len(dl) == len(lst)
    assert dl.head.get_data() == lst[0]
    assert not dl.is_empty()
    for _ in range(len(lst)):
        assert dl[0].get_data() == lst[0]
        assert dl.remove_end().get_data() == lst.pop()
    assert len(dl) == 0
    assert dl.is_empty()
    # test add_front() and remove_front()
    lst = get_list(length=100)
    for i in lst:
        dl.add_front(i)
    assert len(dl) == len(lst)
    assert dl.head.get_data() == lst[-1]
    assert not dl.is_empty()
    for _ in range(len(lst)):
        assert dl[0].get_data() == lst[-1]
        assert dl.remove_front().get_data() == lst.pop()
    assert len(dl) == 0
    assert dl.is_empty()


def test_relational_operators():
    # linked lists have just one value
    assert DoublyLinkedList(3.14) == DoublyLinkedList(3.14)
    assert DoublyLinkedList(get_int()) != DoublyLinkedList(get_float())
    assert DoublyLinkedList(get_string()) != DoublyLinkedList(get_int())
    assert DoublyLinkedList(get_float()) != DoublyLinkedList(get_list())
    assert DoublyLinkedList(2.9999) < DoublyLinkedList(3)
    assert DoublyLinkedList(3.14) <= DoublyLinkedList(3.14)
    assert DoublyLinkedList([1, 2]) > DoublyLinkedList([3])
    assert DoublyLinkedList('3.14') >= DoublyLinkedList('3.14')
    with pytest.raises(TypeError):
        assert DoublyLinkedList(get_float()) < DoublyLinkedList(get_string())
    with pytest.raises(TypeError):
        assert DoublyLinkedList(get_value()) <= DoublyLinkedList(get_list())
    with pytest.raises(TypeError):
        assert DoublyLinkedList(get_string()) > DoublyLinkedList(get_list())
    with pytest.raises(TypeError):
        assert DoublyLinkedList(get_list()) >= DoublyLinkedList(get_float())
    # linked lists have more than one value
    dllist1 = DoublyLinkedList.from_iterable([1, '2', 3.14])
    dllist2 = DoublyLinkedList.from_iterable([1, '2', 5.14])
    assert dllist1 == dllist1
    assert dllist1 != dllist2
    assert dllist1 < dllist2
    assert dllist1 <= dllist2
    assert dllist2 > dllist2
    assert dllist2 >= dllist2
    # slicing lists
    assert dllist1[:-1] == dllist2[:-1]
    assert dllist1[-1:] != dllist2[-1:]
    assert dllist1[:1] < dllist2
    assert dllist1[:2] <= dllist2
    with pytest.raises(TypeError): assert dllist1[1:] < dllist2
    with pytest.raises(TypeError): assert dllist1[1:] <= dllist2
    # if the other one isn't a doubly linked list
    actual_list = [1, '2', 5.14]
    with pytest.raises(TypeError): assert dllist1 == actual_list
    with pytest.raises(TypeError): assert dllist1 != actual_list
    with pytest.raises(TypeError): assert dllist1 < actual_list
    with pytest.raises(TypeError): assert dllist1 <= actual_list
    with pytest.raises(TypeError): assert dllist2 > actual_list
    with pytest.raises(TypeError): assert dllist2 >= actual_list
    # if the other one is a linked list
    llist = LinkedList.from_iterable([1, '2', 5.14])
    with pytest.raises(TypeError): assert dllist1 == llist
    with pytest.raises(TypeError): assert dllist1 != llist
    with pytest.raises(TypeError): assert dllist1 < llist
    with pytest.raises(TypeError): assert dllist1 <= llist
    with pytest.raises(TypeError): assert dllist2 > llist
    with pytest.raises(TypeError): assert dllist2 >= llist
    

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
    assert rotated.head.get_data() == 4
    assert rotated.head.get_prev() is None
    assert rotated.tail.get_data() == 3
    assert rotated.tail.get_next() is None
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
    assert dl[-1].get_data() == 2


def test_join_method():
    lst = get_list()
    # two Doubly linked lists are empty
    dllist1 = DoublyLinkedList(None)
    dllist1.join(DoublyLinkedList())
    assert dllist1 == DoublyLinkedList()
    # one linked list is empty
    dllist1 = DoublyLinkedList.from_iterable([])
    dllist2 = DoublyLinkedList.from_iterable(lst)
    dllist1.join(dllist2)
    assert dllist1 == dllist2
    assert len(dllist1) == len(lst)
    dllist2.join(dllist1)
    assert len(dllist2) == 2*len(lst)
    # two linked lists are NOT empty
    dllist1 = DoublyLinkedList.from_iterable(lst)
    dllist2 = DoublyLinkedList.from_iterable(lst)
    dllist2.join(dllist1)
    assert dllist1.to_list() == lst
    assert dllist2.to_list() == lst+lst
    assert len(dllist2) == 2*len(lst)
    # join other data type
    with pytest.raises(TypeError): DoublyLinkedList().join(LinkedList())
    with pytest.raises(TypeError): DoublyLinkedList().join(get_list())
    with pytest.raises(TypeError): DoublyLinkedList().join(get_value())


def test_split():
    lst = get_list(length=100)
    dl = DoublyLinkedList.from_iterable(lst)
    for i in range(len(lst)):
        # test left list
        left_list, right_list = dl.split(i)
        assert isinstance(left_list, DoublyLinkedList)
        assert isinstance(left_list.head, DoublyNode)
        assert isinstance(left_list.tail, DoublyNode)
        assert left_list.to_list() == lst[:i]
        assert left_list.copy().to_list() == lst[:i]
        assert left_list.reverse().to_list() == lst[:i][::-1]
        # test right list
        assert isinstance(right_list, DoublyLinkedList)
        assert isinstance(right_list.head, DoublyNode)
        assert isinstance(right_list.tail, DoublyNode)
        assert right_list.to_list() == lst[i:]
        assert right_list.copy().to_list() == lst[i:]
        assert right_list.reverse().to_list() == lst[i:][::-1]
    dl.add_front(0)
    dl.add_end('apple')
    assert dl.length == len(dl) == len(lst)+2
    assert dl.to_list() == [0]+lst+['apple']

