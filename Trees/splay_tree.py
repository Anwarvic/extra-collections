from bst import TreeNode, BST

class SplayTree(BST):
    def zig_zig(self, start_node, left_children=True):
        child = start_node
        parent = start_node.parent
        grand_parent = parent.parent
        # start zig-zig
        if left_children:
            print("Left zig-zig")
            child.parent = grand_parent.parent
            grand_parent.set_left(parent.right)
            parent.set_right(grand_parent)
            parent.set_left(child.right)
            child.set_right(parent)
        else:
            print("Right zig-zig")
            child.parent = grand_parent.parent
            grand_parent.set_right(parent.left)
            parent.set_left(grand_parent)
            parent.set_right(child.left)
            child.set_left(parent)
        #child is now the grand-parent
        return child







if __name__ == "__main__":
    # test Left zig-zig
    stree = SplayTree(30)
    stree.insert(20)
    stree.insert(10)
    print(stree)
    stree.root = stree.zig_zig(stree.root.left.left, left_children=True)
    print(stree)
    print('='*50)

    # test Right zig-zig
    stree = SplayTree(10)
    stree.insert(20)
    stree.insert(30)
    print(stree)
    stree.root = stree.zig_zig(stree.root.right.right, left_children=False)
    print(stree)
    print('='*50)