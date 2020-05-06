import pytest
from tests import *
from extra.trees.suffix_trie import SuffixTrie



def test_lcs():
    st = SuffixTrie("ABABABA")
    assert st.get_lcs() == ["ABABA"]

    st = SuffixTrie("banana")
    assert st.get_lcs() == ["ana"]

    st = SuffixTrie("GEEKSFORGEEKS")
    assert st.get_lcs() == ["GEEKS"]

    st = SuffixTrie("AAAAAAAAAA")
    assert st.get_lcs() == ["AAAAAAAAA"]

    st = SuffixTrie("ABCDEFG")
    assert st.get_lcs() == [""]

    st = SuffixTrie("ATCGATCGA")
    assert st.get_lcs() == ["ATCGA"]

    st = SuffixTrie("abcpqrabpqpq")
    assert sorted(st.get_lcs()) == ["ab", "pq"]

    