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
- **Height*: The tree height is the number of edges between the root and the \
    furthest leaf node. In this case, the tree height is 3.


"""
import os
from extra.interface import Extra




class TreeNode(Extra):
    def __name__(self):
        return "extra.TreeNode()"
    

    def __init__(self, value):
        super()._validate_item(value)
        if type(value) == str:
            value = value.replace('\n', '\\n')
        self._data = value
        self._children = []


    def get_data(self):
        return self._data


    def get_children(self):
        return self._children
    

    def set_child(self, child):
        if not isinstance(child, TreeNode):
            raise TypeError(\
            f"You can't set a child unless it's an {self.__name__()} object!!")
        self._children.append(child)
    
    
    def set_children(self, lst):
        if not hasattr(lst, "__iter__"):
            raise TypeError("Given object isn't iterable!!")
        children = []
        for item in lst:
            if not isinstance(item, TreeNode):
                raise TypeError("You can't set a child unless it's an " + \
                    f"{self.__name__()} object!!")
            children.append(item)
        self._children = children
    

    def is_leaf(self):
        return self.get_children() == []
        

    def __repr__(self):
        return f"TreeNode({self._data})"


    @staticmethod
    def swap(node1, node2):
        if not isinstance(node1, TreeNode) or not isinstance(node2, TreeNode):
            raise TypeError(f"Incompitable objects' type preventing swapping!!")
        node1._data, node2._data = node2._data, node1._data




class Tree(Extra):
    def __name__(self):
        return "extra.Tree()"
    

    def __init__(self):
        self._root = None
    

    @staticmethod
    def __form_tree_from_path(parent_abs_path, curr_folder):
        node = TreeNode(curr_folder)
        abs_path = os.path.join(parent_abs_path, curr_folder)
        if os.path.isdir(abs_path):
            for child in sorted( os.listdir(abs_path) ):
                node.set_child(Tree.__form_tree_from_path(abs_path, child))
        return node


    @staticmethod
    def from_path(path):
        t = Tree()
        abs_path = os.path.abspath(path)
        parent, folder = os.path.split(abs_path)
        t._root = Tree.__form_tree_from_path(parent, folder)
        return t


    ##############################     LENGTH     ##############################
    def is_empty(self):
        return self._root is None
    

    def __count_nodes(self, start_node):
        assert isinstance(start_node, TreeNode)

        total_nodes = 1
        for child in start_node.get_children():
            total_nodes += self.__count_nodes(child)
        return total_nodes


    def __len__(self):
        if self.is_empty():
            return 0
        return self.__count_nodes(self._root)


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
            raise IndexError(f"Can't iterate over an empty {self.__name__()}!!")
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
    

