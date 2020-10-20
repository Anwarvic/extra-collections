import pytest
from tests import (
    get_string,
    get_list,
    get_float,
    get_int,
)
from extra.trees.radix_trie import TrieNode, RadixTrie


def test_empty_radix_trie():
    rt = RadixTrie()
    rt.clear()
    assert len(rt) == 1
    assert isinstance(rt._root, TrieNode)
    assert rt._root.get_data() == "ROOT"
    assert "" not in rt
    assert get_string() not in rt
    assert rt.has_prefix("")
    assert (
        rt.auto_complete()
        == rt.auto_complete("")
        == rt.auto_complete(get_string())
        == []
    )
    with pytest.raises(ValueError):
        rt.insert(None)
    with pytest.raises(TypeError):
        rt.insert(get_int())
    with pytest.warns(UserWarning):
        rt.remove(None)
    with pytest.warns(UserWarning):
        rt.remove(get_list())
    assert get_float() not in rt
    assert None not in rt
    assert not rt.has_prefix(None)
    assert not rt.has_prefix(get_int())
    with pytest.raises(ValueError):
        rt.auto_complete(None)
    with pytest.raises(TypeError):
        rt.auto_complete(get_list())
    with pytest.raises(ValueError):
        rt.insert("")
    with pytest.raises(ValueError):
        rt.insert(" \n\t  ")
    rt.remove("")  # do nothing
    rt.remove(" \n\t  ")  # do nothing


def test_radix_trie_with_simple_example():
    rt = RadixTrie()
    rt.insert("shear")
    rt.insert("she")
    rt.insert("shears")
    rt.insert("shepard")
    rt.insert("shepard")
    rt.remove("s")  # shouldn't raise any errors
    assert len(rt) == 5
    assert "she" in rt
    assert "sha" not in rt
    assert "shea" not in rt
    assert rt.has_prefix("")
    assert rt.has_prefix("sh")
    assert rt.has_prefix("shea")
    assert not rt.has_prefix("shp")
    assert rt.auto_complete("") == ["she", "shear", "shears", "shepard"]
    assert rt.auto_complete("a") == []
    assert rt.auto_complete("s") == ["she", "shear", "shears", "shepard"]
    assert rt.auto_complete("sh") == ["she", "shear", "shears", "shepard"]
    assert rt.auto_complete("sha") == []
    assert rt.auto_complete("she") == ["she", "shear", "shears", "shepard"]
    assert rt.auto_complete("shee") == []
    assert rt.auto_complete("shea") == ["shear", "shears"]
    assert rt.auto_complete("shep") == ["shepard"]
    assert rt.auto_complete("sheaa") == []
    assert rt.auto_complete("shearr") == []
    assert rt.auto_complete(get_string()) == []


def test_radix_trie_with_wiki_example():
    # src: https://en.wikipedia.org/wiki/Radix_tree?oldformat=true
    rt = RadixTrie()
    rt.insert("romane")
    rt.insert("romane")  # shouldn't raise anything
    rt.insert("romanus")
    rt.insert("romulus")
    rt.insert("rubens")
    rt.insert("ruber")
    rt.insert("rubicon")
    rt.insert("rubicundus")
    assert len(rt) == 14
    assert list(rt._root.get_characters()) == ["r"]
    assert "r" not in rt
    assert rt.has_prefix("r")
    assert "ruber" in rt
    assert "ruber " not in rt  # notice the space after `ruber`
    assert rt.has_prefix("ru")
    assert (
        rt.auto_complete()
        == rt.auto_complete("r")
        == ["romane", "romanus", "romulus", "rubens", "ruber", "rubicon",
            "rubicundus"]
    )
    assert (
        rt.auto_complete("ro") == ["romane", "romanus", "romulus"]
    )
    assert (
        rt.auto_complete("ru") == ["rubens", "ruber", "rubicon", "rubicundus"]
    )
    assert rt.auto_complete("romu") == ["romulus"]
    assert rt.auto_complete(get_string()) == []


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
    assert "slow" not in rt
    assert rt.has_prefix("slo")
    assert rt.has_prefix("s")
    assert not rt.has_prefix("sloww")
    assert rt.has_prefix("slow")
