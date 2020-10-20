import pytest

from tests import get_string, get_value, get_list, get_pos_int, get_float, \
    get_int, get_neg_int
from extra.lists.linked_list import Node, LinkedList
from extra.lists.circular_linked_list import CircularLinkedList
from extra.lists.doubly_linked_list import DoublyNode, DoublyLinkedList


def test_creating_circular_linked_list_from_constructor():
    # Using constructor
    val = get_value()
    cll = CircularLinkedList()
    cll.add_front(val)
    assert isinstance(cll._head, Node)
    assert cll._head.get_data() == val
    assert cll._head.get_next() == cll._head._next == cll._head
    assert len(cll) == cll._length == 1
    assert cll.to_list() == [item for item in cll] == [val]
    # Using Node
    cll = CircularLinkedList()
    with pytest.raises(TypeError):
        cll.add_front(DoublyNode(get_value()))
    val = get_value()
    cll = CircularLinkedList()
    cll.add_end(val)
    assert isinstance(cll._head, Node)
    cll._head.get_data() == val
    cll._head.get_next() == cll._head._next == cll._head
    assert len(cll) == cll._length == 1
    assert cll.to_list() == [item for item in cll] == [val]


def test_creating_circular_linked_list_from_iterable():
    # Using from_iterable (small length)
    lst = get_list()
    cll = CircularLinkedList(lst)
    assert cll._head.get_data() == lst[0]
    assert len(cll) == cll._length == len(lst)
    assert cll.to_list() == [item for item in cll] == lst
    # Using from_iterable (has None)
    with pytest.raises(ValueError):
        CircularLinkedList([1, 2, None, 3])
    with pytest.raises(TypeError):
        CircularLinkedList().add_end(LinkedList())
    with pytest.raises(TypeError):
        CircularLinkedList().add_front(DoublyLinkedList())
    with pytest.raises(TypeError):
        CircularLinkedList().add_front(CircularLinkedList())
    # Using from_iterable (big length)
    lst = get_list(length=10000)
    cll = CircularLinkedList(lst)
    assert cll._head.get_data() == lst[0]
    assert len(cll) == cll._length == len(lst)
    assert cll.to_list() == [item for item in cll] == lst
    for _ in range(100):  # check random indices
        idx = get_pos_int(b=10000 - 1)
        assert cll[idx] == lst[idx]
    # Using Linked List
    lst = get_list()
    tmp_cll = CircularLinkedList(lst)
    cll = CircularLinkedList(tmp_cll)
    # assert cll == tmp_cll
    assert len(cll) == cll._length == len(lst)
    assert cll.to_list() == [item for item in cll] == lst


def test_empty_circular_linked_list():
    EMPTY = "┌─\n│\n└─"  # represents empty LinkedList
    cll = CircularLinkedList([])
    assert str(cll) == EMPTY
    assert cll._length == len(cll) == 0
    assert cll.is_empty()
    assert cll.to_list() == []
    assert [_ for _ in cll] == []
    assert len(cll.copy()) == 0
    assert len(cll.reverse()) == 0
    # ==================== test operators ====================
    assert CircularLinkedList() == CircularLinkedList()
    assert cll == cll.copy()
    assert cll == cll.reverse()
    assert CircularLinkedList() != CircularLinkedList([get_value()])
    assert CircularLinkedList() < CircularLinkedList([get_value()])
    assert CircularLinkedList() <= CircularLinkedList([get_value()])
    assert CircularLinkedList([get_value()]) > CircularLinkedList()
    assert CircularLinkedList([get_value()]) >= CircularLinkedList()
    # ==================== test count ====================
    assert cll.count(0) == 0
    assert cll.count(get_value()) == 0
    assert cll.count(Node(get_value())) == 0
    # ==================== test __contains__ ====================
    assert None not in cll
    assert Node(get_value()) not in cll
    assert 0 not in cll
    assert get_value() not in cll
    assert LinkedList() not in cll
    # assert LinkedList(get_value()) not in ll
    # ==================== test split ====================
    left_list, right_list = cll.split(0)
    assert str(left_list) == str(right_list) == EMPTY
    with pytest.raises(TypeError):
        cll.split(get_string())
    with pytest.raises(TypeError):
        cll.split(get_float())
    with pytest.raises(TypeError):
        cll.split(True)
    with pytest.raises(IndexError):
        cll.split(-1)
    cll.split(get_pos_int())  # shouldn't raise anything
    with pytest.raises(IndexError):
        cll.split(get_neg_int())
    # ==================== test rotate ====================
    assert cll.rotate_left(get_pos_int(), inplace=False) == cll
    assert cll.rotate_right(get_pos_int(), inplace=False) == cll
    assert len(cll.rotate_left(get_pos_int(), inplace=False)) == 0
    assert len(cll.rotate_right(get_pos_int(), inplace=False)) == 0
    with pytest.raises(TypeError):
        cll.rotate_left(get_string())
    with pytest.raises(TypeError):
        cll.rotate_right(get_float())
    with pytest.raises(TypeError):
        cll.rotate_left([])
    with pytest.raises(ValueError):
        cll.rotate_left(get_neg_int())
    with pytest.raises(ValueError):
        cll.rotate_right(get_neg_int())
    # ==================== test remove/del ====================
    cll.remove_front()  # shouldn't raise any Error
    cll.remove_end()  # shouldn't raise any Error
    cll.remove(get_value())
    cll.remove(get_value(), False)
    with pytest.raises(TypeError):
        cll.remove(get_value(), all=get_string(1))
    del cll[0]  # shouldn't raise anything
    del cll[get_pos_int()]  # shouldn't raise anything
    with pytest.raises(IndexError):
        del cll[get_neg_int()]
    # ==================== test __getitem__ ====================
    with pytest.raises(IndexError):
        _ = cll[0]
    with pytest.raises(IndexError):
        _ = cll[get_pos_int()]
    with pytest.raises(IndexError):
        _ = cll[get_neg_int()]
    with pytest.raises(IndexError):
        CircularLinkedList() == cll[0:10]
    # ==================== test insert/set ====================
    cll.insert(get_pos_int(), get_value())  # shouldn't raise anything
    with pytest.raises(IndexError):
        cll.insert(get_neg_int(), get_value())
    cll[0] = get_float()  # shouldn't raise anything
    cll[get_pos_int()] = get_float()  # shouldn't raise anything
    with pytest.raises(ValueError):
        cll.insert(0, None)
    with pytest.raises(TypeError):
        cll.insert(0, Node(get_value()))


def test_circular_linked_list_with_one_element():
    val = get_value()
    cll = CircularLinkedList()
    cll.insert(0, val)
    assert isinstance(cll._head, Node)
    assert cll._head.get_data() == val
    assert cll._head.get_next() == cll._head
    assert len(cll) == 1
    assert not cll.is_empty()
    assert val in cll
    assert [item for item in cll] == [val]
    assert cll.to_list() == [val]
    assert cll == cll.copy()
    assert cll == cll.reverse()
    # ==================== test rotate ====================
    assert cll == cll.rotate_left(get_pos_int(), inplace=False)
    assert cll == cll.rotate_right(get_pos_int(), inplace=False)
    # ==================== test operators ====================
    assert cll != CircularLinkedList()
    assert cll > CircularLinkedList()
    assert cll >= CircularLinkedList()
    assert CircularLinkedList() < cll
    assert CircularLinkedList() <= cll
    # ==================== test add/remove ====================
    new_value = get_value()
    cll.add_front(new_value)
    cll.remove_front()
    cll.add_end(new_value)
    cll.remove_end()
    assert cll == CircularLinkedList([val])
    # ==================== test insert/split ====================
    with pytest.raises(IndexError):
        cll.insert(-1, get_value())
    cll.insert(2, get_value())  # shouldn't raise anything
    cll.split(get_pos_int())  # shouldn't raise anything


def test_list_with_same_value():
    length = get_pos_int()
    val = get_value()
    cll = CircularLinkedList()
    # test add_end
    for _ in range(length):
        cll.add_end(val)
    # test add_front
    for _ in range(length):
        cll.add_front(val)
    # test __setitem__()
    cll[1] = val
    assert cll == cll.reverse()
    assert cll == cll.copy()
    assert not cll.is_empty()
    assert len(cll) == 2 * length
    assert cll.count(val) == 2 * length
    assert cll.to_list() == [val] * (2 * length)
    # test split
    left_list, right_list = cll.split(length)
    assert len(left_list) == len(right_list) == length
    # test clear
    left_list.clear()
    right_list.clear()
    assert len(left_list) == len(right_list) == 0
    # test remove
    for i in range(length):
        if i > length // 2:
            cll.remove_end()
        else:
            cll.remove_front()
    assert len(cll) == cll.count(val) == length
    cll.remove(val, all=True)
    assert cll.is_empty()
    assert len(cll) == 0


def test_circular_linked_list_with_known_values():
    cll = CircularLinkedList()
    cll.add_front(10)
    cll.add_front(5)
    assert cll.to_list() == [5, 10]
    cll.remove(20)
    cll.remove_front()
    assert cll == CircularLinkedList([10])
    cll.remove_end()
    assert cll == CircularLinkedList()
    cll.insert(0, 100)
    cll.insert(1, 200)
    cll.insert(1, 100)
    assert 100 in cll and 200 in cll
    assert cll == CircularLinkedList([100, 100, 200])
    assert cll.copy().to_list() == [100, 100, 200]
    assert cll.reverse() == CircularLinkedList([200, 100, 100])
    cll.remove(100)
    rev = cll.reverse()
    assert cll == rev == CircularLinkedList([200])
    cll.clear()
    assert not rev.is_empty()
    assert cll.is_empty()
    # ==================================================
    cll = LinkedList()
    cll.add_front(6)
    cll.add_end(20)
    cll.insert(1, 10)
    cll.insert(2, 77)
    cll.insert(4, 43)
    cll.insert(0, 2)
    assert 43 in cll
    assert cll[1:4].to_list() == [6, 10, 77]
    assert cll.copy().to_list() == [2, 6, 10, 77, 20, 43]
    del cll[len(cll) - 1]
    assert cll.reverse().to_list() == [20, 77, 10, 6, 2]
    assert cll._length == len(cll) == 5
    cll.clear()
    assert cll.is_empty()


def test_circular_linked_list_with_random_numbers():
    # test add_end() and remove_end()
    lst = get_list(length=100)
    cll = CircularLinkedList()
    for i in lst:
        cll.add_end(i)
    assert len(cll) == len(lst)
    assert cll._head.get_data() == lst[0]
    assert not cll.is_empty()
    for _ in range(len(lst)):
        assert cll[0] == lst[0]
        cll.remove_end()
        lst.pop()
    assert len(cll) == 0
    assert cll.is_empty()
    # test add_front() and remove_front()
    lst = get_list(length=100)
    for i in lst:
        cll.add_front(i)
    assert len(cll) == len(lst)
    assert cll._head.get_data() == lst[-1]
    assert not cll.is_empty()
    for _ in range(len(lst)):
        assert cll[0] == lst[-1]
        cll.remove_front()
        lst.pop()
    assert len(cll) == 0
    assert cll.is_empty()


def test_relational_operators():
    # linked lists have just one value
    assert CircularLinkedList([3.14]) == CircularLinkedList([3.14])
    assert CircularLinkedList([get_int()]) != CircularLinkedList([get_float()])
    assert (
        CircularLinkedList([get_string()]) != CircularLinkedList([get_int()])
    )
    assert (
        CircularLinkedList([get_float()]) != CircularLinkedList([get_list()])
    )
    assert CircularLinkedList([2.9999]) < CircularLinkedList([3])
    assert CircularLinkedList([3.14]) <= CircularLinkedList([3.14])
    assert CircularLinkedList([3, 2]) > CircularLinkedList([3])
    assert CircularLinkedList(["3.14"]) >= CircularLinkedList(["3.14"])
    with pytest.raises(TypeError):
        CircularLinkedList([get_float()]) < CircularLinkedList([get_string()])
    with pytest.raises(TypeError):
        CircularLinkedList([get_value()]) <= CircularLinkedList([get_list()])
    with pytest.raises(TypeError):
        CircularLinkedList([get_string()]) > CircularLinkedList([get_list()])
    with pytest.raises(TypeError):
        CircularLinkedList([get_list()]) >= CircularLinkedList([get_float()])
    # linked lists have more than one value
    cll1 = CircularLinkedList([1, "2", 3.14])
    cll2 = CircularLinkedList([1, "2", 5.14])
    assert cll1 == cll1
    assert cll1 != cll2
    assert cll1 < cll2
    assert cll1 <= cll2
    assert cll2 > cll1
    assert cll2 >= cll2
    # slicing lists
    with pytest.raises(IndexError):
        cll1[:-1] == cll2[:-1]
    with pytest.raises(IndexError):
        cll1[-1:] != cll2[-1:]
    with pytest.raises(IndexError):
        cll1[:1] < cll2
    with pytest.raises(IndexError):
        cll1[:2] <= cll2
    with pytest.raises(IndexError):
        assert cll1[1:] < cll2
    with pytest.raises(IndexError):
        assert cll1[1:] <= cll2
    # if the other one isn't a circular linked list
    actual_list = [1, "2", 5.14]
    with pytest.raises(TypeError):
        assert cll1 == actual_list
    with pytest.raises(TypeError):
        assert cll1 != actual_list
    with pytest.raises(TypeError):
        assert cll1 < actual_list
    with pytest.raises(TypeError):
        assert cll1 <= actual_list
    with pytest.raises(TypeError):
        assert cll2 > actual_list
    with pytest.raises(TypeError):
        assert cll2 >= actual_list


def test_rotate():
    # rotate when inplace = False
    cll = CircularLinkedList([1, 2, 3, 4, 5, 6])
    rotated = cll.rotate_right(1, inplace=False)
    assert rotated.to_list() == [6, 1, 2, 3, 4, 5]
    assert isinstance(rotated._head, Node)
    assert rotated._head.get_data() == 6
    assert rotated[4] == 4
    rotated = cll.rotate_left(3, inplace=False)
    assert isinstance(rotated._head, Node)
    assert rotated.to_list() == [4, 5, 6, 1, 2, 3]
    assert rotated._head.get_data() == 4
    with pytest.raises(IndexError):
        rotated[-1] == 3
    assert cll.to_list() == [1, 2, 3, 4, 5, 6]
    # rotate when inplace = True
    cll.rotate_right(1)
    assert cll.to_list() == [6, 1, 2, 3, 4, 5]
    assert isinstance(cll._head, Node)
    assert cll._head.get_data() == 6
    cll.rotate_left(3)
    assert cll.to_list() == [3, 4, 5, 6, 1, 2]
    assert cll._head.get_data() == 3
    assert isinstance(cll._head, Node)


def test_extend_method():
    lst = get_list()
    # two linked lists are empty
    cll1 = CircularLinkedList()
    cll1.extend(CircularLinkedList())
    assert cll1 == CircularLinkedList()
    # one linked list is empty
    cll1 = CircularLinkedList([])
    cll2 = CircularLinkedList(lst)
    cll1.extend(cll2)
    assert cll1 == cll2
    assert len(cll1) == len(lst)
    cll2.extend(cll1)
    assert len(cll2) == 2 * len(lst)
    # two linked lists are NOT empty
    cll1 = CircularLinkedList(lst)
    cll2 = CircularLinkedList(lst)
    cll2.extend(cll1)
    assert cll1.to_list() == lst
    assert cll2.to_list() == lst + lst
    assert len(cll2) == 2 * len(lst)


def test_split_method():
    lst = get_list(length=100)
    cll = CircularLinkedList(lst)
    for i in range(len(lst)):
        # test left list
        left_list, right_list = cll.split(i)
        assert isinstance(left_list, LinkedList)
        assert left_list.to_list() == lst[:i]
        assert left_list.copy().to_list() == lst[:i]
        assert left_list.reverse().to_list() == lst[:i][::-1]
        # test right list
        assert isinstance(right_list, CircularLinkedList)
        assert right_list.to_list() == lst[i:]
        assert right_list.copy().to_list() == lst[i:]
        assert right_list.reverse().to_list() == lst[i:][::-1]
    cll.add_front(0)
    cll.add_end("apple")
    assert cll._length == len(cll) == len(lst) + 2
    assert cll.to_list() == [0] + lst + ["apple"]
