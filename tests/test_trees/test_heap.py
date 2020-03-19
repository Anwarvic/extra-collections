import pytest
from tests import *
from extra.trees._heap import Heap
from extra.trees.heap import MinHeap, MaxHeap



def test_heap_node():
    pass


def test_creating_heap():
    with pytest.raises(TypeError):
        _ = Heap()


def test_empty_min_heap():
    # create it from constructor
    heap = MinHeap()
    assert len(heap) == 0
    assert heap.is_empty()
    assert str(heap) == "/ \\"
    assert heap.to_list() == []
    assert get_float() not in heap
    assert get_int() not in heap
    # create it from heapify
    heap = MinHeap.heapify([])
    assert len(heap) == 0
    assert heap.is_empty()
    assert str(heap) == "/ \\"
    assert heap.to_list() == []
    assert get_float() not in heap
    assert get_int() not in heap
    # create it from clear() method
    heap = MinHeap(10)
    heap.clear()
    assert len(heap) == 0
    assert heap.is_empty()
    assert str(heap) == "/ \\"
    assert heap.to_list() == []
    assert get_float() not in heap
    assert get_int() not in heap

    

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
        "1" in heap
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