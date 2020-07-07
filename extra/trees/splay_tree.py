"""
Splay Tree is a binary search tree which is a non-linear data structure that
stores numbers hierarchical. With the exception of the top element, each element
in the binary serach tree has a parent element and each node has two children
elements at most. We typically call the top element of the binary search tree,
"the root". The root is drawn as the highest element, with the other elements
being connected below (just the opposite of an actual tree).

The only difference between "Splay Trees" and "BSTs" is that any operation done
to the the former, like insertion, deletion, or even a search, should be
followed by a move-to-root operation called "splaying" that changes the
structure of the tree. 

To understand the splaying operation even more, let's look at the the following
SplayTree which is a BST in a first place.

.. code-block:: text

      3__
     /   \\
    2     5
         / \\
        4   6

Now, let's insert `4.5` to this SplayTree; now the Splay Tree will look like the
following:

.. code-block:: text

        __4.5
       /     \\
      3       5
     / \\       \\
    2   4       6

As we can see, the newly-inserted node has been moved to the root which makes it
faster to be accessed for later usage. This happens with all searching,
insertion and deletion.


The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **h** is the height of the BST which approximatley equals to **log(n)**.

+--------------------------+----------------------------------------------------+------------+---------+
| Method                   | Description                                        | Worst-case | Optimal |
+==========================+====================================================+============+=========+
| __len__()                | Returns the number of nodes.                       | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_empty()               | Checks if object is empty.                         | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __repr__()               | Represents the BST.                                | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __iter__()               | Iterates over the BST.                             | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __contains__()           | Checks the existence of the given item.            | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_height()             | Gets the BST's height.                             | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_depth()              | Gets the BST's depth.                              | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_nodes()              | Returns a list of all nodes per level.             | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_balanced()            | Checks if the BST is balanced.                     | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_perfect()             | Checks if the BST is perfect.                      | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_strict()              | Checks if the BST is strict.                       | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| count_leaf_nodes()       | Counts all leaf nodes in the tree.                 | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| clear()                  | Clears the whole tree instance.                    | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| to_list()                | Converts the bianry tree instance to list.         | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| traverse()               | Traverses the BST based on given method.           | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| preorder_traverse()      | Traverses the BST in an pre-order manner.          | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| inorder_traverse()       | Traverses the BST in an in-order manner.           | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| postorder_traverse()     | Traverses the BST in an post-order manner.         | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| breadth_first_traverse() | Traverses the BST level by level.                  | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| depth_first_traverse()   | Traverses the BST in an pre-order manner.          | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_min()                | Gets the minimum number in the BST.                | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_max()                | Gets the maximum number in the BST.                | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| insert()                 | Inserts a certain value to the BST.                | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+
| remove()                 | Removes a certain value from the BST.              | O(h)       | O(h)    |
+--------------------------+----------------------------------------------------+------------+---------+

Class Documentation
===================
Here are all of the public methods that can be used with `SplayTree()` objects:
"""
from extra.trees.bst import BST




class SplayTree(BST):
    """
    A Splay Tree is a non-linear data structure that can be defined recursively
    using a collection of `BSTNode()` instances, where each node contains a 
    numeric value and it has either zero, one or two references to the children
    `BSTNode()` instances. Any node that has been accessed is moved to the root
    directly to make it faster to be accessed again. This operation is called
    "splaying". Hence the name of this data structure.
    """
    __name__ = "extra.SplayTree()"
    

    ##############################    SPLAYING    ##############################
    def __zig_zig(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zig-zig operation")
        child = start_node
        parent = child.get_parent()
        grand_parent = child.get_grand_parent()
        # start zig-zig
        child.set_parent( grand_parent.get_parent() )
        grand_parent.set_left(parent.get_right())
        parent.set_right(grand_parent)
        parent.set_left(child.get_right())
        child.set_right(parent)
        #child is now the grand-parent
        return child
    

    def __zag_zag(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zag-zag operation")
        child = start_node
        parent = child.get_parent()
        grand_parent = child.get_grand_parent()
        # start zag-zag
        child.set_parent( grand_parent.get_parent() )
        grand_parent.set_right(parent.get_left())
        parent.set_left(grand_parent)
        parent.set_right(child.get_left())
        child.set_left(parent)
        #child is now the grand-parent
        return child


    def __zig_zag(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zig-zag operation")
        child = start_node
        parent = child.get_parent()
        grand_parent = child.get_grand_parent()
        # start zig-zag
        child.set_parent( grand_parent.get_parent() )
        grand_parent.set_left(child.get_right())
        parent.set_right(child.get_left())
        child.set_right(grand_parent)
        child.set_left(parent)
        return child


    def __zag_zig(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zag-zig operation")
        child = start_node
        parent = child.get_parent()
        grand_parent = child.get_grand_parent()
        # start zag-zig
        child.set_parent( grand_parent.get_parent() )
        grand_parent.set_right(child.get_left())
        parent.set_left(child.get_right())
        child.set_left(grand_parent)
        child.set_right(parent)
        return child


    def __zig(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zig operation")
        child = start_node
        parent = child.get_parent()
        child.set_parent( parent.get_parent() )
        parent.set_left(child.get_right())
        child.set_right(parent)
        return child
    

    def __zag(self, start_node):
        assert isinstance(start_node, self._basic_node)
        # print("zag operation")
        child = start_node
        parent = child.get_parent()
        child.set_parent( parent.get_parent() )
        parent.set_right(child.get_left())
        child.set_left(parent)
        return child


    def __splaying(self, start_node):
        assert isinstance(start_node, self._basic_node)
        child = start_node
        parent = child.get_parent()
        if parent is None:
            return start_node
        grand_parent = child.get_grand_parent()
        # get the operation type
        if grand_parent is None:
            if child.is_left_child():
                root = self.__zig(child)
            else:
                root = self.__zag(child)
        else:
            # left -> left
            if parent.is_left_child() and child.is_left_child():
                grand_parent = self.__zig_zig(child)
            # left -> right
            elif parent.is_left_child() and not child.is_left_child():
                grand_parent = self.__zig_zag(child)
            # right -> left
            elif not parent.is_left_child() and child.is_left_child():
                grand_parent = self.__zag_zig(child)
            # right -> right
            else:
                grand_parent = self.__zag_zag(child)
            if grand_parent.get_parent() is not None:
                root = self.__splaying(grand_parent)
            else:
                root = grand_parent
        return root
    
    
    def _splay(self, start_node):
        """
        Splays the given subtree whose root is the given `start_node` object.
        Splaying means "moving the node to the root". And this operation is done
        after searching, insertion and deletion.

        Parameters
        ----------
        start_node: BSTNode()
            A reference to the root of the subtree.
        """
        self._root = self.__splaying(start_node)


    ##############################     SEARCH     ##############################
    def __contains__(self, find_val):
        """
        Searches the `SplayTree()` for the given value and returns `True` if the 
        value exists and `False` if not.

        Parameters
        ----------
        find_val: int or float
            The value to be searched for in the `SplayTree()` instance.
        
        Returns
        -------
        bool:
            Returns `True` if the value exists in the `SplayTree()` instance and
            `False` if not.
        
        Example
        -------
        >>> stree = SplayTree.from_iterable([[2, 5, 4, 6, 3])
        >>> stree
          3__
         /   \\
        2     5
             / \\
            4   6
        >>> 5 in stree
        True
        >>> stree
            __5
           /   \\
          3     6
         / \\
        2   4
        >> 50 in bst
        False
        >>> stree
                6
               /
            __5
           /
          3
         / \\
        2   4

        Note
        ----
        As you can see from the previous example, the `SplayTree()` instance
        changes its structure each time we search for a certain value. If the
        value if found, the found node will be moved to the root. If the value
        isn't found, the last accessed node will be moved to the root. And
        that's what happended when searching for `50`, the last accessed value 
        which is the greatest value (`6`) in the splay tree is moved to the
        root.
        """
        super()._validate_item(find_val)
        node = super()._search(find_val, self._root)
        self._splay(node)
        return node.get_data() == find_val


    ##############################   INSERTION    ##############################
    def insert(self, value):
        super()._validate_item(value)
        if self.is_empty():
            self._root = super()._basic_node(value)
            self._length += 1
        else:
            new_node = super()._insert(value)
            self._splay(new_node)


    ##############################    REMOVAL     ##############################
    def remove(self, del_value):
        super()._validate_item(del_value)
        node = super()._remove(del_value, self._root)
        self._splay(node)


if __name__ == "__main__":
    st = SplayTree.from_iterable([8, 5, 2, 7, 15, 10, 3])
    print(st)