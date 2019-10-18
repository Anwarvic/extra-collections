"""
Treap is a data structure which is a hyprid of (Tree + Heap) where every node
of it maintains two values.
    - Key: Follows standard BST ordering (left is smaller and right is greater)
    - Priority: Randomly assigned value that follows Max-Heap property.
"""
import random
from bst import TreeNode, BST




class TreapNode(TreeNode):
    def __init__(self, key):
        super().__init__(key)
        self.priority = random.randint(0, 1000)


    def get_priority(self):
        return self.priority


    def set_priority(self, new_priority):
        assert type(new_priority) in {int, float},\
                "Given priority has to be a number!!"
        self.priority = new_priority


    def represent_data(self):
        return "{}|{}".format(self.data, self.priority)




class Treap(BST):
    def __init__(self, key, seed=None):
        # to keep consistency
        if seed is not None: random.seed(seed)
        if isinstance(key, TreapNode):
            self.root = key
        else:
            self.root = TreapNode(key)

    
    ############################## ROTATION  ##############################    
    def __rotate_left(self, start_node):
        # print("Rotating Left")
        middle = start_node.get_right()
        middle.set_parent( start_node.get_parent() )
        start_node.set_right(middle.get_left())
        middle.set_left(start_node)
        return middle

    def __rotate_right(self, start_node):
        # print("Rotating Right")
        middle = start_node.get_left()
        middle.set_parent( start_node.get_parent() )
        start_node.set_left(middle.get_right())
        middle.set_right(start_node)
        return middle


    def __attach(self, parent, child):
        if parent is None:
            self.root = child
        else:
            if parent.get_data() > child.get_data():
                parent.set_left(child) 
            else:
                parent.set_right(child)
    

    ############################## INSERTION ##############################
    def insert(self, value):
        # perform standard BST-insert
        new_node = super()._insert(TreapNode(value), self.root)
        # using rotations when necessary
        parent = new_node.get_parent()
        while(parent is not None):
            grandparent = parent.get_parent()
            if parent.get_priority() > new_node.get_priority():
                break
            else:
                if new_node.is_left_child():
                    parent = self.__rotate_right(parent)
                else:
                    parent = self.__rotate_left(parent)
                self.__attach(grandparent, parent)
                new_node = parent
                parent = grandparent


    ##############################  REMOVAL  ##############################
    def remove(self, del_value):
        assert type(del_value) in {int, float}, "BST conains numbers only!"
        if self.root.is_leaf() and del_value == self.root.get_data():
            raise ValueError("Can't remove the only item in the treap!")

        # search for the del_value node
        removed_node = super()._search(del_value, self.root)
        # couldn't find the node
        if removed_node.get_data() != del_value:
            return
        # rotate till removed_node is leaf
        parent = removed_node.get_parent()
        while(not removed_node.is_leaf()):
            # get children's priority
            left_child = removed_node.get_left()
            right_child = removed_node.get_right()
            left_priority = left_child.get_priority() if left_child else -1
            right_priority = right_child.get_priority() if right_child else -1
            # perform rotation
            if left_priority > right_priority:
                removed_node = self.__rotate_right(removed_node)
                self.__attach(parent, removed_node)
                parent = removed_node
                removed_node = parent.get_right()
            else:
                removed_node = self.__rotate_left(removed_node)
                self.__attach(parent, removed_node)
                parent = removed_node
                removed_node = parent.get_left()
        # perform the removal
        if removed_node.is_left_child():
            parent.set_left(None)
        else:
            parent.set_right(None)




if __name__ == "__main__":
    t = Treap(50, seed=0)
    t.insert(30)
    t.insert(70)
    t.insert(20)
    t.insert(40)
    t.insert(80)
    t.insert(0)
    print(t, '\n')
    t.remove(30)
    print(t)

