import pytest
from tests import (
    get_string,
    get_value,
    get_list,
    get_float,
    get_int,
)
from extra.trees.tree import TreeNode, Tree


def test_treenode():
    with pytest.raises(ValueError):
        TreeNode(None)
    with pytest.raises(TypeError):
        TreeNode(TreeNode(get_value()))
    # the following shouldn't raise anything
    TreeNode("")
    TreeNode("      ")
    assert TreeNode("\nap\nple\n").get_data() == "\\nap\\nple\\n"
    for val in [get_int(), get_float(), get_string(), get_list()]:
        node = TreeNode(val)
        assert node.get_data() == val
        assert node.get_children() == []
    with pytest.raises(TypeError):
        TreeNode(get_value()).set_child(get_value)
    with pytest.raises(TypeError):
        TreeNode(get_value()).set_children(get_value)


def test_empty_tree():
    t = Tree()
    with pytest.raises(TypeError):
        Tree(get_value())
    with pytest.raises(TypeError):
        Tree(None)
    assert t.is_empty()
    assert len(t) == 0
    assert t.get_depth() == t.get_height() == 0
    assert t.count_leaf_nodes() == 0
    assert t.to_list() == []
    assert t.get_nodes_per_level() == []


def test_tree_with_known_values():
    # create Simpsons Family tree
    root = TreeNode("TheSimpsons")
    # homer-side
    abraham = TreeNode("Abraham + Mona")
    herb = TreeNode("Herb")
    homer = TreeNode("Homer")
    abraham.set_children([herb, homer])
    # marge-side
    jackie = TreeNode("Clancy + Jackie")
    marge = TreeNode("Marge")
    patty = TreeNode("Patty")
    selma = TreeNode("Selma")
    ling = TreeNode("Ling")
    selma.set_children([ling])
    jackie.set_children([marge, patty, selma])
    # homer-marge children
    bart = TreeNode("Bart")
    lisa = TreeNode("Lisa")
    maggie = TreeNode("Maggie")
    homer.set_children([bart, lisa, maggie])
    marge.set_children(homer.get_children())
    # set root
    root.set_children([abraham, jackie])
    t = Tree()
    t._root = root
    # test tree
    assert not t.is_empty()
    assert len(t) == 15
    assert t.get_depth() == 0
    assert t.get_height() == 3
    assert t.count_leaf_nodes() == 9
    assert t.to_list() == [
        "TheSimpsons",
        "Abraham + Mona",
        "Clancy + Jackie",
        "Herb",
        "Homer",
        "Marge",
        "Patty",
        "Selma",
        "Bart",
        "Lisa",
        "Maggie",
        "Bart",
        "Lisa",
        "Maggie",
        "Ling",
    ]
    assert t.get_nodes_per_level() == [
        ["TheSimpsons"],
        ["Abraham + Mona", "Clancy + Jackie"],
        ["Herb", "Homer", "Marge", "Patty", "Selma"],
        ["Bart", "Lisa", "Maggie", "Bart", "Lisa", "Maggie", "Ling"],
    ]
    # clear
    t.clear()
    assert t.is_empty()
    assert len(t) == 0
    assert t.get_depth() == t.get_height() == 0
    assert t.count_leaf_nodes() == 0
    assert t.to_list() == []


def test_invalid_path():
    val = get_string()
    with pytest.raises(ValueError):
        Tree.from_path(val)
