import random
import pytest

from tests import *
from extra.lists.linked_list import Node, LinkedList




def test_not_empty_node():
    # Given value: str
    s = get_string()
    node = Node(s)
    assert node.get_data() == node._data == s
    assert node.get_data() != s.upper()
    assert node.get_next() == node._next == None
    with pytest.raises(ValueError): node.set_data(None)
    with pytest.raises(TypeError): node.set_next(get_string())
    with pytest.raises(TypeError): node.set_next(get_value())
    # Given value: has __iter__ attribute
    lst = get_list()
    node = Node(lst)
    assert node.get_data() == lst
    assert node.get_next() == None
    node.set_next(Node(get_string()))
    # Given value: LinkedList()
    ll = LinkedList.from_iterable(get_list())
    with pytest.raises(TypeError): Node(ll)
    

def test_creating_linked_list_from_constructor():
    # Using constructor
    val = get_value()
    ll = LinkedList()
    ll.add_front(val)
    assert isinstance(ll._head, Node)
    assert ll._head.get_data() == val
    assert ll._head.get_next() == ll._head._next == None
    assert len(ll) == ll._length == 1
    assert ll.to_list() == [item for item in ll] == [val]
    # Using Node
    val = get_value()
    ll = LinkedList()
    ll.add_end(val)
    assert isinstance(ll._head, Node)
    ll._head.get_data() == val
    ll._head.get_next() == ll._head._next == None
    assert len(ll) == ll._length == 1
    assert ll.to_list() == [item for item in ll] == [val]


def test_creating_linked_list_from_iterable():
    # Using from_iterable (small length)
    lst = get_list()
    ll = LinkedList.from_iterable(lst)
    assert isinstance(ll._head, Node)
    assert ll._head.get_data() == lst[0]
    assert len(ll) == ll._length == len(lst)
    assert ll.to_list() == [item for item in ll] == lst
    # Using from_iterable (has None)
    with pytest.raises(ValueError): LinkedList.from_iterable([1, 2, None, 3])
    with pytest.raises(TypeError): LinkedList().add_end(LinkedList())
    # Using from_iterable (big length)
    lst = get_list(length = 10000)
    ll = LinkedList.from_iterable(lst)
    assert isinstance(ll._head, Node)
    assert ll._head.get_data() == lst[0]
    assert len(ll) == ll._length == len(lst)
    assert ll.to_list() == [item for item in ll] == lst
    for _ in range(100): #check random indices
        idx = get_pos_int(b=10000-1)
        assert ll[idx].get_data() == lst[idx]
    # iterable is Linked List
    lst = get_list()
    tmp_ll = LinkedList.from_iterable(lst)
    ll = LinkedList.from_iterable(tmp_ll)
    assert ll == tmp_ll
    assert ll._head.get_data() == tmp_ll._head.get_data()
    assert len(ll) == ll._length == len(lst)
    assert ll.to_list() == [item for item in ll] == lst


def test_empty_linked_list():
    EMPTY = "┌─\n│\n└─" #represents empty LinkedList
    ll = LinkedList.from_iterable([])
    assert str(ll) == EMPTY
    assert ll._length == len(ll) == 0
    assert ll.is_empty()
    assert ll.to_list() == []
    assert [_ for _ in ll ] == []
    assert len(ll.copy()) == 0
    assert len(ll.reverse()) == 0
    #################### test operators ####################
    assert LinkedList() == LinkedList()
    assert ll == ll.copy()
    assert ll == ll.reverse()
    assert LinkedList() != LinkedList.from_iterable([get_value()])
    assert LinkedList() < LinkedList.from_iterable([get_value()])
    assert LinkedList() <= LinkedList.from_iterable([get_value()])
    assert LinkedList.from_iterable([get_value()]) > LinkedList()
    assert LinkedList.from_iterable([get_value()]) >= LinkedList()
    #################### test count ####################
    assert ll.count(0) == 0
    assert ll.count(None) == 0
    assert ll.count(get_value()) == 0
    assert ll.count(Node(get_value())) == 0
    #################### test __contains__ ####################
    assert None not in ll
    assert Node(get_value()) not in ll
    assert 0 not in ll
    assert get_value() not in ll
    assert LinkedList() not in ll
    #################### test split ####################
    left_list, right_list = ll.split(0)
    assert str(left_list) == str(right_list) == EMPTY
    with pytest.raises(TypeError): ll.split(get_string())
    with pytest.raises(TypeError): ll.split(get_float())
    with pytest.raises(TypeError): ll.split(True)
    with pytest.raises(IndexError): ll.split(-1)
    with pytest.raises(IndexError): ll.split(get_int())
    #################### test rotate ####################
    assert ll.rotate_left(get_pos_int(), inplace=False) == ll
    assert ll.rotate_right(get_pos_int(), inplace=False) == ll
    assert len(ll.rotate_left(get_pos_int(), inplace=False)) == 0
    assert len(ll.rotate_right(get_pos_int(), inplace=False)) == 0
    with pytest.raises(TypeError): ll.rotate_left(get_string())
    with pytest.raises(TypeError): ll.rotate_right(get_float())
    with pytest.raises(TypeError): ll.rotate_left([])
    with pytest.raises(ValueError): ll.rotate_left(get_neg_int())
    with pytest.raises(ValueError): ll.rotate_right(get_neg_int())
    #################### test remove/del ####################
    ll.remove_front() #shouldn't raise any Error
    ll.remove_end() #shouldn't raise any Error
    ll.remove(get_value())
    ll.remove(get_value(), False)
    with pytest.raises(TypeError): ll.remove(get_value(), all=get_string(1))
    with pytest.raises(IndexError): del ll[0]
    with pytest.raises(IndexError): del ll[get_pos_int()]
    with pytest.raises(IndexError): del ll[get_neg_int()]
    #################### test __getitem__ ####################
    with pytest.raises(IndexError): _ = ll[0]
    with pytest.raises(IndexError): _ = ll[get_pos_int()]
    with pytest.raises(IndexError): _ = ll[get_neg_int()]
    assert LinkedList() == ll[0:10]
    #################### test insert/set ####################
    with pytest.raises(IndexError): ll.insert(get_pos_int(), get_value())
    with pytest.raises(IndexError): ll.insert(get_neg_int(), get_value())
    with pytest.raises(IndexError): ll[0] = get_float()
    with pytest.raises(IndexError): ll[get_int()] = Node(get_float())
    with pytest.raises(ValueError): ll.insert(0, None)


def test_list_with_one_element():
    val = get_value()
    ll = LinkedList()
    ll.insert(0, val)
    assert isinstance(ll._head, Node)
    assert ll._head.get_data() == val
    assert ll._head.get_next() == None
    assert len(ll) == 1
    assert not ll.is_empty()
    assert val in ll
    assert [item for item in ll] == [val]
    assert ll.to_list() == [val]
    assert ll == ll.copy()
    assert ll == ll.reverse()
    #################### test rotate ####################
    assert ll == ll.rotate_left(get_pos_int(), inplace=False)
    assert ll == ll.rotate_right(get_pos_int(), inplace=False)
    #################### test operators ####################
    assert ll != LinkedList()
    assert ll > LinkedList()
    assert ll >= LinkedList()
    assert LinkedList() < ll
    assert LinkedList() <= ll
    #################### test add/remove ####################
    new_value = get_value()
    ll.add_front(new_value)
    assert new_value == ll.remove_front().get_data()
    ll.add_end(new_value)
    assert new_value == ll.remove_end().get_data()
    assert ll == LinkedList.from_iterable([val])
    #################### test insert/split ####################
    with pytest.raises(IndexError): ll.insert(2, get_value())
    with pytest.raises(IndexError): ll.insert(-1, get_value())
    with pytest.raises(IndexError): ll.split(get_pos_int(a=2))


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
    # test __setitem__()
    ll[1] = val
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


def test_list_with_known_values():
    ll = LinkedList()
    ll.add_front(10)
    ll.add_front(5)
    assert ll.to_list() == [5, 10]
    ll.remove(20)
    ll.remove_front()
    assert ll == LinkedList.from_iterable([10])
    ll.remove_end()
    assert ll == LinkedList() 
    ll.insert(0, 100)
    ll.insert(1, 200)
    ll.insert(1, 100)
    assert 100 in ll and 200 in ll
    assert ll == LinkedList.from_iterable([100, 100, 200])
    assert ll.copy().to_list() == [100, 100, 200]
    assert ll.reverse() == LinkedList.from_iterable([200, 100, 100])
    ll.remove(100)
    rev = ll.reverse()
    assert ll == rev == LinkedList.from_iterable([200])
    ll.clear()
    assert not rev.is_empty()
    assert ll.is_empty()
    ###################################################
    ll = LinkedList()
    ll.add_front(6)
    ll.add_end(20)
    ll.insert(1, 10)
    ll.insert(2, 77)
    ll.insert(4, 43)
    ll.insert(0, 2)
    assert 43 in ll
    assert ll[1:4].to_list() == [6, 10, 77]
    assert ll.copy().to_list() == [2, 6, 10, 77, 20, 43]
    del ll[len(ll)-1]
    assert ll.reverse().to_list() == [20, 77, 10, 6, 2]
    assert ll._length == len(ll) == 5
    ll.clear()
    assert ll.is_empty()


def test_list_with_random_numbers():
    # test add_end() and remove_end()
    lst = get_list(length=100)
    llist = LinkedList()
    for i in lst:
        llist.add_end(i)
    assert len(llist) == len(lst)
    assert llist._head.get_data() == lst[0]
    assert not llist.is_empty()
    for _ in range(len(lst)):
        assert llist[0].get_data() == lst[0]
        assert llist.remove_end().get_data() == lst.pop()
    assert len(llist) == 0
    assert llist.is_empty()
    # test add_front() and remove_front()
    lst = get_list(length=100)
    for i in lst:
        llist.add_front(i)
    assert len(llist) == len(lst)
    assert llist._head.get_data() == lst[-1]
    assert not llist.is_empty()
    for _ in range(len(lst)):
        assert llist[0].get_data() == lst[-1]
        assert llist.remove_front().get_data() == lst.pop()
    assert len(llist) == 0
    assert llist.is_empty()


def test_relational_operators():
    # linked lists have just one value
    assert LinkedList.from_iterable([3.14]) == LinkedList.from_iterable([3.14])
    assert LinkedList.from_iterable([get_int()]) != LinkedList.from_iterable([get_float()])
    assert LinkedList.from_iterable([get_string()]) != LinkedList.from_iterable([get_int()])
    assert LinkedList.from_iterable([get_float()]) != LinkedList.from_iterable([get_list()])
    assert LinkedList.from_iterable([2.9999]) < LinkedList.from_iterable([3])
    assert LinkedList.from_iterable([3.14]) <= LinkedList.from_iterable([3.14])
    assert LinkedList.from_iterable([1, 2]) > LinkedList.from_iterable([3])
    assert LinkedList.from_iterable(['3.14']) >= LinkedList.from_iterable(['3.14'])
    with pytest.raises(TypeError): LinkedList.from_iterable([get_float()]) < LinkedList.from_iterable([get_string()])
    with pytest.raises(TypeError): LinkedList.from_iterable([get_value()]) <= LinkedList.from_iterable([get_list()])
    with pytest.raises(TypeError): LinkedList.from_iterable([get_string()]) > LinkedList.from_iterable([get_list()])
    with pytest.raises(TypeError): LinkedList.from_iterable([get_list()]) >= LinkedList.from_iterable([get_float()])
    # linked lists have more than one value
    llist1 = LinkedList.from_iterable([1, '2', 3.14])
    llist2 = LinkedList.from_iterable([1, '2', 5.14])
    assert llist1 == llist1
    assert llist1 != llist2
    assert llist1 < llist2
    assert llist1 <= llist2
    assert llist2 > llist2
    assert llist2 >= llist2
    # slicing lists
    assert llist1[:-1] == llist2[:-1]
    assert llist1[-1:] != llist2[-1:]
    assert llist1[:1] < llist2
    assert llist1[:2] <= llist2
    with pytest.raises(TypeError): assert llist1[1:] < llist2
    with pytest.raises(TypeError): assert llist1[1:] <= llist2
    # if the other one isn't a linked list
    actual_list = [1, '2', 5.14]
    with pytest.raises(TypeError): assert llist1 == actual_list
    with pytest.raises(TypeError): assert llist1 != actual_list
    with pytest.raises(TypeError): assert llist1 < actual_list
    with pytest.raises(TypeError): assert llist1 <= actual_list
    with pytest.raises(TypeError): assert llist2 > actual_list
    with pytest.raises(TypeError): assert llist2 >= actual_list


def test_rotate():
    # rotate when inplace = False
    ll = LinkedList.from_iterable([1, 2, 3, 4, 5, 6])
    rotated = ll.rotate_right(1, inplace=False)
    assert rotated.to_list() == [6, 1, 2, 3, 4 ,5]
    assert isinstance(rotated._head, Node)
    assert rotated._head.get_data() == 6
    assert rotated[4].get_data() == 4
    rotated = ll.rotate_left(3, inplace=False)
    assert isinstance(rotated._head, Node)
    assert rotated.to_list() == [4, 5, 6, 1, 2, 3]
    assert rotated._head.get_data() == 4
    assert rotated[-1].get_data() == 3
    assert ll.to_list() == [1, 2, 3, 4, 5, 6]
    # rotate when inplace = True
    ll.rotate_right(1)
    assert ll.to_list() == [6, 1, 2, 3, 4 ,5]
    assert isinstance(ll._head, Node)
    assert ll._head.get_data() == 6
    ll.rotate_left(3)
    assert ll.to_list() == [3, 4 ,5, 6, 1, 2]
    assert ll._head.get_data() == 3
    assert isinstance(ll._head, Node)


def test_join_method():
    lst = get_list()
    # two linked lists are empty
    llist1 = LinkedList()
    llist1.join(LinkedList())
    assert llist1 == LinkedList()
    # one linked list is empty
    llist1 = LinkedList.from_iterable([])
    llist2 = LinkedList.from_iterable(lst)
    llist1.join(llist2)
    assert llist1 == llist2
    assert len(llist1) == len(lst)
    llist2.join(llist1)
    assert len(llist2) == 2*len(lst)
    # two linked lists are NOT empty
    llist1 = LinkedList.from_iterable(lst)
    llist2 = LinkedList.from_iterable(lst)
    llist2.join(llist1)
    assert llist1.to_list() == lst
    assert llist2.to_list() == lst+lst
    assert len(llist2) == 2*len(lst)


def test_split_method():
    lst = get_list(length=100)
    ll = LinkedList.from_iterable(lst)
    for i in range(len(lst)):
        # test left list
        left_list, right_list = ll.split(i)
        assert isinstance(left_list, LinkedList)
        assert left_list.to_list() == lst[:i]
        assert left_list.copy().to_list() == lst[:i]
        assert left_list.reverse().to_list() == lst[:i][::-1]
        # test right list
        assert isinstance(right_list, LinkedList)
        assert right_list.to_list() == lst[i:]
        assert right_list.copy().to_list() == lst[i:]
        assert right_list.reverse().to_list() == lst[i:][::-1]
    ll.add_front(0)
    ll.add_end('apple')
    assert ll._length == len(ll) == len(lst)+2
    assert ll.to_list() == [0]+lst+['apple']

