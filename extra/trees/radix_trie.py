# from trie import TrieNode, Trie
from extra.trees.trie import TrieNode, Trie




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
    def __name__(self):
        return "extra.RadixTrie()"
    
    
    ############################## INSERTION ##############################
    def insert(self, word):
        super()._validate_item(word, accept_empty_string=False)
        last_node, remaining_word = super()._follow_path(word)
        curr_node = last_node
        while(remaining_word):
            ch = remaining_word[0]
            child = curr_node.get_child(ch)
            child_data = child.get_data() if child else ''
            idx = find_last_common_idx(child_data, remaining_word)
            # couldn't find the remaining_word
            if idx == 0:
                new_node = TrieNode(remaining_word)
                curr_node.set_child(ch, new_node)
                remaining_word = ''
                self.nodes_count += 1
            # child is prefix of the remaining_word
            elif idx <= len(remaining_word) and idx != len(child_data):
                # split child
                new_node = TrieNode(child_data[:idx])
                child.data = child_data[idx:]
                new_node.set_child(child_data[idx], child)
                # connect new_node to curr_node
                curr_node.set_child(child_data[0], new_node)
                remaining_word = remaining_word[idx:]
                self.nodes_count += 1
            curr_node = new_node
        # mark current node as a word
        curr_node.is_word = True


    ######################### AUTO-COMPLETION #########################    
    def auto_complete(self, prefix=''):
        super()._validate_item(prefix)
        candidates = []
        last_node, remaining = super()._follow_path(prefix)
        # update prefix
        curr_node = last_node
        prefix = prefix[:-len(remaining)] if remaining else prefix
        if remaining:
            ch = remaining[0]
            child = curr_node.get_child(ch)
            child_data = child.get_data() if child else ''
            # couldn't find the remaining prefix
            if len(remaining) > len(child_data) or \
                child_data[:len(remaining)] != remaining:
                return candidates
            else:
                remaining = ''
                prefix += child_data
                curr_node = child
       
        # check the current node
        if curr_node.is_word:
            candidates.append(prefix)
        # get candidates starting from given prefix
        for child in curr_node.get_children():
            candidates.extend(super()._get_candidates(child, [prefix]))
        return candidates





if __name__ == "__main__":
    # # src: https://en.wikipedia.org/wiki/Radix_tree?oldformat=true
    rt = RadixTrie()
    rt.insert("romane")
    rt.insert("romane")
    rt.insert("romanus")
    rt.insert("romulus")
    rt.insert("rubens")
    rt.insert("ruber")
    rt.insert("rubicon")
    rt.insert("rubicundus")
    print(rt)
    print("Total Nodes:", len(rt)) #14
    print('='*50)

    rt = RadixTrie()
    rt.insert('s')
    rt.insert("shear")
    rt.insert("she")
    rt.insert("shears")
    rt.insert("shepard")
    rt.insert("shepard")
    rt.remove('s')
    print(rt)
    print("Total Nodes:", len(rt)) #6
    print('she' in rt) #True
    print("sha" in rt) #False
    print(rt.auto_complete("")) # [she', 'shear', 'shears', 'shepard']
    print(rt.auto_complete("a")) # []
    print(rt.auto_complete("s")) # ['she', 'shear', 'shears', 'shepard']
    print(rt.auto_complete("sh")) # ['she', 'shear', 'shears', 'shepard']
    print(rt.auto_complete("sha")) # []
    print(rt.auto_complete("she")) # ['she', 'shear', 'shears', 'shepard']
    print(rt.auto_complete("shee")) # []
    print(rt.auto_complete("shea")) # ['shear' 'shears']
    print(rt.auto_complete("sheaa")) # []
    print(rt.auto_complete("shearr")) # []
    print(rt.auto_complete("shep")) # ['shepard']
    print(rt.auto_complete("apple")) # []
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
    print("Total Nodes:", len(rt)) #11
    print("slowlie" in rt) #False
    print("slowl" in rt) #False
    print("slowly" in rt) #True
    rt.remove("test")
    rt.remove("slow")
    rt.remove("slowl")
    print(rt)
    print("Total Nodes:", len(rt)) #10
    print('slow' in rt) #False
    print(rt.has_prefix("slo")) #True
    print(rt.has_prefix("s")) #True
    print(rt.has_prefix("sloww")) #False
    print(rt.has_prefix("slow")) #True
    print('='*50)
    
    # # sanity checks
    # rt = RadixTrie()
    # print(rt.find(''))
    # print(rt.find(2)) #throws error


