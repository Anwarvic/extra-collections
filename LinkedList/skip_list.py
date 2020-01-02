import random
from doubly_linked_list import DoublyNode, DoublyLinkedList




#helper functions
random.seed(1)
def flip_coin():
    return random.choice(['head','tail'])


def search_sorted(start_node, value):
    # search a sorted linked list and return the last accessed node.
    prev = curr_node = start_node
    while(curr_node != None and curr_node.get_data() <= value):
        prev = curr_node
        curr_node = curr_node.get_next()
    return prev




class SkipNode(DoublyNode):
    def __init__(self, item):
        assert type(item) in {int, float, str}, \
            "Skip Lists support only native data-types like: [int, float, str]!"
        self.data = item
        self.prev = None
        self.next = None
        self.down = None


    def __str__(self):
        if self.data == float("-inf"):
            return "-∞"
        elif self.data == float("inf"):
            return "∞"
        return super().__str__()


    def get_down(self):
        return self.down
    

    def set_down(self, other_node):
        self.down = other_node




class SkipList:
    def __init__(self, value=None):
        self.num_levels = 1
        #SkipList is an array of LinkedList objects
        self.skiplist = [DoublyLinkedList( SkipNode(float("-inf")) )]
        if value != None:
            self.insert(value)
    

    ############################## PRINT ##############################
    def __print_node(self, node, zeroth_node, lower_node):
        """
        This private method is responsible for representing each node in the 
        Skip List. To do its job, it needs to use two other nodes:
        - zeroth_node: node of the 0th level of the Skip List where all nodes
            are represented.
        - lower_node: node of the lower level.
        """
        middle = []
        bottom_border = []
        item = str(zeroth_node)
        width = len(item)+2 #2: for a space before & after an item
        if node != None and zeroth_node.get_data() == node.get_data():
            bottom_border += ['└'] if lower_node == None else ['├']
            bottom_border += (['─']*width)
            bottom_border += ['┘ '] if lower_node == None else ['┤ ']
            middle += [f"| {item} │⟷"]
        else:
            middle += [f"⟷{'⟷'*width}⟷⟷"]
            if lower_node != None and lower_node.data == zeroth_node.data:
                bottom_border += ['┌'] + (['─']*width) + ['┐ ']
            else:
                bottom_border += [' '] + ([' ']*width) + ['  ']
        return middle, bottom_border


    def __print_level(self, level):
        """
        This private method is responsible for representing each level in the 
        Skip List.
        NOTE: I know this isn't the best way to do it, but that's what popped up
        first into my mind.
        """
        zeroth_list = self.skiplist[0]
        curr_list = self.skiplist[level]
        # the following two lists will represent the output of this function
        bottom_border = []
        middle = []
        # iterate over two lists in parallel
        zeroth_node = zeroth_list.head
        curr_node = curr_list.head
        lower_node = self.skiplist[level-1].head if level > 0 else None
        while(zeroth_node != None):
            middle_part, bottom_part = \
                self.__print_node(curr_node, zeroth_node, lower_node)
            middle += middle_part
            bottom_border += bottom_part
            if curr_node != None and zeroth_node.data == curr_node.data:
                curr_node = curr_node.get_next()
            if lower_node != None and zeroth_node.data == lower_node.data:
                lower_node = lower_node.get_next()
            zeroth_node = zeroth_node.get_next()
        return "{}\n{}".format(''.join(middle), ''.join(bottom_border))


    def __print_top_border(self):
        """
        This method is only responsible for just one thing, to print out the 
        top border of the Skip List.
        """
        lower_list = self.skiplist[0]
        top_list = self.skiplist[self.num_levels-1]
        # the following two lists will represent the output of this function
        top_border = []
        # iterate over two lists in parallel
        lower_node = lower_list.head
        curr_node = top_list.head
        while(lower_node != None):
            item = str(lower_node)
            width = len(item)+2 #2: for a space before & after an item
            if curr_node != None and lower_node.data == curr_node.data:
                top_border += ['┌'] + (['─']*width) + ['┐ ']
                curr_node = curr_node.get_next()
            else:
                top_border += [' '] + ([' ']*width) + ['  ']
            lower_node = lower_node.get_next()
        return "{}".format(''.join(top_border))


    def __repr__(self):
        """
        The complexity of this method is O(n*l) where:
            - n: is the number of nodes in the first list
            - l: is the number of levels
        Skip List is gonna look like this:
        ┌────┐                     ┌───┐
        │ -∞ │⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷⟷│ 2 │⟷
        ├────┤        ┌────┐       ├───┤
        │ -∞ │⟷⟷⟷⟷⟷⟷⟷⟷│ 10 │⟷⟷⟷⟷⟷⟷⟷│ 2 │⟷
        ├────┤ ┌────┐ ├────┤ ┌───┐ ├───┤
        │ -∞ │⟷│ 77 │⟷│ 10 │⟷│ 6 │⟷│ 2 │⟷
        └────┘ └────┘ └────┘ └───┘ └───┘
        """
        output = [self.__print_top_border()]
        output += [self.__print_level(level) \
                    for level in range(self.num_levels-1, -1, -1)]
        return "\n".join(output)
    

    ############################## LENGTH ##############################    
    def __len__(self):
        return len(self.skiplist[0]) - 1
    

    def is_empty(self):
        return len(self) == 0


    ############################# ITERATOR #############################
    #TODO: fix the bug where -∞ is yielded
    def __iter__(self):
        for item in self.skiplist[0]:
            yield item

    
    def __contains__(self, value):
        return self.search(value)


    def _search(self, value):
        # returns the last accessed node when searching a certain value.
        last_accessed_nodes = []
        top_list = self.skiplist[self.num_levels-1]
        start_node = top_list.head
        while(start_node.get_down() != None):
            found_node = search_sorted(start_node, value)
            if found_node.get_data() == value:
                return found_node, last_accessed_nodes
            last_accessed_nodes.append(found_node)
            start_node = found_node.get_down()
        found_node = search_sorted(start_node, value)
        assert len(last_accessed_nodes) == self.num_levels-1
        return found_node, last_accessed_nodes[::-1]


    def search(self, value):
        """Search Skip List is one in O(log(n)) time"""
        found_node, _ = self._search(value)
        return found_node.get_data() == value
        

    def _add_extra_level(self):
        top_list = self.skiplist[self.num_levels-1]
        new_llist = DoublyLinkedList(SkipNode(float("-inf")))
        # connect the head of the new linked list to the lower linked list
        new_llist.head.set_down(top_list.head)
        # add new linked list to the SkipList
        self.skiplist.append(new_llist)
        self.num_levels += 1
        return new_llist
    
    
    def _promote(self, upper_prev_node, curr_node, curr_level):
        # create new node with the same data as curr_data
        upper_node = SkipNode(curr_node.get_data())
        # connect the upper list to the new node
        upper_node = self.skiplist[curr_level+1]._insert_node(upper_prev_node,
                                                              upper_node)
        # connect the current list with the upper one
        upper_node.set_down(curr_node)
        return upper_node


    def insert(self, value):
        """
        Inserts a value to our Skip List. Insertion is done in O(log(n)) time
        """
        found_node, last_accessed_nodes = self._search(value)
        # `value` already exists in our SkipList
        if found_node.get_data() == value:
            return
        # create new_node with the new value
        new_node = SkipNode(value)
        # insert new_node to the 0th linkedlist
        curr_node = self.skiplist[0]._insert_node(found_node, new_node) 
        
        # promote the new_node if flipping the coin results `Head`
        curr_level = 0
        while flip_coin() == "head":# TODO: change `if` to `while`
            if curr_level >= self.num_levels-1:
                top_list = self._add_extra_level()
                upper_prev_node = top_list.head
            else:
                upper_prev_node = last_accessed_nodes[curr_level]
            # promote new_node
            curr_node = self._promote(upper_prev_node, curr_node, curr_level)
            curr_level += 1


    def remove(self, value):
        """removal is done in O(log(n))"""
        found_node, last_accessed_nodes = self._search(value)
        if found_node.get_data() == value:
            level = self.num_levels - 1 - len(last_accessed_nodes)
            while(level >= 0):
                self.skiplist[level]._remove_node(found_node.get_prev(),
                                                  found_node)
                level -= 1
                found_node = found_node.get_down()
        





if __name__ == "__main__":
    sk = SkipList()
    print(sk)
    sk.insert(2)
    sk.insert(2)
    sk.insert(0)
    sk.insert(10)
    sk.insert(100)
    sk.insert(50)
    sk.insert(-20)
    print(sk)
    print(2 in sk)
    print(100 in sk)
    print(20 in sk)
    sk.remove(0)
    print(sk)
    for item in sk: print(item)