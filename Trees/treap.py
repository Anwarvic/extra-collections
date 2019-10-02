from random import seed, randint
from bst import TreeNode, BST

seed(0)
class TreapNode(TreeNode):
    def __init__(self, key):
        super().__init__(key)
        self.priority = randint(0, 1000)


    def get_priority(self):
        return self.priority


    def set_priority(self, new_priority):
        assert type(new_priority) in {int, float},\
                "Given priority has to be a number!!"
        self.priority = new_priority


    def represent_data(self):
        return "{}|{}".format(self.data, self.priority)



class Treap(BST):
    def __init__(self, key):
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
            grandparent = parent.get_parent() if parent else None
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




if __name__ == "__main__":
    t = Treap(1)
    print(t)
