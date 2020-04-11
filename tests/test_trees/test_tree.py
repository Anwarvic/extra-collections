import pytest
from tests import *
from extra.trees.tree import TreeNode, Tree


def test_treenode():
    with pytest.raises(ValueError): TreeNode(None)
    with pytest.raises(ValueError): TreeNode('')
    with pytest.raises(ValueError): TreeNode('      ')
    with pytest.raises(ValueError): TreeNode('\t\n')
    with pytest.raises(ValueError): TreeNode(TreeNode(get_value()))
    # the following shouldn't raise anything
    for val in [get_int(), get_float(), get_string(), get_list()]:
        node = TreeNode(val)
        assert node.get_data() == val
        assert node.get_children() == []


def test_empty_tree():
    pass


def test_tree_with_known_values():
    # create Simpsons Family tree
    root = TreeNode('TheSimpsons')
    # homer-side
    abraham = TreeNode('Abraham + Mona')
    herb = TreeNode('Herb')
    homer = TreeNode('Homer')
    abraham.children = [herb, homer]
    # marge-side
    jackie = TreeNode('Clancy + Jackie')
    marge = TreeNode('Marge')
    patty = TreeNode('Patty')
    selma = TreeNode('Selma')
    ling = TreeNode('Ling')
    selma.children = [ling]
    jackie.children = [marge, patty, selma]
    # homer-marge children
    bart = TreeNode('Bart')
    lisa = TreeNode('Lisa')
    maggie = TreeNode('Maggie')
    homer.children = [bart, lisa, maggie]
    marge.children = homer.children
    # set root
    root.children = [abraham, jackie]
    t = Tree()
    t._root = root
    # test tree
    assert not t.is_empty()
    assert len(t) == 15
    assert t.get_depth() == t.get_height() == 3
    assert t.count_leaf_nodes() == 9
    assert t.to_list() == \
        ['TheSimpsons', 'Abraham + Mona', 'Clancy + Jackie', 'Herb', 'Homer',
        'Marge', 'Patty', 'Selma', 'Bart', 'Lisa', 'Maggie', 'Bart', 'Lisa',
        'Maggie', 'Ling']
    assert t.get_nodes() == \
        [['TheSimpsons'],
        ['Abraham + Mona', 'Clancy + Jackie'],
        ['Herb', 'Homer', 'Marge', 'Patty', 'Selma'],
        ['Bart', 'Lisa', 'Maggie', 'Bart', 'Lisa', 'Maggie', 'Ling']]
    # clear
    t.clear()
    assert t.is_empty()
    assert len(t) == 0
    assert t.get_depth() == t.get_height() == 0
    assert t.count_leaf_nodes() == 0
    assert t.to_list() == []
    with pytest.raises(IndexError): [i for i in t]


def test_invalid_path():
    val = get_string()
    t = Tree.from_path(val)
    assert str(t) == str(val)
    assert len(t) == 1
    assert t.get_depth() == t.get_height() == 0
    assert t.count_leaf_nodes() == 1
    assert t.to_list() == [val]
    assert [i for i in t] == [val]
    # clear
    t.clear()
    assert t.is_empty()
    assert len(t) == 0
    assert t.get_depth() == t.get_height() == 0
    assert t.count_leaf_nodes() == 0
    assert t.to_list() == []
    with pytest.raises(IndexError): [i for i in t]