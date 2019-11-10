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


    def __repr__(self):
        data = self.data
        nxt = self.next.data if self.next else None
        return "Node: (item: {}, next: {})".format(data, nxt)




class SkipList:
    def __init__(self, value=None):
        self.num_levels = 1
        #SkipList is an array of LinkedList objects
        self.skiplist = [LinkedList( SkipNode(float("-inf")) )]
        if value != None:
            self.insert(value)


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
        

    def insert(self, value):
        #insertion is done in O(log(n))
        found_node, last_accessed_nodes = self._search(value)
        if found_node.get_data() != value:
            self.skiplist[0].




    def remove(self, item):
        #removal is done in O(log(n))
        pass
