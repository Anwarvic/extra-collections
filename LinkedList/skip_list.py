"""
Skip List is gonna look like this:
┌────┬─────────────┬───┬─
│ -∞ →→→→→→→→→→→→→→→ 2 → 
├────┼─────────┼───┼───┼─
│ -∞ →→→→→→→→→→→ 6 → 2 → 
├────┼────┬────┼───┼───┬─
│ -∞ → 77 → 10 → 6 → 2 → 
└────┴────┴────┴───┴───┴─
"""
import random
from linked_list import Node, LinkedList




#helper function
def flip_coin():
    return random.choice(['head','tail'])

def search(start_node, value):
    # search a sorted linked list and return the last accessed node.
    prev = curr_node = start_node
    while(curr_node != None and curr_node.get_data() < value):
        prev = curr_node
        curr_node = curr_node.get_next()
    return prev




class SkipNode(Node):
    def __init__(self, item):
        assert type(item) in {int, float, str}, \
            "Skip Lists support only native data-types like: [int, float, str]!"
        self.data = item
        self.next = None
        self.up = None
        self.down = None


    def __str__(self):
        if self.data == float("-inf"):
            return "-∞"
        elif self.data == float("inf"):
            return "∞"
        return str(self.data)

    
    def set_down(self, other_node):
        other_node.up = self
        self.down = other_node
    
    def set_up(self, other_ndoe):
        other_ndoe.down = self
        self.up = other_ndoe



class SkipList:
    def __init__(self, value=None):
        self.num_levels = 1
        #SkipList is an array of LinkedList objects
        self.skiplist = [LinkedList( SkipNode(float("-inf")) )]
        if value != None:
            self.insert(value)
    
    def __repr__(self):
        pass
    
    def __contains__(self, value):
        return self.search(value)


    def _search(self, value):
        # returns the last accessed node when searching a certain value.
        top_list = self.skiplist[self.num_levels-1]
        start_node = top_list.head
        curr_level = self.num_levels - 1
        last_accessed_nodes = []
        while(curr_level > 0):
            found_node = search(start_node, value)
            last_accessed_nodes.append(found_node)
            curr_level -= 1
            start_node = found_node.get_down()
        found_node = search(start_node, value)
        assert len(last_accessed_nodes) == self.num_levels-1
        return found_node, last_accessed_nodes[::-1]


    def search(self, value):
        found_node, _ = self._search(value)
        return found_node.get_data() == value
        

    def promote(self, upper_node, curr_node):
        new_node = SkipNode(curr_node.get_data())
        upper_node.set_next(new_node)
        curr_node.set_up(new_node)


    
    def insert(self, value):
        #insertion is done in O(log(n))
        found_node, last_accessed_nodes = self._search(value)
        # `value` already exists in our SkipList
        if found_node.get_data() == value:
            return
        curr_level = 0
        new_node = SkipNode(value)
        found_node.set_next(new_node)
        # promote the new_node if coin is `Head`
        while flip_coin() == "Head":
            curr_level += 1
            self._promote()



    def remove(self, item):
        #removal is done in O(log(n))
        pass
