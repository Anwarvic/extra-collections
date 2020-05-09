import pytest
from tests import *
from extra.trees.suffix_trie import SuffixTrie



def test_lcs():
    st = SuffixTrie("ABABABA")
    assert st.get_lcs() == ["ABABA"]

    st = SuffixTrie("banana")
    assert st.get_lcs() == ["ana"]

    st = SuffixTrie("PAPERSFORPAPERS")
    assert st.get_lcs() == ["PAPERS"]

    st = SuffixTrie("AAAAAAAAAA")
    assert st.get_lcs() == ["AAAAAAAAA"]

    st = SuffixTrie("ABCDEFG")
    assert st.get_lcs() == [""]

    st = SuffixTrie("ATCGATCGA")
    assert st.get_lcs() == ["ATCGA"]

    st = SuffixTrie("abcpqrabpqpq")
    assert sorted(st.get_lcs()) == ["ab", "pq"]


def test_count_pattern_occurrence():
    # in case of: banana
    st = SuffixTrie("banana")
    assert st.count_pattern_occurrences("bi") == 0
    assert st.count_pattern_occurrences("b") == 1
    assert st.count_pattern_occurrences("a") == 3
    assert st.count_pattern_occurrences("an") == 2
    assert st.count_pattern_occurrences("ana") == 2
    assert st.count_pattern_occurrences("anana") == 1
    assert st.count_pattern_occurrences("banana") == 1
    assert st.count_pattern_occurrences("ba") == 1
    assert st.count_pattern_occurrences("ban") == 1
    assert st.count_pattern_occurrences("bann") == 0
    assert st.count_pattern_occurrences("bananab") == 0
    