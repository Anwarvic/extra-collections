from radix_trie import RadixTrie
from trie import Trie



class SuffixTrie:

    def __init__(self, word):
        assert type(word) == str, "The initial value must be a string!!"
        assert len(word) > 0, "An empty string can't be used!!"
        # Ukkonen's algorithm
        self.rt = RadixTrie()
        for idx in range(len(word)):
            self.rt.insert(word[idx:])


    def __repr__(self):
        return str(self.rt)


    def __len__(self):
        return len(self.rt)




if __name__ == "__main__":
    # st = SuffixTrie("banana")
    # print(st)
    # print(st.find('nan'))

    st = SuffixTrie("minimize")
    st = SuffixTrie("ATCGATCGA")
    print(st)
    print("Total Nodes:", len(st))
