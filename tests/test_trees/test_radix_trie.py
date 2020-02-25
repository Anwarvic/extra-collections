import pytest
from tests import *
from extra.trees.radix_trie import RadixTrie



def test_empty_radix_trie():
    pass


def test_radix_trie_with_simple_example():
    rt = RadixTrie()
    rt.insert("shear")
    rt.insert("she")
    rt.insert("shears")
    rt.insert("shepard")
    rt.insert("shepard")
    rt.remove('s') #shouldn't raise any errors
    assert len(rt) == 5
    assert 'she' in rt
    assert "sha" not in rt
    assert "shea" not in rt
    assert rt.has_prefix('')
    assert rt.has_prefix("sh")
    assert rt.has_prefix("shea")
    assert not rt.has_prefix("shp")
    assert rt.auto_complete("") ==  ['she', 'shear', 'shears', 'shepard']
    assert rt.auto_complete("a") == []
    assert rt.auto_complete("s") == ['she', 'shear', 'shears', 'shepard']
    assert rt.auto_complete("sh") == ['she', 'shear', 'shears', 'shepard']
    assert rt.auto_complete("sha") == []
    assert rt.auto_complete("she") == ['she', 'shear', 'shears', 'shepard']
    assert rt.auto_complete("shee") == []
    assert rt.auto_complete("shea") == ["shear", "shears"]
    assert rt.auto_complete("shep") == ['shepard']
    assert rt.auto_complete("sheaa") == []
    assert rt.auto_complete("shearr") == []
    assert rt.auto_complete(get_string()) == []


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


def test_radix_with_multi_words():
    rt = RadixTrie()
    rt.insert("test")
    rt.insert("toaster")
    rt.insert("toasting")
    rt.insert("slow")
    rt.insert("slowly")
    rt.insert("slowlier")
    rt.insert("toast")
    rt.insert("slower")
    assert len(rt) == 11
    assert "slowlie" not in rt
    assert not rt.has_prefix("slowy")
    assert "slowl" not in rt
    assert rt.has_prefix("slowl")
    assert "slowly" in rt
    rt.remove("test")
    rt.remove("slow")
    rt.remove("slowl")
    assert len(rt) == 10
    assert 'slow' not in rt
    assert rt.has_prefix("slo")
    assert rt.has_prefix("s")
    assert not rt.has_prefix("sloww")
    assert rt.has_prefix("slow")
