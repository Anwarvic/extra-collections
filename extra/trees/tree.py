"""
A tree is a non-linear data structure that stores elements hierarchically. With
the exception of the top element, each element in a tree has a parent element
and zero or more children elements. We typically call the top element of the
tree, "the root". The root is drawn as the highest element, with the other
elements being connected below (just the opposite of an actual tree).

The following is a simple tree that represents the family-tree of Homer Simpson
from The Simpsons show :)

.. code-block:: text

    TheSimpsons
    └─┬ Abraham
      ├── Herb
      └─┬ Homer
        ├── Bart
        ├── Lisa
        └── Maggie

In the previous tree, we can say the following:

- "TheSimpsons" tree node has no parent.
- "Abraham" is the **only child** of the "TheSimpsons".
- "Abraham" is the **parent** of both "Herb" and "Homer" which means that \
    "Herb" and "Homer" are the **two children** of "Abraham".
- Same goes for "Bart", "Lisa" and "Maggie" as they are the **three \
    children** of "Homer"; and "Homer" is their parent.
- "Bart", "Lisa" and "Maggie" have **no children**.
- As we can see, each entry in the tree can have *zero*, *one*, *two*, \
    *three* or even more children for each parent.

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
- **Depth**: The depth of a tree node is the number of edges between this \
    tree node and the root. So, the depth of the tree's root is always 0.
"""
import os
from extra.interface import Extra


class TreeNode(Extra):
    """
    A tree node is the basic unit for building trees. A tree node must contain
    a value and this value can't be `None`. Each tree node has zero or more
    child tree nodes. The node that has no children is called a **leaf node**.
    """

    __name__ = "extra.TreeNode()"

    def __init__(self, value):
        """
        Creates a `TreeNode()` object which is the basic unit for building
        `Tree()` objects!!

        Parameters
        ----------
        value: object
            The value to be saved within the `TreeNode()` instance

        Raises
        ------
        ValueError:
            If the given item is `None`.
        TypeError:
            If the given item is an `Extra()` object.

        Examples
        --------
        >>> x = TreeNode(10)
        >>> x
        TreeNode(10)
        >>> type(x)
        <class 'extra.trees.tree.TreeNode'>

        You can't initialize a `TreeNode()` using a `None`

        >>> TreeNode(None)
        ValueError: Can't use `None` as an element within `extra.TreeNode()`!!
        """
        super()._validate_item(value)
        if type(value) == str:
            value = value.replace("\n", "\\n")
        self._data = value
        self._children = []

    def get_data(self):
        """
        Returns the data stored in the `TreeNode()` instance.

        Returns
        -------
        object:
            The object stored in the `TreeNode()`.

        Example
        -------
        >>> x = TreeNode(10)
        >>> x.get_data()
        10
        """
        return self._data

    def get_children(self):
        """
        Returns a list of all the children of the `TreeNode()` instance.

        Returns
        -------
        list:
            A list of all the children of the `TreeNode()` instance.

        Example
        -------
        >>> x = TreeNode(2021)
        >>> y = TreeNode("hello")
        >>> z = TreeNode("world")
        >>> x.set_child(y)
        >>> x.set_child(z)
        >>> x.get_children()
        [TreeNode(hello), TreeNode(world)]
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
        TypeError:
            If the given item is not an `TreeNode()` object.

        Example
        -------
        >>> x = TreeNode("hello")
        >>> x.set_child(TreeNode("world"))
        >>> x.set_child(TreeNode(2021))

        A child has to be a `TreeNode()` object:

        >>> x.set_child(20)
        TypeError: You can't set a child unless it's an `extra.TreeNode()` \
            object!!
        """
        if not isinstance(child, TreeNode):
            raise TypeError(
                f"You can't set a child unless it's an `{self.__name__}` "
                + "object!!"
            )
        self._children.append(child)

    def set_children(self, lst):
        """
        Sets multiple `TreeNode()` instances as children for the current one.

        Parameters
        ----------
        lst: iterable (list, tuple, ...)
            A list of the `TreeNode()` instances that will be set as children
            to the current `TreeNode()`.

        Raises
        ------
        TypeError:
            This can be raised in either of these two cases:
                1. If the given object isn't iterable.
                2. If the given object has an element which isn't a
                `TreeNode()` instance.

        Example
        -------
        >>> x = TreeNode("hello")
        >>> x.set_children([TreeNode("world"), TreeNode(2021)])

        A child has to be a `TreeNode()` object:

        >>> x.set_children([TreeNode("world"), 2021])
        TypeError: You can't set a child unless it's an `extra.TreeNode()` \
            object!!
        """
        if not hasattr(lst, "__iter__"):
            raise TypeError("Given object isn't iterable!!")
        children = []
        for item in lst:
            if not isinstance(item, TreeNode):
                raise TypeError(
                    f"You can't set a child unless it's an `{self.__name__}` "
                    + "object!!"
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

        Example
        --------
        >>> x = TreeNode("hello")
        >>> x.is_leaf()
        True
        >>> x.set_child(TreeNode("world"))
        >>> x.is_leaf()
        False
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
        TreeNode(10)
        """
        return f"TreeNode({self._data})"

    def _represent(self):
        """
        A helpful function used to represent the `TreeNode()` instance when
        printing. It's used with Tree.__repr__() method

        Returns
        -------
        str:
            A string representing the `TreeNode()` is a very simple way.

        Example
        -------
        >>> x = TreeNode(10)
        >>> x
        TreeNode(10)
        >>> x._represent()
        10
        >>> type(x._represent())
        <class 'str'>
        """
        return str(self._data)

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
        TypeError:
            If one of the given instances isn't a `TreeNode()` object.

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
            raise TypeError(
                "Incompitable objects' type preventing swapping!!"
            )
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
        AssertionError:
            This can be raised if either of the two parameters weren't string.
        """
        assert type(parent_abs_path) == str
        assert type(curr_folder) == str

        node = TreeNode(curr_folder)
        abs_path = os.path.join(parent_abs_path, curr_folder)
        if os.path.isdir(abs_path):
            for child in sorted(os.listdir(abs_path)):
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
        TypeError:
            If the given path's type wasn't a string.
        ValueError:
            If the given path doesn't exist.

        Example
        -------
        >>> # this can't be reproduced and it's for the sake of explanation.
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
        if type(path) != str:
            raise TypeError("Invalid path was given!!")
        elif not os.path.exists(path):
            raise ValueError("Invalid path was given!!")
        t = Tree()
        abs_path = os.path.abspath(path)
        parent, folder = os.path.split(abs_path)
        t._root = Tree.__form_tree_from_path(parent, folder)
        return t

    # =============================    LENGTH    ==============================
    def __count_nodes(self, start_node):
        """
        Recurrsively, cunts the number of `TreeNode()` instances found in the
        `Tree()` object.

        Parameters
        ----------
        start_node: TreeNode()
            The `TreeNode()` instance at which we are going to start counting
            the tree nodes. At the beginning, this will be the root of the
            `Tree()` instance.

        Returns
        -------
        int:
            The number of `TreeNode()` objects found in the `Tree()` instance.

        Raises
        ------
        AssertionError:
            If the given `start_node` isn't an `TreeNode()` object.
        """
        assert isinstance(start_node, TreeNode)

        total_nodes = 1
        for child in start_node.get_children():
            total_nodes += self.__count_nodes(child)
        return total_nodes

    def __len__(self):
        """
        Gets the length of the `Tree()` instance. Length is the number of nodes
        in the instance.

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
        Checks if the `Tree()` instance is empty or not in constant time.

        Returns
        -------
        bool:
            A boolean flag showing if the `Tree()` instance is empty or not.
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

    # =============================     PRINT    ==============================
    def __print_subtree(self, start_node, lines, is_last_child, seq=[]):
        """
        Prints the subtree starting at the given `start_node` parameter.

        Parameters
        ----------
        start_node: TreeNode()
            The TreeNode() at which the sub-tree printing begines
        lines: list
            A list of all lines that should be printed before printing the
            current subtree.
        is_last_child: bool
            A boolean value showing if the given `start_node` is the last
            child. `True` means that `start_node` is the last child.
        seq: list
            A list of boolean values saved showing earlier nodes being the last
            child.

        Returns
        -------
        list
            A list of all lines that should be printed to represent the whole
            subtree.

        Raises
        ------
        AssertionError:
            This can be raised in the following cases:
                1. The `start_node` isn't an instance of `TreeNode()`.
                2. The type of `lines` is not `list`.
                3. The `is_last_child` is not a boolean value.
                4. The type of `seq` variable isn't a `list`.

        TODO
        ----
        Refactor this method... it contains a lot redundant information.
        """
        assert isinstance(start_node, TreeNode)
        assert type(lines) == list
        assert type(is_last_child) == bool
        assert type(seq) == list

        line = []
        if seq:
            for is_parent_last_child in seq[1:]:
                (line.append("  ")
                    if is_parent_last_child
                    else line.append("│ "))
            line.append("└─") if is_last_child else line.append("├─")
            (line.append("┬ ")
                if start_node.get_children()
                else line.append("─ "))
        line.append(start_node._represent())
        lines.append("".join(line))
        # append node status
        my_seq = seq.copy()
        my_seq.append(is_last_child)
        # iterate over children
        children = start_node.get_children()
        num_children = len(children)
        for idx in range(num_children):
            child = children[idx]
            is_last_child = True if idx == num_children - 1 else False
            self.__print_subtree(child, lines, is_last_child, my_seq)
        return lines

    def _print_empty_tree(self):
        """
        Prints the `Tree()` instance when it's empty.

        Returns
        -------
        str
            A string representing an empty `Tree()` instance.

        Raises
        ------
        AssertionError:
            In case the `Tree()` instance isn't empty!!

        Example
        -------
        >>> t = Tree()
        >>> t
        --
        """
        assert self.is_empty()
        return "--"

    def __repr__(self):
        """
        Represents the `Tree()` instance as a string.

        Returns
        -------
        str:
            The string-representation of the `Tree()` instance.

        Example
        -------
        >>> t = Tree()
        >>> t
        --
        >>> # the following is "The Simpsons" family tree :)
        >>> abraham = TreeNode('Abraham')
        >>> herb = TreeNode('Herb')
        >>> homer = TreeNode('Homer')
        >>> abraham.set_children([herb, homer])
        >>> # homer-marge children
        >>> bart = TreeNode('Bart')
        >>> lisa = TreeNode('Lisa')
        >>> maggie = TreeNode('Maggie')
        >>> homer.set_children([bart, lisa, maggie])
        >>> root = TreeNode('TheSimpsons')
        >>> root.set_child(abraham)
        >>> t._root = root
        >>> t
        TheSimpsons
        └─┬ Abraham
          ├── Herb
          └─┬ Homer
            ├── Bart
            ├── Lisa
            └── Maggie
        """
        if self.is_empty():
            return self._print_empty_tree()
        elif self._root.get_children():
            return "\n".join(self.__print_subtree(self._root, [], False))
        else:
            return str(self._root.get_data())

    # ============================= HEIGHT/DEPTH ==============================
    def _get_height(self, start_node):
        """
        Gets the height of the subtree defined by the given `start_node`
        parameter. The tree's height is the number of edges between the given
        `start_node` and the furthest leaf node.

        Returns
        -------
        int:
            A positive integer representing the height of the given
            `start_node`.

        Raises
        ------
        AssertionError:
            If the given `start_node` isn't a `TreeNode()`

        Example
        -------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> t._get_height(t._root)
        2
        """
        assert isinstance(start_node, TreeNode)

        height = 0
        for child in start_node.get_children():
            height = max(height, 1 + self._get_height(child))
        return height

    def get_height(self):
        """
        Gets the height of the `Tree()` instance. The tree's height is the
        number of edges between the root and the furthest leaf node.

        Returns
        -------
        int:
            A positive integer representing the height of the instance.

        Example
        -------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> t.get_height()
        2
        """
        if self.is_empty():
            return 0
        return self._get_height(self._root)

    def _get_depth(self, start_node):
        """
        Gets the depth of the subtree defined by the `start_node` parameter.
        The tree's depth is the number of edges between the given `start_node`
        and the tree's root.

        Returns
        -------
        int:
            A positive integer representing the depth of the given
            `start_node`.

        Raises
        ------
        AssertionError:
            If the given `start_node` isn't a `TreeNode()`

        Example
        -------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> t._get_depth(t._root)
        0
        >>> t._get_depth(first_child)
        >>> 1
        """
        assert isinstance(start_node, TreeNode)
        return self._get_height(self._root) - self._get_height(start_node)

    def get_depth(self):
        """
        Gets the depth of the `Tree()` instance.

        Returns
        -------
        int:
            A positive integer representing the depth of the given `Tree()`.

        Example
        -------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> t.get_depth()
        0
        """
        if self.is_empty():
            return 0
        return self._get_depth(self._root)

    # =============================  LEAF NODES  ==============================
    def _count_leaf_nodes(self, start_node):
        """
        Counts the number of leaf nodes in the given subtree defined by the
        given `start_node` parameter. Leaf nodes are the tree nodes that have
        no children.

        Parameters
        ----------
        start_node: TreeNode()
            The `TreeNode()` which represents the root of the subtree whose
            leaf nodes will be counted.

        Returns
        -------
        int:
            A positive integer representing the number of leaf nodes in the
            subtree.

        Raises
        ------
        AssertionError:
            If the given `start_node` isn't a `TreeNode()`

        Example
        -------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> t._count_leaf_nodes(t._root)
        5
        >>> t._count_leaf_nodes(first_child)
        3
        >>> t._count_leaf_nodes(second_child)
        2
        """
        assert isinstance(start_node, TreeNode)

        if start_node.is_leaf():
            return 1
        total_nodes = 0
        for child in start_node.get_children():
            total_nodes += self._count_leaf_nodes(child)
        return total_nodes

    def count_leaf_nodes(self):
        """
        Counts the number of leaf nodes in the `Tree()` instance. Leaf nodes
        are the tree nodes that have no children.

        Returns
        -------
        int:
            A positive integer representing the number of leaf nodes in the
            `Tree()`.

        Example
        -------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> t.count_leaf_nodes()
        5
        """
        if self.is_empty():
            return 0
        return self._count_leaf_nodes(self._root)

    # =============================     ITER     ==============================
    def __iter__(self):
        """
        Iterates over the `Tree()` instance and returns a generator of the
        `TreeNode()` values in breadth-first manner.

        Yields
        ------
        object:
            The value stored at each node in the `Tree()` instance.

        Examples
        --------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> for value in t:
        ...     print(value)
        10
        100
        200
        1
        2
        3
        4
        5
        """
        if not self.is_empty():
            current_nodes = [self._root]
            while len(current_nodes) > 0:
                next_nodes = []
                for node in current_nodes:
                    yield node.get_data()
                    next_nodes.extend(node.get_children())
                current_nodes = next_nodes

    def to_list(self):
        """
        Converts the `Tree()` instance to a `list` where values will be
        inserted in breadth-first manner.

        Returns
        -------
        list:
            A `list` object containing the same elements as the `Tree()`
            instance.

        Example
        -------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> t.to_list()
        [10, 100, 200, 1, 2, 3, 4, 5]
        """
        if self.is_empty():
            return []
        return [node for node in self]

    # =============================    SEARCH    ==============================
    def _search(self, value):
        """
        Searches the `Tree()` for a given value and returns the node containing
        that value if found. If not found, it returns `None`.

        Parameters
        ----------
        value: object
            The value to be searched for in the `Tree()` instance.

        Returns
        -------
        TreeNode() or None:
            If the value is found, this object represents the found node. If
            the value isn't found, this object will be `None`.

        Examples
        --------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> t._search(100)
        TreeNode(100)
        >>> t._search(50)
        None
        """
        queue = [self._root]
        while queue:
            curr_node = queue.pop()
            if curr_node.get_data() == value:
                return curr_node
            queue.extend(curr_node.get_children())
        return None

    def __contains__(self, value):
        """
        Searches the `Tree()` for the given value and returns `True` if the
        value exists and `False` if not.

        Parameters
        ----------
        value: object
            The value to be searched for in the `Tree()` instance.

        Returns
        -------
        bool:
            Returns `True` if the value exists in the `Tree()` instance and
            `False` if not.

        Examples
        --------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> 100 in t
        True
        >>> 50 in t
        False
        """
        found_node = self._search(value)
        return True if found_node is not None else False

    # =============================     NODES    ==============================
    def _get_nodes_per_level(self, start_node, level, nodes, save_data=True):
        """
        Retreeves all treenodes within the subtree defined by `start_node`
        parameter so that all treenodes in a certain level will be concatenated
        into a standalone list.

        Parameters
        ----------
        start_node: TreeNode()
            The `TreeNode()` which is the root of the subtree.
        level: int
            A postive integer representing the level of `start_node`.
        nodes: list
            A list of all previous nodes.
        save_data: bool (default=True)
            A boolean value to choose either to save the `TreeNode()` data or
            the `TreeNode()` object itself. `True` means to save just the data.

        Returns
        -------
        list:
            A nested list where the first inner-list has all the tree nodes in
            the first level, the second inner-list has all the tree nodes in
            the second level, ... so on.
        """
        assert isinstance(start_node, TreeNode)
        assert type(level) == int and level >= 0
        assert type(nodes) == list

        if start_node is not None:
            if level == len(nodes):
                nodes.append([])
            if save_data:
                nodes[level].append(start_node.get_data())
            else:
                nodes[level].append(start_node)
            for child in start_node.get_children():
                self._get_nodes_per_level(child,
                                          level + 1,
                                          nodes,
                                          save_data)
        return nodes

    def get_nodes_per_level(self):
        """
        Retreeves all treenodes within the `Tree()` instance so that all
        treenodes in a certain level will be concatenated into a separate list.

        Returns
        -------
        list:
            A nested list where the first inner-list has all the tree nodes in
            the first level, the second inner-list has all the tree nodes in
            the second level, ... so on.

        Example
        -------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> t.get_nodes_per_level()
        [[10], [100, 200], [1, 2, 3, 4, 5]]
        """
        if self.is_empty():
            return []
        return self._get_nodes_per_level(self._root, 0, [], True)

    # =============================     CLEAR    ==============================
    def clear(self):
        """
        Removes all nodes within the `Tree()` instance in constant time.

        Example
        -------
        >>> t = Tree()
        >>> root = TreeNode(10)
        >>> first_child = TreeNode(100)
        >>> second_child = TreeNode(200)
        >>> first_child.set_children([TreeNode(1), TreeNode(2), TreeNode(3)])
        >>> second_child.set_children([TreeNode(4), TreeNode(5)])
        >>> root.set_children([first_child, second_child])
        >>> t._root = root
        >>> t
        10
        ├─┬ 100
        │ ├── 1
        │ ├── 2
        │ └── 3
        └─┬ 200
          ├── 4
          └── 5
        >>> t.clear()
        >>> t
        --
        >>> t.is_empty()
        True
        """
        self.__init__()
