"""
A tree is a non-linear data structure that stores elements hierarchically. With
the exception of the top element, each element in a tree has a parent element
and zero or more children elements. We typically call the top element the root
of the tree, but it is drawn as the highest element, with the other elements
being connected below (just the opposite of an actual tree).

The following is a simple tree that represents the family-tree of Homer Simpson
from The Simpsons show :)

.. code-block::

    TheSimpsons
    └─┬ Abraham
      ├── Herb
      └─┬ Homer
        ├── Bart
        ├── Lisa
        └── Maggie

In the previous tree, we can say the following:

- "Abraham" is the **only child** of the "TheSimpsons".
- "Abraham" is the **parent** of both "Herb" and "Homer" which means that \
    "Herb" and "Homer" are the **two children** of "Abraham".
- Same goes for "Bart", "Lisa" and "Maggie" as they are the **three children** \
    of "Homer"; and "Homer" is their parent.
- "Bart", "Lisa" and "Maggie" have **no children**.
- As we can see, each entry in the tree can have *zero*, *one*, *two*, *three* \
    or even more children for each parent.

Now, let's try to use the previous tree to explain a few terms:

- **Tree Node**: Each entry in the tree data structure is called a tree node. \
    So, "TheSimpsons", "Abraham", "Herb", ... "Maggie" are all tree nodes. So,
    the number of nodes in the previous tree is 7.
- **Root**: The root is the first tree node in the tree and it's the only \
    treenode that has no *parent*. So, "TheSimpsons" is the root of the \
    previuos tree.
- **Leaf Node**: The leaf node is a tree node that has no children. So, both \
    "Bart", "Lisa" and "Maggie" are leaf nodes. So, the number of leaf nodes \
    in the previous tree is 3.
- **Height**: The tree height is the number of edges between the root and the \
    furthest leaf node. In this case, the tree height is 3.

The following table sums up all the different public functionality in this
class and also provides the worst-case time complexity along side with the
optimal time complexity that I will try to reach in future releases Insha'Allah.
Generally, we are going to use the following indicators in the table:

- **n** is the number of elements currently in the container.
- **k** is the value of a parameter.

+--------------------+------------------------------------------+------------+---------+
| Method             | Description                              | Worst-case | Optimal |
+====================+==========================================+============+=========+
| __len__()          | Returns the number of nodes              | O(n)       | O(1)    |
+--------------------+------------------------------------------+------------+---------+
| is_empty()         | Checks if object is empty                | O(1)       | O(1)    |
+--------------------+------------------------------------------+------------+---------+
| __repr__()         | Represents the object                    | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| __iter__()         | Iterates over the object                 | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| __contains__()     | Checks the existence of the given item   | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| get_height()       | Gets the tree's height                   | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| get_depth()        | Gets the tree's depth                    | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| get_nodes()        | Returns a list of all nodes per level    | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| count_leaf_nodes() | Counts all leaf nodss in the tree        | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+
| clear()            | Clears the whole tree instance           | O(1)       | O(1)    |
+--------------------+------------------------------------------+------------+---------+
| to_list()          | Converts the tree instance to  list.     | O(n)       | O(n)    |
+--------------------+------------------------------------------+------------+---------+


Class Documentation
===================
Here are all of the public methods that can be used with `Tree()` objects:
"""
import os
from extra.interface import Extra




class TreeNode(Extra):
    """
    A tree node is the basic unit for building Trees. A tree node must contain
    a value and this value can't be `None`. Each tree node has zero or more
    child tree nodes. The node that has no children is called a **leaf node**.
    """
    __name__ = "extra.TreeNode()"
    

    def __init__(self, value):
        """
        Creates a `TreeNode()` object which is the basic unit for building 
        Tree() objects!!

        Parameters
        ----------
        value: object
            The value to be saved within the `TreeNode()` instance

        Raises
        ------
        ValueError: If the given item is `None`.
        TypeError: If the given item is an `Extra()` object.
        """
        super()._validate_item(value)
        if type(value) == str:
            value = value.replace('\n', '\\n')
        self._data = value
        self._children = []


    def get_data(self):
        """
        Returns the data stored in the `TreeNode()` instance.

        Returns
        -------
        object:
            The object stored in the `TreeNode()`.
        """
        return self._data


    def get_children(self):
        """
        Returns a list of all the children TreeNode() instances.

        Returns
        -------
        list:
            A list of all the children TreeNode() instances.
        """
        return self._children
    

    def set_child(self, child):
        """
        Sets the given `TreeNode()` as a child for the current `TreeNode()`.

        Parameters
        ----------
        child: TreeNode()
            The `TreeNode()` that will be a child for the current one.

        Raises
        ------
        TypeError: If the given item is not an `TreeNode()` object.
        """
        if not isinstance(child, TreeNode):
            raise TypeError(
                f"You can't set a child unless it's an `{self.__name__}` " + 
                "object!!"
            )
        self._children.append(child)
    
    
    def set_children(self, lst):
        """
        Sets multiple `TreeNode()` instances as children for the current one.

        Parameters
        ----------
        lst: iterable (list, tuple, ...)
            A list of the `TreeNode()` instances that will be set as children to
            the current `TreeNode()`.

        Raises
        ------
        TypeError: This can be raised in either of these two cases:
            1. If the given object isn't iterable.
            2. If the given object has an element which isn't a `TreeNode()` \
                instance.
        """
        if not hasattr(lst, "__iter__"):
            raise TypeError("Given object isn't iterable!!")
        children = []
        for item in lst:
            if not isinstance(item, TreeNode):
                raise TypeError(
                    f"You can't set a child unless it's an `{self.__name__}` " + 
                    "object!!"
                )
            children.append(item)
        self._children = children
    

    def is_leaf(self):
        """
        Checks if the current `TreeNode()` instance is a leaf node. A leaf node
        is a tree node that has no children.

        Returns
        -------
        bool:
            `True` if the current `TreeNode()` has no children and `False`
            otherwise.
        """
        return self.get_children() == []
        

    def __repr__(self):
        """
        Represents `TreeNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `TreeNode()` instance.
        
        Example
        -------
        >>> x = TreeNode(10)
        >>> x
        >>> TreeNode(10)
        """
        return f"TreeNode({self._data})"


    @staticmethod
    def swap(node1, node2):
        """
        A static method to swap the data within the given two `TreeNode()`
        instances.

        Parameters
        ----------
        node1: TreeNode()
            The first `TreeNode()` instance whose data should be swapped.
        node2: TreeNode()
            The second `TreeNode()` instance whose data should be swapped.

        Raises
        ------
        TypeError: If one of the given instances isn't a `TreeNode()` object.

        Example
        -------
        >>> x = TreeNode(10)
        >>> y = TreeNode(20)
        >>>
        >>> TreeNode.swap(x, y)
        >>> x
        TreeNode(20)
        >>> y
        TreeNode(10)
        >>>
        >>> TreeNode.swap(x, 10)
        TypeError: Incompitable objects' type preventing swapping!!
        """
        if not isinstance(node1, TreeNode) or not isinstance(node2, TreeNode):
            raise TypeError(f"Incompitable objects' type preventing swapping!!")
        node1._data, node2._data = node2._data, node1._data




class Tree(Extra):
    """
    A tree is a non-linear data structure that can be defined recursively using
    a collection of `TreeNode()` instances, where each node has a list of
    references to the children TreeNode() instances.
    """
    __name__ = "extra.Tree()"
    

    def __init__(self):
        """
        Creates an empty `Tree()` object!!
        
        Example
        -------
        >>> t = Tree()
        >>> type(t)
        <class 'extra.trees.tree.Tree'>
        """
        self._root = None
    

    @staticmethod
    def __form_tree_from_path(parent_abs_path, curr_folder):
        """
        Creates a `Tree()` instance of the content of a given directory. Each
        path/file in each sub-directory will be represented as a `TreeNode()`
        instance.

        Parameters
        ----------
        parent_abs_path: str
            The absolute path of the parent of the current directory.
        curr_folder: str
            The name of the current directory
        
        Returns
        -------
        TreeNode()
            A tree node representing the root of the hierarchy of the 
            `curr_folder` directory.
        
        Raises
        ------
        AssertionError: This can be raised if either of the two parameters
        weren't string.
        """
        assert type(parent_abs_path) == str
        assert type(curr_folder) == str

        node = TreeNode(curr_folder)
        abs_path = os.path.join(parent_abs_path, curr_folder)
        if os.path.isdir(abs_path):
            for child in sorted( os.listdir(abs_path) ):
                node.set_child(Tree.__form_tree_from_path(abs_path, child))
        return node


    @staticmethod
    def from_path(path):
        """
        Creates a `Tree()` instance of the hierarchy of a given directory/path.
        Each file in each sub-directory will be represented as a `TreeNode()`
        instance.

        Parameters
        ----------
        path: str
            The path which will be the root of the returned `Tree()` object.

        Returns
        ------
        Tree()
            The `Tree()` object representing the hierarchy of the given path.
        
        Raises
        ------
        TypeError: If the given path was invalid.

        Example
        -------
        >>> Tree.from_path("example")
        trees
        ├── script.py
        ├─┬ folder
        │ ├── file.txt
        │ ├── file2.txt
        │ └── file3.txt
        ├── script2.py
        └── script3.py
        """
        if type(path) != str or not os.path.exists(path):
            raise TypeError("Invalid path was given!!")
        t = Tree()
        abs_path = os.path.abspath(path)
        parent, folder = os.path.split(abs_path)
        t._root = Tree.__form_tree_from_path(parent, folder)
        return t


    ##############################     LENGTH     ##############################
    def __len__(self):
        """
        Gets the length of the `Tree()` instance in time-complexity of O(n) 
        where **n** is the number of nodes in the tree.
        
        Returns
        -------
        int:
            The length of the `Tree()` instance. Length is the number of tree
            nodes in the instance.
        
        Examples
        --------
        >>> t = Tree()
        >>> len(t)
        0
        >>> x = TreeNode(2021)
        >>> y = TreeNode("hello")
        >>> z = TreeNode("world")
        >>> x.set_children([y, z])
        >>> t._root = x
        >>> t
        2021
        ├── hello
        └── world
        >>> len(t)
        3
        """
        if self.is_empty():
            return 0
        return self.__count_nodes(self._root)


    def is_empty(self):
        """
        Checks if the `Tree()` instance is empty or not in time-complexity of
        O(1).
        
        Returns
        -------
        bool:
            A boolean flag showing if the Tree() instance is empty or not.
            `True` shows that this instance is empty and `False` shows it's
            not empty.
        
        Example
        --------
        >>> t = Tree()
        >>> t.is_empty()
        True
        >>> t._root = TreeNode(1)
        >>> t.is_empty()
        False
        """
        return self._root is None
    

    def __count_nodes(self, start_node):
        assert isinstance(start_node, TreeNode)

        total_nodes = 1
        for child in start_node.get_children():
            total_nodes += self.__count_nodes(child)
        return total_nodes


    ##############################     PRINT      ##############################
    def __print_subtree(self, start_node, lines, is_last_child, seq=[]):
        """
        seq (list): is a boolean list containing values
        """
        line = []
        if seq:
            for is_parent_last_child in seq[1:]:
                line.append('  ') if is_parent_last_child else line.append('│ ')
            line.append('└─') if is_last_child else line.append('├─')
            line.append('┬ ')if start_node.get_children() else line.append('─ ')
        line.append(str(start_node.get_data()))
        lines.append("".join(line))
        # append node status
        my_seq = seq.copy()
        my_seq.append(is_last_child)
        # iterate over children
        children = start_node.get_children()
        num_children = len(children)
        for idx in range(num_children):
            child = children[idx]
            is_last_child = True if idx == num_children-1 else False
            self.__print_subtree(child, lines, is_last_child, my_seq)
        return lines


    def _print_empty_tree(self):
        return "--"


    def __repr__(self):
        if self.is_empty():
            return self._print_empty_tree()
        elif self._root.get_children():
            return "\n".join(self.__print_subtree(self._root, [], False))
        else:
            return str(self._root.get_data())


    ##############################  HEIGHT/DEPTH  ##############################
    def _get_height(self, start_node):
        assert isinstance(start_node, TreeNode)

        height = 0
        for child in start_node.get_children():
            height = max(height, 1 + self._get_height(child))
        return height
    

    def get_height(self):
        if self.is_empty():
            return 0
        return self._get_height(self._root)
    

    def _get_depth(self, start_node):
        assert isinstance(start_node, TreeNode)
        return self._get_height(self._root) - self._get_height(start_node)
        

    def get_depth(self):
        if self.is_empty():
            return 0
        return self._get_depth(self._root)
    

    ##############################   LEAF NODES   ##############################
    def _count_leaf_nodes(self, start_node):
        assert isinstance(start_node, TreeNode)

        if start_node.is_leaf():
            return 1
        total_nodes = 0
        for child in start_node.get_children():
            total_nodes += self._count_leaf_nodes(child)
        return total_nodes


    def count_leaf_nodes(self):
        if self.is_empty():
            return 0
        return self._count_leaf_nodes(self._root)


    ##############################      ITER      ##############################
    def __iter__(self):
        if self.is_empty():
            raise IndexError(f"Can't iterate over an empty `{self.__name__}`!!")
        current_nodes = [self._root]
        while len(current_nodes) > 0:
            next_nodes = []
            for node in current_nodes:
                yield node.get_data()
                next_nodes.extend(node.get_children())
            current_nodes = next_nodes


    def to_list(self):
        if self.is_empty():
            return []
        return [node for node in self]


    ##############################     SEARCH     ##############################
    def _search(self, value):
        queue = [self._root]
        while(queue):
            curr_node = queue.pop()
            if curr_node.get_data() == value:
                return curr_node
            queue.extend(curr_node.get_children())
        return None
            
    
    def __contains__(self, value):
        found_node = self._search(value)
        return True if found_node is not None else False


    ##############################      NODES     ##############################
    def _get_nodes_per_level(self,start_node,level,level_nodes,save_data=True):
        assert isinstance(start_node, TreeNode)
        assert type(level) == int and level >= 0
        assert type(level_nodes) == list
        
        if start_node is not None:
            if level == len(level_nodes):
                level_nodes.append([])
            if save_data:
                level_nodes[level].append(start_node.get_data())
            else:
                level_nodes[level].append(start_node)
            for child in start_node.get_children():
                self._get_nodes_per_level(child,level+1,level_nodes,save_data)
        return level_nodes


    def get_nodes(self):
        if self.is_empty():
            return []
        return self._get_nodes_per_level(self._root, 0, [], True)


    ##############################      CLEAR     ##############################
    def clear(self):
        self.__init__()
    
