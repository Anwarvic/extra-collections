import random
from linked_list import Node, LinkedList




#helper functions
def flip_coin():
    # return random.choice(['head','tail'])
    return "head"


def search(start_node, value):
    # search a sorted linked list and return the last accessed node.
    prev = curr_node = start_node
    while(curr_node != None and curr_node.get_data() <= value):
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
    

    def __print_level(self, level):
        lower_list = self.skiplist[0]
        curr_list = self.skiplist[level]
        # the following two lists will represent the output of this function
        bottom_border = ['└'] if curr_list.head.get_down() == None else ['├']
        middle = ['│']
        # iterate over two lists in parallel
        lower_node = lower_list.head
        curr_node = curr_list.head
        while(lower_node != None):
            item = str(curr_node)
            width = len(item)+2 #2: for a space before & after an item
            if lower_node.get_data() == curr_node.get_data():
                middle += [f" {item} →"]
                bottom_border += (['─']*width)
                bottom_border +=  ['┴'] if level == 0 else ['┼']
                curr_node = curr_node.get_next()
            else:
                placeholder = '→'*width
                middle += [f"{placeholder}→"]
                bottom_border += (['─']*width) + ['┬']
            lower_node = lower_node.get_next()
        middle += [' ']
        bottom_border += ['─']
        return "{}\n{}".format("".join(middle), "".join(bottom_border))


    def __repr__(self):
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
        output = [self.__print_level(level) \
                    for level in range(self.num_levels-1, -1, -1)]
        return "\n".join(output)
    
    
    def __contains__(self, value):
        return self.search(value)


    def _search(self, value):
        # returns the last accessed node when searching a certain value.
        last_accessed_nodes = []
        top_list = self.skiplist[self.num_levels-1]
        start_node = top_list.head
        while(start_node.get_down() != None):
            found_node = search(start_node, value)
            last_accessed_nodes.append(found_node)
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
        return new_llist
    
    
    def _promote(self, upper_prev_node, curr_node):
        # create new node with the same data as curr_data
        upper_node = SkipNode(curr_node.get_data())
        # connect the upper list to the new node
        upper_node.set_next(upper_prev_node.get_next())
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
        new_node.set_next(found_node.get_next())
        found_node.set_next(new_node)
        # promote the new_node if coin is `Head`
        # TODO: change `if` to `while`
        if flip_coin() == "head":
            if curr_level >= self.num_levels-1:
                top_list = self._add_extra_level()
                upper_prev_node = top_list.head
            else:
                upper_prev_node = last_accessed_nodes[curr_level]
            # promote new_node
            self._promote(upper_prev_node, new_node)
            curr_level += 1


    def remove(self, value):
        """removal is done in O(log(n))"""
        pass






if __name__ == "__main__":
    sk = SkipList()
    sk.insert(2)
    sk.insert(2)
    sk.insert(0)
    # for level, lst in enumerate(sk.skiplist):
    #     print(lst)
    print(sk)