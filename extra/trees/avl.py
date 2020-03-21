from extra.trees.bst import BSTNode, BST



class AVL(BST):

    ######################### RE-BALANCE #########################
    def __get_children_depths(self, start_node):
        left_depth = 1 if start_node.get_left() != None else 0
        left_depth += super()._get_depth(start_node.get_left())
        right_depth = 1 if start_node.get_right() != None else 0
        right_depth += super()._get_depth(start_node.get_right())
        return left_depth, right_depth

    def __rebalance_subtree(self, start_node):
        left_depth, right_depth = self.__get_children_depths(start_node)
        # subtree is imbalanced
        if abs(left_depth - right_depth) > 1:
            # left direction
            if left_depth > right_depth:
                child = start_node.get_left()
                left_depth, right_depth = self.__get_children_depths(child)
                # left direction
                if left_depth > right_depth:
                    start_node = super()._rotate_right(start_node)
                # right direction
                else:
                    start_node = super()._rotate_left_right(start_node)
            # right direction
            else:
                child = start_node.get_right()
                left_depth, right_depth = self.__get_children_depths(child)
                # left direction
                if left_depth > right_depth:
                    start_node = super()._rotate_right_left(start_node)
                # right direction
                else:
                    start_node = super()._rotate_left(start_node)
        # recurssively apply __reblanace_subtree()
        if start_node.get_left() is not None:
            start_node.set_left( \
                self.__rebalance_subtree(start_node.get_left()) )
        if start_node.get_right() is not None:
            start_node.set_right( \
                self.__rebalance_subtree(start_node.get_right()) )
        return start_node

    def rebalance(self):
        new_root = self.__rebalance_subtree(self.root)
        self.root = new_root
    
    
    ######################### INSERTION #########################
    def insert(self, value):
        super().insert(value)
        self.rebalance()


    ######################### REMOVAL #########################
    def remove(self, del_value):
        super().remove(del_value)
        self.rebalance()





if __name__ == "__main__":
    # to test left rotation
    avl = AVL(22)
    avl.root.set_right(BSTNode(43))
    avl.root.set_left(BSTNode(18))
    avl.root.get_left().set_left(BSTNode(9))
    avl.root.get_left().set_right(BSTNode(21))
    avl.root.get_left().get_left().set_left(BSTNode(6))
    avl.root.get_left().get_left().get_left().set_left(BSTNode(0))
    print(avl, '\n')
    avl.rebalance()
    print(avl)
    print('='*50)

    #######################################
    # to test left-right rotation
    avl = AVL(78)
    avl.root.set_right(BSTNode(88))
    avl.root.set_left(BSTNode(50))
    avl.root.get_left().set_left(BSTNode(48))
    avl.root.get_left().set_right(BSTNode(62))
    avl.root.get_left().get_right().set_left(BSTNode(54))
    print(avl, '\n')
    avl.rebalance()
    print(avl)
    print('='*50)

    #######################################
    # test all rotation-operations
    # src: Data Structures and Algorithms in Python Book (page: 506)
    avl = AVL(44)
    avl.root.set_left(BSTNode(17))
    avl.root.get_left().set_right(BSTNode(32))
    avl.root.set_right(BSTNode(78))
    avl.root.get_right().set_left(BSTNode(50))
    avl.root.get_right().set_right(BSTNode(88))
    avl.root.get_right().get_left().set_left(BSTNode(48))
    avl.root.get_right().get_left().set_right(BSTNode(62))
    avl.root.get_right().get_left().get_right().set_left(BSTNode(54))
    print(avl)
    avl.rebalance()
    print(avl)
    print('='*50)

    #######################################
    # insertion test (src: https://www.youtube.com/watch?v=7m94k2Qhg68)
    avl = AVL(43)
    avl.insert(18)
    avl.insert(22)
    avl.insert(9)
    avl.insert(21)
    avl.insert(6)
    avl.insert(8)
    avl.insert(20)
    avl.insert(63)
    avl.insert(50)
    avl.insert(62)
    avl.insert(51)
    print(avl)
    print('='*50)
    
    #######################################
    # test all remove operation
    # src: Data Structures and Algorithms in Python Book (page: 508)
    avl = AVL(44)
    avl.root.set_left(BSTNode(17))
    avl.root.get_left().set_right(BSTNode(32))
    avl.root.set_right(BSTNode(62))
    avl.root.get_right().set_left(BSTNode(50))
    avl.root.get_right().set_right(BSTNode(78))
    avl.root.get_right().get_left().set_left(BSTNode(48))
    avl.root.get_right().get_left().set_right(BSTNode(54))
    avl.root.get_right().get_right().set_right(BSTNode(88))
    print(avl)
    avl.remove(17)
    avl.remove(50)
    print(avl)
    print('='*50)
