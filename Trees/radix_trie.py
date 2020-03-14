from trie import TrieNode, Trie



#helper function
def find_last_common_idx(word1, word2):
    idx = 0
    while(idx < len(word1)):
        if idx < len(word2) and word1[idx] == word2[idx]:
            idx += 1
        else:
            break
    return idx




class RadixTrie(Trie):
   
    ############################## INSERTION ##############################
    def insert(self, word):
        assert type(word) == str, "You can insert String objects only!!"
        assert len(word) > 0, "You can't insert any empty String!!"
        # insert it
        curr_node = self.root
        while(word):
            ch = word[0]
            child = curr_node.get_child(ch)
            if not child:
                new_node = TrieNode(word)
                new_node.is_word = True
                curr_node.set_child(word[0], new_node)
                return
            else:
                child_data = child.get_data()
                # child has exactly the given word
                if child_data == word:
                    child.is_word = True
                    return
                idx = find_last_common_idx(child_data, word)
                # child has part of the given word as a prefix
                if idx <= len(word) and idx != len(child_data):
                    # split child
                    new_node = TrieNode(child_data[:idx])
                    child.data = child_data[idx:]
                    new_node.set_child(child_data[idx], child)
                    # connect new_node to curr_node
                    curr_node.set_child(child_data[0], new_node)
                    child = new_node
                curr_node = child
                word = word[idx:]
                if word == "":
                    curr_node.is_word = True


    ############################## REMOVE ##############################
    def remove(self, word):
        assert type(word) == str, "You can remove String objects only!!"
        # search for the word
        start_node = self.root
        while(word):
            ch = word[0]
            child = start_node.get_child(ch)
            if not child:
                return
            else:
                child_data = child.get_data()
                if child_data == word[:len(child_data)]:
                    start_node = child
                    word = word[len(child_data):]
                else:
                    return
                
        # if word is found, clear it
        if start_node.is_word:
            start_node.is_word = False
        while(not start_node.is_word and start_node.has_no_children()):
            ch = start_node.get_data()[0]
            parent = start_node.get_parent()
            del parent.children[ch]
            start_node = parent


    ######################### AUTO-COMPLETION #########################
    def __get_candidates(self, start_node, prefix):
        output = []
        new_prefix = prefix.copy()
        new_prefix += start_node.get_data()
        if start_node.is_word:
            output.append("".join(new_prefix))
        # iterate over children
        for child in start_node.get_children():
            output.extend( self.__get_candidates(child, new_prefix) )
        return output
    
    def auto_complete(self, prefix=''):
        assert type(prefix) == str, "A character-sequence is expected!!"
        start_node = self.root
        # parse the prefix
        new_perfix = []
        while(prefix):
            ch = prefix[0]
            child = start_node.get_child(ch)
            if not child:
                return []
            else:
                start_node =  child
                child_data = child.get_data()
                if len(prefix) <= len(child_data):
                    if child_data[:len(prefix)] == prefix:
                        prefix = ''
                        new_perfix.append(child_data)
                    else:
                        return []
                else:
                    if prefix[:len(child_data)] == child_data:
                        prefix = prefix[len(child_data):]
                        new_perfix.append(child_data)
                    else:
                        new_perfix.append(ch)
                        prefix = prefix[1:]
        
        candidates = []
        curr_node = start_node
        prefix = "".join(new_perfix)
        # check the current node
        if curr_node.is_word:
            candidates.append(prefix)
        # get candidates starting from given prefix
        for child in curr_node.get_children():
            candidates.extend(self.__get_candidates(child, [prefix]))
        return candidates







if __name__ == "__main__":
    # src: https://en.wikipedia.org/wiki/Radix_tree?oldformat=true
    rt = RadixTrie()
    rt.insert("romane")
    rt.insert("romanus")
    rt.insert("romulus")
    rt.insert("rubens")
    rt.insert("ruber")
    rt.insert("rubicon")
    rt.insert("rubicundus")
    print(rt)
    print('='*50)

    rt = RadixTrie()
    rt.insert("shear")
    rt.insert("she")
    rt.insert("shepard")
    rt.insert("shepard")
    rt.insert('s')
    print(rt)
    print('s' in rt)
    print("shea" in rt)
    print(rt.auto_complete(""))     # ['s', 'she', 'shear', 'shepard']
    print(rt.auto_complete("a"))    # []
    print(rt.auto_complete("s"))    # ['s', 'she', 'shear', 'shepard']
    print(rt.auto_complete("sh"))   # ['she', 'shear', 'shepard']
    print(rt.auto_complete("sha"))  # []
    print(rt.auto_complete("she"))  # ['she', 'shear', 'shepard']
    print(rt.auto_complete("shee")) # []
    print(rt.auto_complete("shea")) # ['shear']
    print(rt.auto_complete("sheaa"))# []
    print('='*50)

    rt = RadixTrie()
    rt.insert("test")
    rt.insert("toaster")
    rt.insert("toasting")
    rt.insert("slow")
    rt.insert("slowly")
    rt.insert("slowlier")
    rt.insert("toast")
    rt.insert("slower")
    print(rt)
    print("slowlie" in rt)
    rt.remove("test")  # remove 'est' from tree
    rt.remove("slow") # remove is_word
    rt.remove("slowl") # do nothin'
    print(rt)
    print('='*50)
    print(rt.has_substring("slowy"))
    
    # # sanity checks
    # rt = RadixTrie()
    # print(rt.find(''))
    # print(rt.find(2)) #throws error


