import pytest
from tests import *
from extra.trees.tree import TreeNode, Tree


def test_treenode():
    with pytest.raises(TypeError):
        TreeNode(None)
    with pytest.raises(ValueError):
        TreeNode('')
        TreeNode('      ')
        TreeNode('\t\n')
    # the following shouldn't raise anything
    TreeNode(get_int())
    TreeNode(get_float())
    TreeNode(get_string())
    TreeNode(get_value())
    TreeNode(get_list())

