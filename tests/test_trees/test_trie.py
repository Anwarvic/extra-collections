import pytest
from tests import *
from extra.trees.trie import TrieNode, Trie




def test_trienode():
    node = TrieNode('a')
    assert node.get_data() == 'a'
    assert node.get_parent() is None
    assert list(node.get_characters()) == []
    assert node.get_children() == []
    with pytest.raises(TypeError): TrieNode(None)
    with pytest.raises(TypeError): TrieNode(get_int())
    with pytest.raises(TypeError): TrieNode(get_float())
    with pytest.raises(TypeError): TrieNode(get_list())
    # with pytest.raises(AssertionError):
    #     TrieNode("apple")
    #     TrieNode(get_string())


def test_empty_trie():
    t = Trie()
    t.clear()
    assert len(t) == 1
    assert isinstance(t._root, TrieNode)
    assert t._root.get_data() == "ROOT"
    assert '' not in t
    assert get_string() not in t
    assert t.has_prefix('')
    assert t.auto_complete() == t.auto_complete('') \
        == t.auto_complete(get_string()) == []
    with pytest.raises(ValueError): t.insert(None)
    with pytest.raises(TypeError): t.insert(get_int())
    with pytest.warns(UserWarning): t.remove(None)
    with pytest.warns(UserWarning): t.remove(get_list())
    assert get_float() not in t
    assert None not in t
    assert not t.has_prefix(None)
    assert not t.has_prefix(get_int())
    with pytest.raises(ValueError): t.auto_complete(None)
    with pytest.raises(TypeError): t.auto_complete(get_list())
    with pytest.raises(ValueError): t.insert('')
    with pytest.raises(ValueError): t.insert(' \n\t  ')
    with pytest.raises(ValueError): t.remove('')
    with pytest.raises(ValueError): t.remove(' \n\t  ')


def test_trie_similar_words():
    t = Trie()
    t.insert("tre")
    t.insert("trees")
    t.insert("treed")
    t.remove("trees")
    t.remove("tre")
    assert len(t) == 6
    assert t.auto_complete("t") == ['treed']


def test_trie_many_words():
    t = Trie()
    t.insert('car')
    t.insert('card')
    t.insert('cards')
    t.insert('cot')
    t.insert('cots')
    t.insert('trie')
    t.insert('tried')
    t.insert('tries')
    t.insert('try')
    assert t.has_prefix('ca')
    assert len(t) == 16
    # explort Trie
    assert t._root.get_data() == "ROOT"
    assert t._root.get_child('t').get_data() == 't'
    assert list(t._root.get_child('c').get_characters()) == ['a', 'o']
    # test find() and get_cadidates()
    assert 'cards' in t
    assert 'c' not in t
    assert t.auto_complete() == \
        ['car', 'card', 'cards', 'cot', 'cots', 'trie', 'tried', 'tries', 'try']
    assert t.auto_complete('c') == ['car', 'card', 'cards', 'cot', 'cots']
    assert t.auto_complete('tri') == ['trie', 'tried', 'tries']
    assert t.auto_complete('caa') == []


