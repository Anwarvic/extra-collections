import pytest
from extra.trees.suffix_trie import SuffixTrie


def test_lcs():
    st = SuffixTrie("ABABABA")
    assert st.get_longest_common_substring() == ["ABABA"]

    st = SuffixTrie("banana")
    assert st.get_longest_common_substring() == ["ana"]

    st = SuffixTrie("PAPERSFORPAPERS")
    assert st.get_longest_common_substring() == ["PAPERS"]

    st = SuffixTrie("AAAAAAAAAA")
    assert st.get_longest_common_substring() == ["AAAAAAAAA"]

    st = SuffixTrie("ABCDEFG")
    assert st.get_longest_common_substring() == [""]

    st = SuffixTrie("ATCGATCGA")
    assert st.get_longest_common_substring() == ["ATCGA"]

    st = SuffixTrie("abcpqrabpqpq")
    assert sorted(st.get_longest_common_substring()) == ["ab", "pq"]


def test_lowest_common_ancestor():
    # in case of: ABABABA
    st = SuffixTrie("ABABABA")
    assert st.get_lowest_common_ancestor(0, 1) == ""
    assert st.get_lowest_common_ancestor(1, 3) == "BABA"
    assert st.get_lowest_common_ancestor(1, 5) == "BA"
    assert st.get_lowest_common_ancestor(2, 4) == "ABA"
    assert st.get_lowest_common_ancestor(1, 6) == ""
    assert st.get_lowest_common_ancestor(6, 0) == "A"
    with pytest.raises(TypeError):
        st.get_lowest_common_ancestor("1", "6")
    with pytest.raises(ValueError):
        st.get_lowest_common_ancestor(-1, 100)

    # in case of: banana
    st = SuffixTrie("banana")
    assert st.get_lowest_common_ancestor(0, 1) == ""
    assert st.get_lowest_common_ancestor(1, 3) == "ana"
    assert st.get_lowest_common_ancestor(1, 5) == "a"
    assert st.get_lowest_common_ancestor(2, 4) == "na"
    assert st.get_lowest_common_ancestor(1, 6) == ""
    assert st.get_lowest_common_ancestor(5, 2) == ""

    # in case of: PAPERSFORPAPERS
    st = SuffixTrie("PAPERSFORPAPERS")
    assert st.get_lowest_common_ancestor(2, 9) == "P"
    assert st.get_lowest_common_ancestor(12, 3) == "ERS"
    assert st.get_lowest_common_ancestor(12, 12) == "ERS"
    assert st.get_lowest_common_ancestor(13, 4) == "RS"
    assert st.get_lowest_common_ancestor(0, 9) == "PAPERS"
    assert st.get_lowest_common_ancestor(1, 6) == ""
    assert st.get_lowest_common_ancestor(2, 11) == "PERS"

    # in case of: ATCGATCGA
    st = SuffixTrie("ATCGATCGA")
    assert st.get_lowest_common_ancestor(1, 5) == "TCGA"
    assert st.get_lowest_common_ancestor(0, 8) == "A"
    assert st.get_lowest_common_ancestor(0, 2) == ""
    assert st.get_lowest_common_ancestor(2, 6) == "CGA"
    assert st.get_lowest_common_ancestor(1, 6) == ""
    assert st.get_lowest_common_ancestor(0, 4) == "ATCGA"


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


# def test_get_longest_palindrome():
#     assert SuffixTrie("banana").get_longest_palindrome() == "anana"
#     assert SuffixTrie("nonsense").get_longest_palindrome() == "non"
#     assert (
#         SuffixTrie("1234aba4321").get_longest_palindrome() == "1234aba4321"
#     )
#     assert SuffixTrie("xababayz").get_longest_palindrome() == "ababa"
#     assert SuffixTrie("abacdfgdcaba").get_longest_palindrome() == "aba"
#     assert SuffixTrie("pqrqpabcdfgdcba").get_longest_palindrome() == "pqrqp"
#     assert SuffixTrie("pqqpabcdfghfdcba").get_longest_palindrome() == "pqqp"
#     assert SuffixTrie("cabbaabb").get_longest_palindrome() == "bbaabb"
#     assert (
#         SuffixTrie("forgeeksskeegfor").get_longest_palindrome()
#         == "geeksskeeg"
#     )
#     assert SuffixTrie("abcde").get_longest_palindrome() == "a"
#     assert SuffixTrie("abcdae").get_longest_palindrome() == "a"
#     assert SuffixTrie("abacd").get_longest_palindrome() == "aba"
#     assert SuffixTrie("abcdc").get_longest_palindrome() == "cdc"
#     assert SuffixTrie("abacdfgdcaba").get_longest_palindrome() == "aba"
#     assert SuffixTrie("xyabacdfgdcaba").get_longest_palindrome() == "aba"
#     assert SuffixTrie("xababayz").get_longest_palindrome() == "ababa"
#     assert SuffixTrie("xabax").get_longest_palindrome() == "xabax"


def test_suffix_array():
    st = SuffixTrie("banana")
    assert st.to_suffix_array() == [6, 5, 3, 1, 0, 4, 2]
