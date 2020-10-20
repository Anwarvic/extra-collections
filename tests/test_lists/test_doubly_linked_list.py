import pytest

from extra.lists.linked_list import Node, LinkedList
from extra.lists.doubly_linked_list import DoublyNode, DoublyLinkedList


def test_not_empty_doubly_node(helper):
    val = helper.get_value()
    node = DoublyNode(val)
    assert node.get_data() == val
    assert node.get_next() is None
    assert node.get_prev() is None
    node.set_next(None)
    node.set_prev(None)
    with pytest.raises(ValueError):
        DoublyNode(None)
    with pytest.raises(ValueError):
        node.set_data(None)
    with pytest.raises(ValueError):
        node.set_next(Node(None))
    with pytest.raises(ValueError):
        node.set_prev(Node(None))
    node.set_next(DoublyNode(helper.get_value()))  # do nothing
    node.set_prev(DoublyNode(helper.get_value()))  # do nothing
    # Given value: has __iter__ attribute
    lst = helper.get_list()
    node = DoublyNode(lst)
    assert node.get_data() == lst
    assert node.get_next() is None
    assert node.get_prev() is None
    node.set_next(DoublyNode(helper.get_string()))
    node.set_prev(DoublyNode(helper.get_string()))
    # Given value: LinkedList()
    dl = LinkedList(helper.get_list())
    with pytest.raises(TypeError):
        DoublyNode(dl)
    # Given value: LinkedList()
    dl = DoublyLinkedList(helper.get_list())
    with pytest.raises(TypeError):
        DoublyNode(dl)


def test_creating_doubly_linked_list_from_constructor(helper):
    # Using constructor
    val = helper.get_value()
    dl = DoublyLinkedList()
    dl.add_front(val)
    dl._head.get_data() == dl._tail.get_data() == val
    dl._head.get_next() == dl._head._next is None
    dl._head.get_prev() == dl._head._prev is None
    dl._tail.get_next() == dl._head._next is None
    dl._tail.get_prev() == dl._head._prev is None
    assert len(dl) == dl._length == 1
    assert dl.to_list() == [item for item in dl] == [val]

    dl = DoublyLinkedList()
    with pytest.raises(TypeError):
        dl.add_end(Node(helper.get_value()))
    with pytest.raises(TypeError):
        dl.add_front(Node(helper.get_value()))

    # Using Node
    dl = DoublyLinkedList()
    with pytest.raises(TypeError):
        dl.add_end(Node(helper.get_value()))
    with pytest.raises(TypeError):
        dl.add_front(Node(helper.get_value()))
    assert len(dl) == dl._length == 0
    assert dl.to_list() == [item for item in dl] == []

    # Using DoublyNode
    dl = DoublyLinkedList()
    with pytest.raises(TypeError):
        dl.add_end(DoublyNode(helper.get_value()))
    with pytest.raises(TypeError):
        dl.add_front(DoublyNode(helper.get_value()))
    assert len(dl) == dl._length == 0
    assert dl.to_list() == [item for item in dl] == []


def test_creating_doubly_linked_list_from_iterable(helper):
    # Using from_iterable (small length)
    lst = helper.get_list()
    dl = DoublyLinkedList(lst)
    assert dl._head.get_data() == lst[0]
    assert dl._tail.get_data() == lst[-1]
    assert len(dl) == dl._length == len(lst)
    assert dl.to_list() == [item for item in dl] == lst
    # Using from_iterable (has None)
    with pytest.raises(ValueError):
        DoublyLinkedList([1, 2, None, 3])
    with pytest.raises(TypeError):
        DoublyLinkedList().add_end(LinkedList())
    with pytest.raises(TypeError):
        DoublyLinkedList().add_front(DoublyLinkedList())
    # Using from_iterable (big length)
    lst = helper.get_list(length=10000)
    dl = DoublyLinkedList(lst)
    assert dl._head.get_data() == lst[0]
    assert dl._tail.get_data() == lst[-1]
    assert len(dl) == dl._length == len(lst)
    assert dl.to_list() == [item for item in dl] == lst
    for _ in range(100):  # check random indices
        idx = helper.get_pos_int(b=10000 - 1)
        assert dl[idx] == lst[idx]
    # Using Linked List
    lst = helper.get_list()
    tmp_dl = DoublyLinkedList(lst)
    dl = DoublyLinkedList(tmp_dl)
    assert dl == tmp_dl
    assert len(dl) == dl._length == len(lst)
    assert dl.to_list() == [item for item in dl] == lst


def test_empty_doubly_linked_list(helper):
    EMPTY = "┌─\n│\n└─"  # represents empty Doubly LinkedList
    dl = DoublyLinkedList()
    assert str(dl) == EMPTY
    assert dl._length == len(dl) == 0
    assert dl.is_empty()
    assert dl.to_list() == []
    assert [_ for _ in dl] == []
    assert len(dl.copy()) == 0
    assert len(dl.reverse()) == 0
    # ==================== test operators ====================
    with pytest.raises(TypeError):
        LinkedList() == DoublyLinkedList()
    with pytest.raises(TypeError):
        LinkedList() != DoublyLinkedList()
    with pytest.raises(TypeError):
        LinkedList() > DoublyLinkedList()
    with pytest.raises(TypeError):
        LinkedList() >= DoublyLinkedList()
    with pytest.raises(TypeError):
        LinkedList() < DoublyLinkedList()
    with pytest.raises(TypeError):
        LinkedList() <= DoublyLinkedList()
    assert DoublyLinkedList() == DoublyLinkedList()
    assert dl == dl.copy()
    assert dl == dl.reverse()
    assert DoublyLinkedList() != DoublyLinkedList([helper.get_value()])
    assert DoublyLinkedList() < DoublyLinkedList([helper.get_value()])
    assert DoublyLinkedList() <= DoublyLinkedList([helper.get_value()])
    assert DoublyLinkedList([helper.get_value()]) > DoublyLinkedList()
    assert DoublyLinkedList([helper.get_value()]) >= DoublyLinkedList()
    # ==================== test count ====================
    assert dl.count(0) == 0
    assert dl.count(None) == 0
    assert dl.count(Node(helper.get_value())) == 0
    assert dl.count(DoublyNode(helper.get_value())) == 0
    assert dl.count(helper.get_value()) == 0
    # ==================== test __contains__ ====================
    assert None not in dl
    assert Node(helper.get_value()) not in dl
    assert 0 not in dl
    assert helper.get_value() not in dl
    assert LinkedList() not in dl
    # ==================== test split ====================
    left_list, right_list = dl.split(0)
    assert str(left_list) == str(right_list) == EMPTY
    with pytest.raises(TypeError):
        dl.split(helper.get_string())
    with pytest.raises(TypeError):
        dl.split(helper.get_float())
    with pytest.raises(TypeError):
        dl.split(True)
    with pytest.raises(IndexError):
        dl.split(-1)
    with pytest.raises(IndexError):
        dl.split(helper.get_int())
    # ==================== test rotate ====================
    assert dl.rotate_left(helper.get_pos_int(), inplace=False) == dl
    assert dl.rotate_right(helper.get_pos_int(), inplace=False) == dl
    assert len(dl.rotate_left(helper.get_pos_int(), inplace=False)) == 0
    assert len(dl.rotate_right(helper.get_pos_int(), inplace=False)) == 0
    with pytest.raises(TypeError):
        dl.rotate_left(helper.get_string())
    with pytest.raises(TypeError):
        dl.rotate_right(helper.get_float())
    with pytest.raises(TypeError):
        dl.rotate_left([])
    with pytest.raises(ValueError):
        dl.rotate_left(helper.get_neg_int())
    with pytest.raises(ValueError):
        dl.rotate_right(helper.get_neg_int())
    # ==================== test remove/del ====================
    dl.remove_front()  # shouldn't raise any Error
    dl.remove_end()  # shouldn't raise any Error
    dl.remove(helper.get_value())
    dl.remove(helper.get_value(), False)
    with pytest.raises(TypeError):
        dl.remove(helper.get_value(), all=helper.get_string())
    with pytest.raises(IndexError):
        del dl[0], dl[helper.get_pos_int()], dl[helper.get_neg_int()]
    # ==================== test __getitem__ ====================
    with pytest.raises(IndexError):
        _ = dl[0]
    with pytest.raises(IndexError):
        _ = dl[helper.get_pos_int()]
    with pytest.raises(IndexError):
        _ = dl[helper.get_neg_int()]
    assert DoublyLinkedList() == dl[0:10]
    # ==================== test insert/set ====================
    with pytest.raises(IndexError):
        dl.insert(helper.get_pos_int(), helper.get_pos_int())
    with pytest.raises(IndexError):
        dl.insert(helper.get_neg_int(), helper.get_pos_int())
    with pytest.raises(IndexError):
        dl[0] = helper.get_float()
    with pytest.raises(IndexError):
        dl[helper.get_int()] = Node(helper.get_float())
    with pytest.raises(ValueError):
        dl.insert(0, None)
    with pytest.raises(TypeError):
        dl.insert(0, Node(helper.get_value()))


def test_list_with_one_element(helper):
    val = helper.get_value()
    dl = DoublyLinkedList()
    dl.insert(0, val)
    assert dl._head.get_data() == val
    assert dl._tail.get_data() == val
    assert dl._head.get_next() is None
    assert dl._head.get_prev() is None
    assert dl._tail.get_next() is None
    assert dl._tail.get_prev() is None
    assert len(dl) == 1
    assert not dl.is_empty()
    assert val in dl
    assert [item for item in dl] == [val]
    assert dl.to_list() == [val]
    assert dl == dl.copy()
    assert dl == dl.reverse()
    # ==================== test rotate ====================
    assert dl == dl.rotate_left(helper.get_pos_int(), inplace=False)
    assert dl == dl.rotate_right(helper.get_pos_int(), inplace=False)
    # ==================== test operators ====================
    assert dl != DoublyLinkedList()
    assert dl > DoublyLinkedList()
    assert dl >= DoublyLinkedList()
    assert DoublyLinkedList() < dl
    assert DoublyLinkedList() <= dl
    with pytest.raises(TypeError):
        assert dl != LinkedList()
    with pytest.raises(TypeError):
        assert dl > LinkedList()
    with pytest.raises(TypeError):
        assert dl >= LinkedList()
    with pytest.raises(TypeError):
        assert LinkedList() < dl
    with pytest.raises(TypeError):
        assert LinkedList() <= dl
    # ==================== test add/remove ====================
    new_value = helper.get_value()
    dl.add_front(new_value)
    dl.remove_front()
    dl.add_end(new_value)
    dl.remove_end()
    tmp_dl = DoublyLinkedList()
    tmp_dl.add_front(val)
    assert dl == tmp_dl
    # ==================== test insert/split ====================
    with pytest.raises(IndexError):
        dl.insert(2, helper.get_value())
    with pytest.raises(IndexError):
        dl.insert(-1, helper.get_value())
    with pytest.raises(IndexError):
        dl.split(helper.get_pos_int(a=2))


def test_list_with_same_value(helper):
    length = helper.get_pos_int()
    val = helper.get_value()
    dl = DoublyLinkedList()
    # test add_end
    for _ in range(length):
        dl.add_end(val)
    # test add_front
    for _ in range(length):
        dl.add_front(val)
    # test __setitem__()
    dl[1] = val
    assert dl == dl.reverse()
    assert dl == dl.copy()
    assert not dl.is_empty()
    assert len(dl) == 2 * length
    assert dl.count(val) == 2 * length
    assert dl.to_list() == [val] * (2 * length)
    # test split
    left_list, right_list = dl.split(length)
    assert len(left_list) == len(right_list) == length
    # test clear
    left_list.clear()
    right_list.clear()
    assert len(left_list) == len(right_list) == 0
    # test remove
    for i in range(length):
        if i > length // 2:
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
    dl.remove_end()
    assert dl == DoublyLinkedList()
    dl.insert(0, 100)
    dl.insert(1, 200)
    dl.insert(1, 100)
    assert 100 in dl and 200 in dl
    assert dl == DoublyLinkedList([100, 100, 200])
    assert dl.copy().to_list() == [100, 100, 200]
    assert dl.reverse() == DoublyLinkedList([200, 100, 100])
    dl.remove(100)
    rev = dl.reverse()
    assert dl == rev
    dl.clear()
    assert not rev.is_empty()
    assert dl.is_empty()
    # ==================================================
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
    del dl[len(dl) - 1]
    assert dl.reverse().to_list() == [20, 77, 10, 6, 2]
    assert dl._length == len(dl) == 5
    dl.clear()
    assert dl.is_empty()


def test_list_with_random_numbers(helper):
    # test add_end() and remove_end()
    lst = helper.get_list(length=100)
    dl = DoublyLinkedList()
    for i in lst:
        dl.add_end(i)
    assert len(dl) == len(lst)
    assert dl._head.get_data() == lst[0]
    assert not dl.is_empty()
    for _ in range(len(lst)):
        assert dl[0] == lst[0]
        lst.pop()
        dl.remove_end()
    assert len(dl) == 0
    assert dl.is_empty()
    # test add_front() and remove_front()
    lst = helper.get_list(length=100)
    for i in lst:
        dl.add_front(i)
    assert len(dl) == len(lst)
    assert dl._head.get_data() == lst[-1]
    assert not dl.is_empty()
    for _ in range(len(lst)):
        assert dl[0] == lst[-1]
        lst.pop()
        dl.remove_front()
    assert len(dl) == 0
    assert dl.is_empty()


def test_relational_operators(helper):
    # linked lists have just one value
    assert DoublyLinkedList([3.14]) == DoublyLinkedList([3.14])
    assert (
        DoublyLinkedList([helper.get_int()])
        != DoublyLinkedList([helper.get_float()])
    )
    assert (
        DoublyLinkedList([helper.get_string()])
        != DoublyLinkedList([helper.get_int()])
    )
    assert (
        DoublyLinkedList([helper.get_float()])
        != DoublyLinkedList([helper.get_list()])
    )
    assert DoublyLinkedList([2.9999]) < DoublyLinkedList([3])
    assert DoublyLinkedList([3.14]) <= DoublyLinkedList([3.14])
    assert DoublyLinkedList([3, 2]) > DoublyLinkedList([3])
    assert DoublyLinkedList(["3.14"]) >= DoublyLinkedList(["3.14"])
    with pytest.raises(TypeError):
        (
            DoublyLinkedList([helper.get_float()])
            < DoublyLinkedList([helper.get_string()])
        )
    with pytest.raises(TypeError):
        (
            DoublyLinkedList([helper.get_value()])
            <= DoublyLinkedList([helper.get_list()])
        )
    with pytest.raises(TypeError):
        (
            DoublyLinkedList([helper.get_string()])
            > DoublyLinkedList([helper.get_list()])
        )
    with pytest.raises(TypeError):
        (
            DoublyLinkedList([helper.get_list()])
            >= DoublyLinkedList([helper.get_float()])
        )
    # linked lists have more than one value
    dllist1 = DoublyLinkedList([1, "2", 3.14])
    dllist2 = DoublyLinkedList([1, "2", 5.14])
    assert dllist1 == dllist1
    assert dllist1 != dllist2
    assert dllist1 < dllist2
    assert dllist1 <= dllist2
    assert dllist2 > dllist1
    assert dllist2 >= dllist1
    # slicing lists
    assert dllist1[:-1] == dllist2[:-1]
    assert dllist1[-1:] != dllist2[-1:]
    assert dllist1[:1] < dllist2
    assert dllist1[:2] <= dllist2
    with pytest.raises(TypeError):
        assert dllist1[1:] < dllist2
    with pytest.raises(TypeError):
        assert dllist1[1:] <= dllist2
    # if the other one isn't a doubly linked list
    actual_list = [1, "2", 5.14]
    with pytest.raises(TypeError):
        assert dllist1 == actual_list
    with pytest.raises(TypeError):
        assert dllist1 != actual_list
    with pytest.raises(TypeError):
        assert dllist1 < actual_list
    with pytest.raises(TypeError):
        assert dllist1 <= actual_list
    with pytest.raises(TypeError):
        assert dllist2 > actual_list
    with pytest.raises(TypeError):
        assert dllist2 >= actual_list
    # if the other one is a linked list
    llist = LinkedList([1, "2", 5.14])
    with pytest.raises(TypeError):
        assert dllist1 == llist
    with pytest.raises(TypeError):
        assert dllist1 != llist
    with pytest.raises(TypeError):
        assert dllist1 < llist
    with pytest.raises(TypeError):
        assert dllist1 <= llist
    with pytest.raises(TypeError):
        assert dllist2 > llist
    with pytest.raises(TypeError):
        assert dllist2 >= llist


def test_rotate():
    # rotate when inplace = False
    dl = DoublyLinkedList([1, 2, 3, 4, 5, 6])
    rotated = dl.rotate_right(1, inplace=False)
    assert isinstance(rotated._head, DoublyNode)
    assert isinstance(rotated._tail, DoublyNode)
    assert rotated.to_list() == [6, 1, 2, 3, 4, 5]
    assert rotated._head.get_data() == 6
    assert rotated._head.get_prev() is None
    assert rotated._tail.get_data() == 5
    assert rotated._tail.get_next() is None
    assert rotated[4] == 4
    rotated = dl.rotate_left(3, inplace=False)
    assert isinstance(rotated._head, DoublyNode)
    assert isinstance(rotated._tail, DoublyNode)
    assert rotated.to_list() == [4, 5, 6, 1, 2, 3]
    assert rotated._head.get_data() == 4
    assert rotated._head.get_prev() is None
    assert rotated._tail.get_data() == 3
    assert rotated._tail.get_next() is None
    assert rotated[-2] == 2
    assert dl.to_list() == [1, 2, 3, 4, 5, 6]
    # rotate when inplace = True
    dl.rotate_right(1)
    assert isinstance(dl._head, DoublyNode)
    assert isinstance(dl._tail, DoublyNode)
    assert dl.to_list() == [6, 1, 2, 3, 4, 5]
    assert dl._head.get_data() == 6
    assert dl._head.get_prev() is None
    assert dl._tail.get_data() == 5
    assert dl._tail.get_next() is None
    assert dl[4] == 4
    dl.rotate_left(3)
    assert isinstance(rotated._head, DoublyNode)
    assert isinstance(rotated._tail, DoublyNode)
    assert dl.to_list() == [3, 4, 5, 6, 1, 2]
    assert dl._head.get_data() == 3
    assert dl._head.get_prev() is None
    assert dl._tail.get_data() == 2
    assert dl._tail.get_next() is None
    assert dl[-1] == 2


def test_extend_method(helper):
    lst = helper.get_list()
    # two Doubly linked lists are empty
    dllist1 = DoublyLinkedList()
    dllist1.extend(DoublyLinkedList())
    assert dllist1 == DoublyLinkedList()
    # one linked list is empty
    dllist1 = DoublyLinkedList([])
    dllist2 = DoublyLinkedList(lst)
    dllist1.extend(dllist2)
    assert dllist1 == dllist2
    assert len(dllist1) == len(lst)
    dllist2.extend(dllist1)
    assert len(dllist2) == 2 * len(lst)
    # two linked lists are NOT empty
    dllist1 = DoublyLinkedList(lst)
    dllist2 = DoublyLinkedList(lst)
    dllist2.extend(dllist1)
    assert dllist1.to_list() == lst
    assert dllist2.to_list() == lst + lst
    assert len(dllist2) == 2 * len(lst)
    # extend other data type
    with pytest.raises(TypeError):
        DoublyLinkedList().extend(LinkedList())
    with pytest.raises(TypeError):
        DoublyLinkedList().extend(helper.get_list())
    with pytest.raises(TypeError):
        DoublyLinkedList().extend(helper.get_value())


def test_split(helper):
    lst = helper.get_list(length=100)
    dl = DoublyLinkedList(lst)
    for i in range(len(lst)):
        # test left list
        left_list, right_list = dl.split(i)
        assert isinstance(left_list, DoublyLinkedList)
        assert left_list.to_list() == lst[:i]
        assert left_list.copy().to_list() == lst[:i]
        assert left_list.reverse().to_list() == lst[:i][::-1]
        # test right list
        assert isinstance(right_list, DoublyLinkedList)
        assert right_list.to_list() == lst[i:]
        assert right_list.copy().to_list() == lst[i:]
        assert right_list.reverse().to_list() == lst[i:][::-1]
    dl.add_front(0)
    dl.add_end("apple")
    assert dl._length == len(dl) == len(lst) + 2
    assert dl.to_list() == [0] + lst + ["apple"]
