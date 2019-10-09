from radix_trie import RadixTrie


class SuffixTrie(RadixTrie):
    pass



if __name__ == "__main__":
    st = SuffixTrie()
    st.insert("she")
    st.insert("shepard")
    print(st)