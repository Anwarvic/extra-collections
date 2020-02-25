import pytest
from extra.trees.radix_trie import RadixTrie



def test_empty_radix_trie():
    pass


def test_radix_trie_with_simple_example():
    pass


def test_radix_trie_with_wiki_example():
    # src: https://en.wikipedia.org/wiki/Radix_tree?oldformat=true
    rt = RadixTrie()
    rt.insert("romane")
    rt.insert("romane")
    rt.insert("romanus")
    rt.insert("romulus")
    rt.insert("rubens")
    rt.insert("ruber")
    rt.insert("rubicon")
    rt.insert("rubicundus")
    assert len(rt) == 14


