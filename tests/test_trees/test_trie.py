import pytest
from extra.trees.trie import TrieNode, Trie




def test_trienode():
    pass


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
    assert t.root.get_data() == "ROOT"
    assert t.root.get_child('t').get_data() == 't'
    assert list(t.root.get_child('c').get_characters()) == ['a', 'o']
    # test find() and get_cadidates()
    assert 'cards' in t
    assert 'c' not in t
    assert t.auto_complete() == \
        ['car', 'card', 'cards', 'cot', 'cots', 'trie', 'tried', 'tries', 'try']
    assert t.auto_complete('c') == ['car', 'card', 'cards', 'cot', 'cots']
    assert t.auto_complete('tri') == ['trie', 'tried', 'tries']
    assert t.auto_complete('caa') == []