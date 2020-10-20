import pytest

from extra.trees._heap import Heap, HeapNode
from extra.trees.min_heap import MinHeap
from extra.trees.max_heap import MaxHeap


def test_heap_node(helper):
    with pytest.raises(TypeError):
        HeapNode(None)
    with pytest.raises(TypeError):
        HeapNode(helper.get_string())
    with pytest.raises(TypeError):
        HeapNode(helper.get_list())
    val = helper.get_float()
    node = HeapNode(val)
    assert node.get_data() == val
    assert node.get_left() == node.get_right() is None
    assert node.get_children() == []


def test_creating_heap(helper):
    with pytest.raises(TypeError):
        Heap()
    with pytest.raises(TypeError):
        Heap.heapify(helper.get_list())


def test_empty_heap(helper, heap=MinHeap()):
    # create it from constructor
    assert len(heap) == 0
    assert heap.is_empty()
    assert str(heap) == "/ \\"
    assert heap.to_list() == []
    assert helper.get_float() not in heap
    assert helper.get_int() not in heap
    helper.get_list() in heap
    helper.get_string() in heap
    with pytest.raises(IndexError):
        heap.get_min()
    with pytest.raises(IndexError):
        heap.get_max()
    with pytest.raises(ValueError):
        heap.insert(None)
    with pytest.raises(TypeError):
        heap.insert(helper.get_string())
    with pytest.raises(TypeError):
        heap.insert(helper.get_list())
    # should raise warnings
    with pytest.warns(UserWarning):
        heap.remove(helper.get_int())
    with pytest.warns(UserWarning):
        heap.remove(helper.get_float())
    with pytest.warns(UserWarning):
        heap.remove(helper.get_string())
    with pytest.warns(UserWarning):
        heap.remove(helper.get_list())


def test_empty_max_heap(helper, heap=MaxHeap()):
    test_empty_heap(helper, heap)


def test_empty_heap_using_heapify(helper):
    # test MinHeap
    heap = MinHeap.heapify([])
    test_empty_heap(helper, heap)
    # test MaxHeap
    heap = MaxHeap.heapify([])
    test_empty_heap(helper, heap)


def test_empty_heap_after_clearing(helper):
    # test MaxHeap
    heap = MinHeap()
    heap.insert(10)
    heap.clear()
    test_empty_heap(helper, heap)
    # test MaxHeap
    heap = MaxHeap()
    heap.insert(10)
    heap.clear()
    test_empty_heap(helper, heap)


def test_heap_with_same_value(helper):
    for HeapClass in [MinHeap, MaxHeap]:
        val = helper.get_float()
        length = helper.get_pos_int()
        lst = [val] * length
        heap = HeapClass.heapify(lst)
        if HeapClass == MinHeap:
            assert helper.verify_min_heap(heap._transform()._root)
        elif HeapClass == MaxHeap:
            assert helper.verify_max_heap(heap._transform()._root)
        assert not heap.is_empty()
        assert heap.to_list() == lst
        assert len(heap) == len(lst)
        assert heap.get_max() == val
        assert heap.get_min() == val
        for node in heap:
            assert node == val
        for _ in range(length):
            heap.remove(val)
        # test_empty_heap(heap)


def test_heapify_of_min_heap_small_example(helper):
    lst = [6, 2, 7, 1]
    heap = MinHeap.heapify(lst)
    assert helper.verify_min_heap(heap._transform()._root)
    assert not heap.is_empty()
    assert len(heap) == len(lst)
    assert heap.get_max() == max(lst)
    assert heap.get_min() == min(lst)
    for num in lst:
        assert num in heap
    assert 19 not in heap
    assert 0 not in heap
    assert helper.get_list() not in heap
    assert helper.get_string() not in heap


def test_heapify_of_min_heap_big_example(helper):
    lst = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190]
    heap = MinHeap.heapify(lst)
    assert len(heap) == len(lst)
    assert helper.verify_min_heap(heap._transform()._root)
    assert heap.get_max() == max(lst)
    assert heap.get_min() == min(lst)
    for node, value in zip(heap, lst):
        assert node == value
    for num in lst:
        assert num in heap
    assert helper.get_list() not in heap
    assert helper.get_string() not in heap


def test_insert_remove_min_heap(helper):
    heap = MinHeap()
    heap.insert(35)
    heap.insert(33)
    heap.insert(42)
    heap.insert(10)
    heap.insert(14)
    heap.insert(19)
    heap.insert(27)
    heap.insert(44)
    heap.insert(26)
    heap.insert(31)
    assert len(heap) == 10
    assert not heap.is_empty()
    assert heap.get_min() == 10
    assert heap.get_max() == 44
    assert helper.verify_min_heap(heap._transform()._root)
    with pytest.warns(UserWarning):
        heap.remove(0)
    assert len(heap) == 10
    heap.remove(10)
    assert len(heap) == 9
    assert heap.get_min() == 14
    assert heap.get_max() == 44
    assert helper.verify_min_heap(heap._transform()._root)
    heap.remove(44)
    assert len(heap) == 8
    assert heap.get_min() == 14
    assert heap.get_max() == 42
    assert helper.verify_min_heap(heap._transform()._root)


def test_heapify_of_max_heap_small_example(helper):
    lst = [6, 2, 7, 1]
    heap = MaxHeap.heapify(lst)
    assert not heap.is_empty()
    assert helper.verify_max_heap(heap._transform()._root)
    assert len(heap) == len(lst)
    assert heap.get_max() == max(lst)
    assert heap.get_min() == min(lst)
    for node, value in zip(heap, [7, 2, 6, 1]):
        assert node == value
    for num in lst:
        assert num in heap
    assert 19 not in heap
    assert 0 not in heap
    assert helper.get_list() not in heap
    assert helper.get_string() not in heap


def test_heapify_of_max_heap_big_example(helper):
    lst = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190]
    heap = MaxHeap.heapify(lst)
    assert helper.verify_max_heap(heap._transform()._root)
    assert len(heap) == len(lst)
    assert heap.get_max() == max(lst)
    assert heap.get_min() == min(lst)
    for node, value in zip(
        heap, [190, 15, 102, 8, 13, 17, 100, 1, 5, 4, 9, 3, 10, 6, 90]
    ):
        assert node == value
    for num in lst:
        assert num in heap
    assert helper.get_list() not in heap
    assert helper.get_string() not in heap


def test_insert_remove_max_heap(helper):
    heap = MaxHeap()
    heap.insert(35)
    heap.insert(33)
    heap.insert(42)
    heap.insert(10)
    heap.insert(14)
    heap.insert(19)
    heap.insert(27)
    heap.insert(44)
    heap.insert(26)
    heap.insert(31)
    assert helper.verify_max_heap(heap._transform()._root)
    assert len(heap) == 10
    assert not heap.is_empty()
    assert heap.get_min() == 10
    assert heap.get_max() == 44
    with pytest.warns(UserWarning):
        heap.remove(0)
    assert len(heap) == 10
    heap.remove(10)
    assert len(heap) == 9
    assert heap.get_min() == 14
    assert heap.get_max() == 44
    assert helper.verify_max_heap(heap._transform()._root)
    heap.remove(44)
    assert len(heap) == 8
    assert heap.get_min() == 14
    assert heap.get_max() == 42
    assert helper.verify_max_heap(heap._transform()._root)
