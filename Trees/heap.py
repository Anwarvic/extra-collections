from avl import TreeNode
from bst import BST


class MinHeap(BST):
    def __init__(self, value):
        if type(value) == list:
            self.length = len(value)
            self.root = self.__heapify(value)
        else:
            self.length = 1
            self.root = TreeNode(value)

    def __heapify(self, lst):
        lst = sorted(lst)
        length = len(lst)
        assert length >0, "Given List must have values!!"
        if length == 1:
            node = TreeNode(lst[0])
        elif length == 2:
            node = TreeNode(lst[0])
            node.set_left( TreeNode(lst[1]) )
        else:
            node = TreeNode(lst[0])
            node.set_left( self.__heapify(lst[1::2]) )
            node.set_right( self.__heapify(lst[2::2]) )
        return node


    def __len__(self):
        return self.length

    def get_min(self):
        return self.root.data

    def get_max(self):
        raise NotImplementedError("This is a min-heap!!")


    ############################## INSERTION ##############################
    def swap(self, parent, start_node):
        pass


    def insert(self, value):
        assert type(value) in {int, float}, "You can insert only numbers!"
        self.length += 1
        level = 





if __name__ == "__main__":
    h = MinHeap([4,3,1,2, 5, 80, 10, 20, 30, 40, 52, 10])
    print(h)
    print(h.get_min())
    print("Heap Traverse:", h.traverse("depth-first"))
    print(len(h))
