import pytest
from tests import *
from extra.lists.stack import Stack



def test_creating_stack():
    # empty stack
    s = Stack()
    assert s.max_capacity == float("inf")
    assert s.container == []
    assert len(s) == 0
    assert s.pop() == None
    with pytest.raises(IndexError):
        s.peek()
    


