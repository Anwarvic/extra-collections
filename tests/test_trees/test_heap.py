import pytest
from tests import *
from extra.trees._heap import Heap, HeapNode
from extra.trees.heap import MinHeap, MaxHeap



def test_heap_node():
    with pytest.raises(TypeError):
        _ = HeapNode(None)
        _ = HeapNode(get_string())
        _ = HeapNode(get_list())
    val = get_float()
    node = HeapNode(val)
    assert node.get_data() == val
    assert node.get_left() == node.get_right() == None
    assert node.get_children() == []


def test_creating_heap():
    with pytest.raises(TypeError):
        _ = Heap()
        _ = Heap.heapify(get_list())


def test_empty_heap():
    # create it from constructor
    for Heap in [MinHeap, MaxHeap]:
        heap = Heap()
        assert len(heap) == 0
        assert heap.is_empty()
        assert str(heap) == "/ \\"
        assert heap.to_list() == []
        assert get_float() not in heap
        assert get_int() not in heap
        with pytest.raises(TypeError):
            get_list() in heap
            get_string() in heap
        with pytest.raises(IndexError):
            heap.get_min()
            heap.get_max()
        with pytest.raises(TypeError):
            heap.insert(None)
            heap.insert(get_string())
            heap.insert(get_list())
            heap.remove(get_string())
            heap.remove(get_list())
        #shouldn't raise anything
        heap.remove(get_int())
        heap.remove(get_float())


def test_empty_heap_using_heapify():
    # create it from heapify
    for Heap in [MinHeap, MaxHeap]:
        heap = Heap.heapify([])
        assert len(heap) == 0
        assert heap.is_empty()
        assert str(heap) == "/ \\"
        assert heap.to_list() == []
        assert get_float() not in heap
        assert get_int() not in heap
        with pytest.raises(IndexError):
            heap.get_min()
            heap.get_max()
        with pytest.raises(TypeError):
            heap.insert(None)
            heap.insert(get_string())
            heap.insert(get_list())
            heap.remove(get_string())
            heap.remove(get_list())
        #shouldn't raise anything
        heap.remove(get_int())
        heap.remove(get_float())


def test_empty_heap_after_clearing():
    # create it from clear() method
    for Heap in [MinHeap, MaxHeap]:
        heap = Heap(10)
        heap.clear()
        assert len(heap) == 0
        assert heap.is_empty()
        assert str(heap) == "/ \\"
        assert heap.to_list() == []
        assert get_float() not in heap
        assert get_int() not in heap
        with pytest.raises(IndexError):
            heap.get_min()
            heap.get_max()
        with pytest.raises(TypeError):
            heap.insert(None)
            heap.insert(get_string())
            heap.insert(get_list())
            heap.remove(get_string())
            heap.remove(get_list())
        #shouldn't raise anything
        heap.remove(get_int())
        heap.remove(get_float())



def test_heapify_of_min_heap_small_example():
    lst = [6, 2, 7, 1]
    heap = MinHeap.heapify(lst)
    assert heap.to_list() == [1, 2, 7, 6]
    assert len(heap) == len(lst)
    assert heap.get_max() == max(lst)
    assert heap.get_min() == min(lst)
    for node, value in zip(heap, [1, 2, 7, 6]):
        assert node.get_data() == value
    for num in lst:
        assert num in heap
    assert 19 not in heap
    assert 0 not in heap
    with pytest.raises(TypeError):
        get_list() in heap
        get_string() in heap


def test_heapify_of_min_heap_big_example():
    lst = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190]
    heap = MinHeap.heapify(lst)
    assert heap.to_list() == lst
    assert len(heap) == len(lst)
    assert heap.get_max() == max(lst)
    assert heap.get_min() == min(lst)
    for node, value in zip(heap, lst):
        assert node.get_data() == value
    for num in lst:
        assert num in heap
    with pytest.raises(TypeError):
        "1" in heap
        get_list() in heap
        get_string() in heap


def test_insert_remove_min_heap():
    pass