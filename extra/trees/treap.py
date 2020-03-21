"""
Treap is a data structure which is a hyprid of (Tree + Heap) where every node
of it maintains two values.
    - Key: Follows standard BST ordering (left is smaller and right is greater)
    - Priority: Randomly assigned value that follows Max-Heap property.

A treap node is represented like the following 0|⁽²⁶⁵⁾ where 0 is the key and 
205 is the priority. The higher the number is, the more priority it has.
"""
import random
from extra.trees.bst import BSTNode, BST




class TreapNode(BSTNode):
    def __name__(self):
        return "extra.TreapNode()"
    

    def __init__(self, key):
        super().__init__(key)
        self.priority = random.randint(0, 100)


    def get_priority(self):
        return self.priority


    def set_priority(self, new_priority):
        if type(new_priority) not in {int, float}:
            raise TypeError("Given priority has to be a number!!")
        self.priority = new_priority


    def __repr__(self):
        """Represents Node object as a string"""
        return f"TreapNode(data: {self.data}, Priority: {self.priority})"


    def _represent(self):
        if Treap.SHOW_PRIORITY:
            return f"{self.data}|P:{self.priority}"
        else:
            return f"{self.data}"




class Treap(BST):
    SHOW_PRIORITY = False
    _basic_node = TreapNode


    def __name__(self):
        return "extra.Treap()"
    

    def __init__(self, key, seed=None):
        # to keep consistency
        if seed is not None: random.seed(seed)
        super().__init__(key)

    
    ############################## INSERTION ##############################
    def insert(self, value):
        # perform standard BST-insert
        new_node = super()._insert_value(self.root, value)
        # using rotations when necessary
        parent = new_node.get_parent()
        while(parent is not None):
            grandparent = parent.get_parent()
            if parent.get_priority() > new_node.get_priority():
                break
            else:
                if new_node.is_left_child():
                    parent = super()._rotate_right(parent)
                else:
                    parent = super()._rotate_left(parent)
                super()._attach(grandparent, parent)
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
                removed_node = super()._rotate_right(removed_node)
                super()._attach(parent, removed_node)
                parent = removed_node
                removed_node = parent.get_right()
            else:
                removed_node = super()._rotate_left(removed_node)
                super()._attach(parent, removed_node)
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
    print("Total nodes:", len(t))
    print("Biggest Value is:", t.get_max())

