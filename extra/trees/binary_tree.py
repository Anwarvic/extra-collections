"""
A binary tree is a non-linear data structure that stores elements hierarchical.
With the exception of the top element, each element in the binary tree has a
parent element and zero or one or two children elements. We typically call the
top element the root of the binary tree, but it is drawn as the highest element, 
with the other elements being connected below (just the opposite of an actual
tree). In other words, we can consider the binary tree a tree data structure with the
only exception that every tree node in the binary tree has at most two children
while every tree node in the tree can have more than two children.

So, the following is a simple binary tree that represents a small family:

.. code-block::

              ___________GrandFather_________              <--- level 0
             /                               \\
         _Father___                      ___Uncle__        <--- level 1
        /          \\                   /           \\
      You        Sibling             Cousin1      Cousin2  <--- level 2

In the previous binary tree, we can say the following:

- "GrandFather" tree node has no parent.
- "Father" is left child of the "GrandFather" and "Uncle" is the right child.
- "Father" is the parent of both "You" and "Sibling" which means that "You" \
    and "Sibling" are the two children of "Father".
- Same goes for "Cousin1" and "Cousin2" as they are the children of "Uncle"; \
    and "Uncle" is their parent.
- "You", "Sibling", "Cousin1" and "Cousin2" have no children.


Now, let's try to use the previous tree to explain a few terms:

- **Tree Node**: Each entry in the binary tree data structure is called a tree \
    node. So, "GrandFather", "Father", "You", ... "Cousin" are all tree nodes. \
    So, the number of nodes in the previous binary tree is 7.
- **Root**: The root is the first tree node in the tree and it's the only \
    treenode that has no *parent*. So, "GrandFather" is the root of the \
    previuos tree.
- **Leaf Node**: The leaf node is a tree node that has no children. So, both \
    "You", "Sibling", "Cousin1" and "Cousin2" are leaf nodes. So, the number \
    of leaf nodes in the previous tree is 4.
- **Height**: The tree height is the number of edges between the root and the \
    furthest leaf node. In this case, the tree height is just 2.
- **Depth**: The depth of a tree node is the number of edges between this tree \
    node and the root. So, the depth of the tree's root is always 0.
- **Balanced Tree**: A binaryTree is said to be balanced if the difference \
    between the depth of any two leaf nodes is less than or equal one.
- **Perfect Tree**: A binaryTree is said to be perfect if all its levels are \
    completely filled.
- **Strict Tree**: A binaryTree is said to be strict if all its non-leaf nodes \
    has left and right children.
- **Traversal**: Traversal is the process to visit all nodes of a binary tree \
    starting from the root as we cannot randomly access any node in a binary \
    tree. There are four ways which we use to traverse a binary tree:

    - **Pre-order Traversal**: It's also known as "Depth-first Traversal" \
        where the **parent** is visited first. Then, the **left subtree** \
        (if found), then the **right subtree** (if found). So, the pre-order \
        traversal of the previous binary tree will be: \

            GrandFather ⟶ Father ⟶ Me ⟶ Sibling ⟶ Uncle ⟶ Cousin1 ⟶ Cousin2
        
    - **In-order Traversal**: The **left subtree** (if found) is visited first. \
        Then, the **parent** then the **right subtree** (if found). So, the \
        in-order traversal of the previous binary tree will be: \

            Me ⟶ Father ⟶ Sibling ⟶ GrandFather ⟶ Cousin1 ⟶ Uncle ⟶ Cousin2
        
    - **Post-order Traversal**: The **left subtree** (if found) is visited \
        first. Then, the **right subtree** (if found) then the **parent**. So, \
        the post-order traversal of the previous binary tree will be: \

            Me ⟶ Sibling ⟶ Father ⟶ Cousin1 ⟶ Cousin2 ⟶ Uncle ⟶ GrandFather
        
    - **Breadth-order Traversal**: It's also known as "Level-order Traversal" \
        where all nodes is visited by the order of the level they are in. So, \
        tree nodes in the first level are visited before all tree nodes in the \
        second level and so on. So, the breadth-first traversal of the previuos \
        binary tree will be: \

            GrandFather ⟶ Father ⟶ Uncle ⟶ Me ⟶ Sibling ⟶ Cousin1 ⟶ Cousin2


The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.

+--------------------------+----------------------------------------------------+------------+---------+
| Method                   | Description                                        | Worst-case | Optimal |
+==========================+====================================================+============+=========+
| __len__()                | Returns the number of nodes.                       | O(n)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_empty()               | Checks if object is empty.                         | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __repr__()               | Represents the object.                             | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __iter__()               | Iterates over the object.                          | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| __contains__()           | Checks the existence of the given item.            | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_height()             | Gets the tree's height.                            | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_depth()              | Gets the tree's depth.                             | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| get_nodes()              | Returns a list of all nodes per level.             | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_balanced()            | Checks if the binary tree is balanced.             | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_perfect()             | Checks if the binary tree is perfect.              | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| is_strict()              | Checks if the binary tree is strict.               | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| count_leaf_nodes()       | Counts all leaf nodss in the tree.                 | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| clear()                  | Clears the whole tree instance.                    | O(1)       | O(1)    |
+--------------------------+----------------------------------------------------+------------+---------+
| to_list()                | Converts the bianry tree instance to list.         | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| traverse()               | Traverses the binary tree based on given method.   | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| preorder_traverse()      | Traverses the binary tree in an pre-order manner.  | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| inorder_traverse()       | Traverses the binary tree in an in-order manner    | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| postorder_traverse()     | Traverses the binary tree in an post-order manner. | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| breadth_first_traverse() | Traverses the binary tree level by level.          | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+
| depth_first_traverse()   | Traverses the binary tree in an pre-order manner.  | O(n)       | O(n)    |
+--------------------------+----------------------------------------------------+------------+---------+

Class Documentation
===================
Here are all of the public methods that can be used with `BinaryTree()` objects:

"""
import warnings
from extra.trees.tree import TreeNode, Tree




class BinaryTreeNode(TreeNode):
    """
    A binary tree node is the basic unit for building binary trees. A binary 
    tree node must contain a value and this value can't be `None`. Each binary 
    tree node has either zero, one or two children binary tree nodes.
    The node that has no children is called a **leaf node**.
    """
    __name__ = "extra.BinaryTreeNode()"
    
    
    def __init__(self, value):
        """
        Creates a `BinaryTreeNode()` object which is the basic unit for building 
        BinaryTree() objects!!

        Parameters
        ----------
        value: object
            The value to be saved within the ` BinaryTreeNode()` instance

        Raises
        ------
        ValueError: If the given item is `None`.
        TypeError: If the given item is an `Extra()` object.
        """
        super().__init__(value)
        self._left = self._right = None
        del self._children


    def get_left(self):
        """
        Returns the left-child of the current `BinaryTreeNode()` instance.

        Returns
        -------
        object:
            The object stored in the `BinaryTreeNode()`.
        """
        return self._left


    def get_right(self):
        """
        Returns the right-child of the current `BinaryTreeNode()` instance.

        Returns
        -------
        object:
            The object stored in the `BinaryTreeNode()`.
        """
        return self._right


    def get_children(self):
        """
        Returns a list of all the children of the current `BinaryTreeNode()`
        instance.

        Returns
        -------
        list:
            A list of all the children of the `BinaryTreeNode()` instance.
        """
        children = []
        if self._left is not None: children.append(self._left)
        if self._right is not None: children.append(self._right)
        return children


    def set_children(self, lst):
        raise NotImplementedError(
            "You can use `set_left()` or `set_right()` methods instead!!"
        )


    def set_left(self, new_node):
        """
        Sets the given `BinaryTreeNode()` as a left child for the current
        `BinaryTreeNode()`.

        Parameters
        ----------
        child: BinaryTreeNode()
            The `BinaryTreeNode()` that will be a left child for the current one.

        Raises
        ------
        TypeError: If the given item is not an `BinaryTreeNode()` object.
        """
        if not isinstance(new_node, BinaryTreeNode):
            raise TypeError(
                f"You can't set a child unless it's an `{self.__name__}` " + 
                "object!!"
            )
        self._left = new_node


    def set_right(self, new_node):
        """
        Sets the given `BinaryTreeNode()` as a right child for the current
        `BinaryTreeNode()`.

        Parameters
        ----------
        child: BinaryTreeNode()
            The `BinaryTreeNode()` that will be a right child for the current one.

        Raises
        ------
        TypeError: If the given item is not an `BinaryTreeNode()` object.
        """
        if not isinstance(new_node, BinaryTreeNode):
            raise TypeError(
                f"You can't set a child unless it's an `{self.__name__}` " + 
                "object!!"
            )
        self._right = new_node
        

    def has_one_child(self):
        """
        Checks if the current `BinaryTreeNode()` has only one child. This child
        can be the left or the right one.

        Returns
        -------
        bool:
            `True` if the current `BinaryTreeNode()` has only one child. `False`
            if it has either zero or two children.
        """
        return not super().is_leaf() \
                and (self._left is None or self._right is None)


    def __repr__(self):
        """
        Represents `BinaryTreeNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `BinaryTreeNode()` instance.
        
        Example
        -------
        >>> x = BinaryTreeNode(10)
        >>> x
        >>> BinaryTreeNode(10)
        """
        return f"BinaryTreeNode({self._data})"


    def _represent(self):
        """
        A helpful function used to represent the `BinaryTreeNode()` instance
        when printing. It's used with BinaryTree.__repr__() method
        
        Returns
        -------
        str:
            A string representing the `BinaryTreeNode()` is a very simple way.
        
        Example
        -------
        >>> x = BinaryTreeNode(10)
        >>> x
        BinaryTreeNode(10)
        >>> x._represent()
        10
        >>> type(x._represent())
        <class 'str'>
        """
        return str(self._data)




class BinaryTree(Tree):
    """
    A binary tree is a non-linear data structure that can be defined recursively
    using a collection of `BinaryTreeNode()` instances, where each node has 
    either zero, one or two references to the children `BinaryTreeNode()`
    instances.
    """
    _basic_node = BinaryTreeNode
    __name__ = "extra.BinaryTree()"

    
    def __init__(self):
        """
        Creates an empty `BinaryTree()` object!!
        
        Example
        -------
        >>> t = BinaryTree()
        >>> type(t)
        <class 'extra.trees.binary_tree.BinaryTree'>
        """
        super().__init__()
    

    @staticmethod
    def __create_subtree(lst):
        """
        Creates a `BinaryTree()` instance from a nested list where the each 
        element has a nested list represening a subtree where the first 
        element in the parent and the second element is the left subtree and the
        third element is the right subtree.

        Parameters
        ----------
        lst: list or tuple
            A list or tuple object representing the tree in a linear-form.
        
        Returns
        -------
        BinaryTreeNode():
            The root of the `BinaryTree()` instance formed from parsing the 
            given object.
        
        Raises
        ------
        ValueError: If the given object can't be parsed
        """
        if type(lst) not in {list, tuple}: lst = [lst]
        if len(lst) == 0 or len(lst) >= 4:
            raise ValueError(f"Given {type(lst)} can not be parsed!!")
        try:
            parent = BinaryTreeNode(lst[0])
            parent.set_left( BinaryTree.__create_subtree(lst[1]) )
            parent.set_right( BinaryTree.__create_subtree(lst[2]) )
        except IndexError:
            pass
        return parent


    @staticmethod
    def parse(lst):
        """
        A static method that Creates a `BinaryTree()` instance from a nested
        list where the each element has a nested list represening a subtree 
        where the first element in the parent and the second element is the
        left subtree and the third element is the right subtree.

        Parameters
        ----------
        lst: list or tuple
            A list or tuple object representing the tree in a linear-form.
        
        Returns
        -------
        BinaryTreeNode():
            The root of the `BinaryTree()` instance formed from parsing the 
            given object.
        
        Raises
        ------
        ValueError: If the given object can't be parsed
        
        Example
        -------
        >>> lst = ["PP", ["ADP", "in"], ["NP", ["PRON", "our"], ["Noun", "home"]]]
        >>> btree = BinaryTree.parse(lst)
        >>> btree
              _PP_________
             /            \\
          _ADP           __NP______
         /              /          \\
        in           _PRON       __Noun
                    /           /
                  our         home
        """
        if type(lst) not in {list, tuple}:
            raise TypeError("Given object must be a `list` or `tuple`!!")
        bt = BinaryTree()
        bt._root = BinaryTree.__create_subtree(lst)
        return bt


    ##############################     PRINT      ##############################
    def __print_subtree(self, root, curr_index):
        """
        src: https://github.com/joowani/binarytree/blob/master/binarytree
        """
        if root is None:
            return [], 0, 0, 0
        else:
            line1 = []
            line2 = []
            node_repr = root._represent()
            new_root_width = gap_size = len(node_repr)

            # Get the left and right sub-boxes, their widths, and root repr positions
            l_box, l_box_width, l_root_start, l_root_end = \
                self.__print_subtree(root.get_left(), 2 * curr_index + 1)
            r_box, r_box_width, r_root_start, r_root_end = \
                self.__print_subtree(root.get_right(), 2 * curr_index + 2,)

            # Draw the branch connecting the current root node to the left sub-box
            # Pad the line with whitespaces where necessary
            if l_box_width > 0:
                l_root = (l_root_start + l_root_end) // 2 + 1
                line1.append(' ' * (l_root + 1))
                line1.append('_' * (l_box_width - l_root))
                line2.append(' ' * l_root + '/')
                line2.append(' ' * (l_box_width - l_root))
                new_root_start = l_box_width + 1
                gap_size += 1
            else:
                new_root_start = 0

            # Draw the representation of the current root node
            line1.append(node_repr)
            line2.append(' ' * new_root_width)

            # Draw the branch connecting the current root node to the right sub-box
            # Pad the line with whitespaces where necessary
            if r_box_width > 0:
                r_root = (r_root_start + r_root_end) // 2
                line1.append('_' * r_root)
                line1.append(' ' * (r_box_width - r_root + 1))
                line2.append(' ' * r_root + '\\')
                line2.append(' ' * (r_box_width - r_root))
                gap_size += 1
            new_root_end = new_root_start + new_root_width - 1

            # Combine the left and right sub-boxes with the branches drawn above
            gap = ' ' * gap_size
            new_box = [''.join(line1), ''.join(line2)]
            for i in range(max(len(l_box), len(r_box))):
                l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
                r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
                new_box.append(l_line + gap + r_line)

            # Return the new box, its width and its root repr positions
            return new_box, len(new_box[0]), new_root_start, new_root_end


    def _print_empty_tree(self):
        """
        Prints the `BinaryTree()` instance when it's empty.

        Returns
        -------
        str
            A string representing an empty `BinaryTree()` instance.

        Raises
        ------
        AssertionError: In case the `BinaryTree()` instance isn't empty!!

        Example
        -------
        >>> btree = BinaryTree()
        >>> btree
        / \\
        """
        return "/ \\"


    def __repr__(self):
        """
        Represents the `BinaryTree()` instance as a string.
        
        Returns
        -------
        str:
            The string-representation of the `BinaryTree()` instance.

        Example
        -------
        >>> btree = BinaryTree()
        >>> btree
        / \\
        >>> # the following is a simple family tree
        >>> root = BinaryTreeNode("GrandFather")
        >>> left_child = BinaryTreeNode("Father")
        >>> left_child.set_left(BinaryTreeNode("You"))
        >>> left_child.set_right(BinaryTreeNode("Sibling"))
        >>> root.set_left(left_child)
        >>>
        >>> right_child = BinaryTreeNode("Uncle")
        >>> righ_child.set_left(BinaryTreeNode("Cousin1"))
        >>> righ_child.set_right(BinaryTreeNode("Cousin2"))
        >>> root.set_right(right_child)
        >>> btree._root = root
        >>> btree
        
                ___________GrandFather_________
               /                               \\
           _Father___                      ___Uncle__
          /          \\                   /           \\
        You        Sibling             Cousin1      Cousin2
        """
        if self.is_empty():
            return self._print_empty_tree()
        lines, _, _, _ = self.__print_subtree(self._root, 0)
        return '\n'.join((line.rstrip() for line in lines[:-1]))


    ##############################    BALANCED    ##############################
    def is_balanced(self):
        """
        Checks if the `BinaryTreeNode()` instance is balanced. A binary tree is
        balanced if the difference between the depth of any two leaf nodes is
        less than or equal to one.

        Returns
        -------
        bool:
            `True` if the `BinaryTree()` instance is balanced and `False` if it
            is not balanced.
        
        Raises
        ------
        UserWarning: If the `BinaryTree()` is empty.

        Example
        -------
        >>> btree = BinaryTree.parse([1, [2, 4, 5], [3]])
        >>> btree
            __1__
           /     \\
          2       3
         / \\
        4   5
        >>> btree.is_balanced()
        True
        """
        if self.is_empty():
            warnings.warn(
                    f"You are checking the balance of an empty `{self.__name__}`",
                    UserWarning
                )
            return True
        left_depth = 0 if self._root.get_left() is None \
                        else 1 + super()._get_depth(self._root.get_left()) 
        right_depth = 0 if self._root.get_right() is None \
                        else 1 + super()._get_depth(self._root.get_right()) 
        return abs(left_depth - right_depth) <= 1


    ##############################    PERFECT     ##############################
    def is_perfect(self):
        """
        Checks if the `BinaryTreeNode()` instance is perfect. A binary tree is
        perfect if all its levels are completely filled.

        Returns
        -------
        bool:
            `True` if the `BinaryTree()` instance is perfect and `False` if it
            is not perfect.
        
        Raises
        ------
        UserWarning: If the `BinaryTree()` is empty.

        Example
        -------
        >>> btree = BinaryTree.parse([1, [2, 4, 5], [3]])
        >>> btree
            __1__
           /     \\
          2       3
         / \\
        4   5
        >>> btree.is_perfect()
        False
        >>> btree = BinaryTree.parse([1, [2, 4, 5], [3, 6, 7]])
        >>> btree
            __1__
           /     \\
          2       3
         / \\    / \\     
        4   5    6  7
        >>> btree.is_perfect()
        True
        """
        if self.is_empty():
            warnings.warn(\
                f"You are checking the perfection of an empty `{self.__name__}`",
                UserWarning)
            return True
        for level, nodes in enumerate(self.get_nodes_per_level()):
            if 2**level != len(nodes):
                return False
        return True


    ##############################     STRICT     ##############################
    def __is_subtree_strict(self, start_node):
        """
        Checks if the given binary subtree defined by the given `start_node` is
        strict. A binary tree is strict if all its non-leaf nodes has two 
        children (left and right).

        Returns
        -------
        bool:
            `True` if the `BinaryTree()` instance is perfect and `False` if it
            is not perfect.
        
        Raises
        ------
        AssertionError: If the given `start_node` is not `None` and it's not
        a `BinaryTreeNode()` object.
        """
        assert start_node is None or isinstance(start_node, self._basic_node)

        left_node = start_node.get_left()
        right_node = start_node.get_right()

        if left_node is None and right_node is None:
            return True
        elif left_node is not None and right_node is None:
            return False
        elif left_node is None and right_node is not None:
            return False
        else:
            return self.__is_subtree_strict(start_node.get_left()) and \
                    self.__is_subtree_strict(start_node.get_right())


    def is_strict(self):
        """
        Checks if the `BinaryTreeNode()` instance is perfect. A binary tree is
        perfect if all its all its non-leaf nodes has two children (left and 
        right).

        Returns
        -------
        bool:
            `True` if the `BinaryTree()` instance is strict and `False` if it
            is not strict.
        
        Raises
        ------
        UserWarning: If the `BinaryTree()` is empty.

        Example
        -------
        >>> btree = BinaryTree.parse([1, [2, 4, 5], [3]])
        >>> btree
            __1__
           /     \\
          2       3
         / \\
        4   5
        >>> btree.is_strict()
        True
        """
        if self.is_empty():
            warnings.warn(
                f"You are checking the strictness of an empty `{self.__name__}`",
                UserWarning
            )
            return True
        return self.__is_subtree_strict(self._root)


    ##############################   Pre-Order    ##############################
    def __preorder_traverse(self, start_node):
        
        assert start_node is None or isinstance(start_node, self._basic_node)

        nodes = []
        if start_node != None:
            nodes.append(start_node.get_data())
            if start_node.get_left():
                nodes.extend(self.__preorder_traverse(start_node.get_left()))
            if start_node.get_right():
                nodes.extend(self.__preorder_traverse(start_node.get_right()))
        return nodes


    def preorder_traverse(self):
        """
        Traverses the `BinaryTree()` instance in pre-order manner. Which means
        that the **parent** is visited first. Then, the **left subtree** (if
        found), then the **right subtree** (if found). 
        
        Note
        -----
        It's the same as depth_first_traverse() method.

        Returns
        --------
        list:
            A list of all values of the pre-order visited nodes.
        
        Example
        -------
        >>> btree = BinaryTree.parse([1, [2, 4, 5], [3, 6, 7]])
        >>> btree
            __1__
           /     \\
          2       3
         / \\    / \\     
        4   5    6  7
        >>> btree.preorder_traverse()
        [1, 2, 4, 5, 3, 6, 7]
        """
        return self.__preorder_traverse(self._root)


    def depth_first_traverse(self):
        return self.__preorder_traverse(self._root)


    ##############################   Post-Order   ##############################
    def __postorder_traverse(self, start_node):
        assert start_node is None or isinstance(start_node, self._basic_node)

        nodes = []
        if start_node != None:
            if start_node.get_left():
                nodes.extend(self.__postorder_traverse(start_node.get_left()))
            if start_node.get_right():
                nodes.extend(self.__postorder_traverse(start_node.get_right()))
            nodes.append(start_node.get_data())
        return nodes


    def postorder_traverse(self):
        return self.__postorder_traverse(self._root)


    ##############################    In-Order    ##############################
    def __inorder_traverse(self, start_node):
        assert start_node is None or isinstance(start_node, self._basic_node)
        
        nodes = []
        if start_node != None:
            if start_node.get_left():
                nodes.extend(self.__inorder_traverse(start_node.get_left()))
            nodes.append(start_node.get_data())
            if start_node.get_right():
                nodes.extend(self.__inorder_traverse(start_node.get_right()))
        return nodes


    def inorder_traverse(self):
        return self.__inorder_traverse(self._root)


    ##############################  BREADTH-FIRST ##############################
    def breadth_first_traverse(self):
        return super().to_list()


    ##############################    TRAVERSE    ##############################
    def traverse(self, method='inorder'):
        trav_methods = {"inorder", "postorder", "preorder", "depth-first",
                        "breadth-first"}
        if type(method) != str:
            raise TypeError("Given traverse method has to be one of these:\n"+\
                        str(trav_methods))
        # traverse based on given method
        method = method.lower()
        if method == 'inorder':
            return self.inorder_traverse()
        elif method == 'postorder':
            return self.postorder_traverse()
        elif method in {"preorder", "depth-first"}:
            return self.preorder_traverse()
        elif method == "breadth-first":
            return self.breadth_first_traverse()
        else:
            raise ValueError("Given traverse method has to be one of these:\n"+\
                        str(trav_methods))


if __name__ == "__main__":
    root = BinaryTreeNode("GrandFather")
    root.set_left(BinaryTreeNode("Father"))
    root.get_left().set_left(BinaryTreeNode("Me"))
    root.get_left().set_right(BinaryTreeNode("Sibling"))
    root.set_right(BinaryTreeNode("Uncle"))
    root.get_right().set_left(BinaryTreeNode("Cousin1"))
    root.get_right().set_right(BinaryTreeNode("Cousin2"))
    btree = BinaryTree()
    btree._root = root
    print(btree)
    print(btree.preorder_traverse())
    print(" ⟶ ".join(btree.inorder_traverse()))
    print(" ⟶ ".join(btree.postorder_traverse()))
    print(" ⟶ ".join(btree.breadth_first_traverse()))