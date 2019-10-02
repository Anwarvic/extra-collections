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

    
    ############################## INSERTION ##############################
    def insert(self, ):
        pass




if __name__ == "__main__":
    t = Treap(1)
    print(t)
