"""
AVL is a self-balancing binary search tree which is a non-linear data structure
that stores numbers hierarchical with the assertion that any operation, like
insertion, searching, and deletion, will be done in **log(n)** time-complexity
where **n** is the number of elements in the AVL. AVL was named after the
initials of its inventors: Adel’son-Vel’skii and Landis.
"""
from extra.trees.bst import BSTNode, BST



class AVLNode(BSTNode):
    """
    An AVL node is the basic unit for building AVL trees. A AVL node must
    contain a  number. Each AVL node has either zero, one or two children AVL
    nodes. The node that has no children is called a **leaf node**. The only 
    difference between `AVLNode()` and `BSTNode()` is that the former dedicates
    a variable for the `height` which makes balancing `AVL()` objects done in 
    a constant time.
    """
    __name__ = "extra.AVLNode()"
    

    def __init__(self, value):
        """
        Creates a `AVLNode()` object which is the basic unit for building 
        AVL() objects!!

        Parameters
        ----------
        value: int or float
            The value to be saved within the `AVLNode()` instance

        Raises
        ------
        ValueError: If the given item is `None`.
        TypeError: If the given item isn't a number.
        """
        super().__init__(value)
        self._height = 0
    

    def set_left(self, new_node):
        """
        Sets the given `AVLNode()` as a left child for the current `AVLNode()`.

        Parameters
        ----------
        child: AVLNode()
            The `AVLNode()` that will be a left child for the current one.

        Raises
        ------
        TypeError: If the given item is not an `AVLNode()` object.
        """
        super().set_left(new_node)
        self._height = max(self.get_children_heights())
    

    def set_right(self, new_node):
        """
        Sets the given `AVLNode()` as a right child for the current `AVLNode()`.

        Parameters
        ----------
        child: AVLNode()
            The `AVLNode()` that will be a right child for the current one.

        Raises
        ------
        TypeError: If the given item is not an `AVLNode()` object.
        """
        super().set_right(new_node)
        self._height = max(self.get_children_heights())
    

    def get_height(self):
        """
        Returns the height of the `AVLNode()`.

        Returns
        -------
        int:
            The height of the current `AVLNode()`.
        """
        return self._height
    

    def get_left_height(self):
        """
        Returns the height of the left `AVLNode()` child.

        Returns
        -------
        int:
            The height of the left `AVLNode()` child.
        """
        return 1 + self.get_left().get_height() \
            if self.get_left() is not None else 0
        

    def get_right_height(self):
        """
        Returns the height of the right `AVLNode()` child.

        Returns
        -------
        int:
            The height of the right `AVLNode()` child.
        """
        return 1 + self.get_right().get_height() \
            if self.get_right() is not None else 0
    

    def get_children_heights(self):
        """
        Returns a list of two children heights of the current `AVLNode()`
        instance where the first value is the height of the left child and the
        other is the height of the right child.

        Returns
        -------
        list:
            A list of the two children of the `AVLNode()` instance.
        """
        return [self.get_left_height(), self.get_right_height()]
    

    def set_height(self, new_height):
        """
        Sets the height of the current `AVLNode()`.

        Parameters
        ----------
        new_height: int
            The new height that should be assigned to the current `AVLNode()`
        
        Raises
        ------
        TypeError: If the given `height` isn't an integer.
        ValueError: If the given `height` is less than zero.
        """
        if type(new_height) != int:
            raise TypeError("Height has to be an integer number >= 0!!")
        elif new_height < 0:
            raise ValueError("Height has to be an integer number >= 0!!")
        self._height = new_height
    

    def is_balanced(self):
        left_height, right_height = self.get_children_heights()
        return abs(right_height - left_height) <= 1
    

    def __repr__(self):
        """
        Represents `AVLNode()` object as a string.

        Returns
        -------
        str:
            A string representing the `AVLNode()` instance.
        
        Example
        -------
        >>> x = AVLNode(10)
        >>> x
        >>> AVLNode(10)
        """
        return f"AVLNode({self._data})"
    



class AVL(BST):
    """
    AVL is self-balancing (BST), Binary Search Tree  which is a non-linear data
    structure that can be defined recursively using a collection of `AVLNode()`
    instances, where each node contains a numeric value and it has either zero,
    one or two references to the children `BSTNode()` instances. And the value
    holding by the node must be greater than all values being hold by the left
    subtree and smaller that all the values being hold by the right subtree.
    """
    _basic_node = AVLNode
    __name__ = "extra.AVL()"
    

    def __init__(self):
        """
        Creates an empty `AVL()` object!!
        
        Example
        -------
        >>> avl = AVL()
        >>> type(avl)
        <class 'extra.trees.avl.AVL'>
        """
        super().__init__()
    

    