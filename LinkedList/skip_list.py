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
    # return random.choice(['head','tail'])
    return 'head'


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
        #TODO: is self.up necessary... I think not
        self.data = item
        self.next = None
        self.up = None
        self.down = None


    def __str__(self):
        if self.data == float("-inf"):
            return "-∞"
        elif self.data == float("inf"):
            return "∞"
        return super().__str__()


    def get_down(self):
        return self.down
    

    def get_up(self):
        return self.up
    
    
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
        

    def _add_extra_level(self):
        top_list = self.skiplist[self.num_levels-1]
        new_llist = LinkedList(SkipNode(float("-inf")))
        # connect the head of the new linked list to the lower linked list
        new_llist.head.set_down(top_list.head)
        # add new linked list to the SkipList
        self.skiplist.append(new_llist)
        self.num_levels += 1
    
    
    def _promote(self, upper_prev_node, curr_node):
        # create new node with the same data as curr_data
        upper_node = SkipNode(curr_node.get_data())
        # connect the upper list to the new node
        upper_prev_node.set_next(upper_node)
        # connect the curruent list with the upper one
        curr_node.set_up(upper_node)


    def insert(self, value):
        """
        Inserts a value into our Skip List. Insertion is done in O(log(n)) time
        """
        found_node, last_accessed_nodes = self._search(value)
        # `value` already exists in our SkipList
        if found_node.get_data() == value:
            return
        curr_level = 0
        new_node = SkipNode(value)
        found_node.set_next(new_node)
        # promote the new_node if coin is `Head`
        # TODO: change `if` to `while`
        if flip_coin() == "head":
            if curr_level >= self.num_levels-1:
                self._add_extra_level()
                top_list = self.skiplist[self.num_levels-1]
                upper_prev_node = top_list.head
            else:
                upper_prev_node = last_accessed_nodes[curr_level]
            self._promote(upper_prev_node, new_node)
            curr_level += 1



    def remove(self, item):
        #removal is done in O(log(n))
        pass




if __name__ == "__main__":
    sk = SkipList()
    sk.insert(2)
    sk.insert(2)
    for level, lst in enumerate(sk.skiplist):
        print(lst)