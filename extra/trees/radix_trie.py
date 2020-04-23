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
    

    ##############################   INSERTION    ##############################
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
                self._nodes_count += 1
            # child is prefix of the remaining_word
            elif idx <= len(remaining_word) and idx != len(child_data):
                # split child
                new_node = TrieNode(child_data[:idx])
                child._data = child_data[idx:]
                new_node.set_child(child_data[idx], child)
                # connect new_node to curr_node
                curr_node.set_child(child_data[0], new_node)
                remaining_word = remaining_word[idx:]
                self._nodes_count += 1
            curr_node = new_node
        # mark current node as a word
        curr_node._is_word = True


    ############################## AUTOCOMPLETION ##############################
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
        if curr_node._is_word:
            candidates.append(prefix)
        # get candidates starting from given prefix
        for child in curr_node.get_children():
            candidates.extend(super()._get_candidates(child, [prefix]))
        return candidates


