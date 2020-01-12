# Introduction

This folder contains two different, but related, classes:

* Binary Tree.
* Binary Search Tree (BST).

---

# Binary Tree

![Binary Tree UML](http://www.mediafire.com/convkey/0ea5/362cpgu27ybp2opzg.jpg)

Our binary Tree can be initialized using a list represented as nested multi-dimensional arrays encoded JSON. Each list can be either a length of one, two or three. Like so:

![](http://www.mediafire.com/convkey/a3b0/wo1n63qk70gajv7zg.jpg)

```python
>>> lst = ["A", ["B", "D", "E"], "C"]
```

So, the previous list can be represented as:

![](http://www.mediafire.com/convkey/f6cb/v2bxea0gmd82ct7zg.jpg)

Now, let's create our `BinaryTree` and make sure that it has been created properly:

```python
>>> lst = ["A", ["B", "D", "E"], "C"]
>>> btree = BinaryTree(lst)
>>> len(btree)
5
>>> btree.get_root()
A
>>> btree.get_root().left
B
>>> btree.get_root().right
C
>>> btree.get_root().right.left
None
>>> btree.get_root().left.left
D
```

#### Basic Methods

Now, let's see how to use some of the `BinaryTree` basic methods:

```python
>>> btree.count_leaf()
3
>>> btree.height()
2
>>> btree.is_balanced()
True
```

Remember that:

* `Leaf Node` is the node that has no children. And According to our tree, we have three nodes. ['C', 'D', 'E'].
* The depth of the tree is the number of edges from the root to the node.
* The Tree is said to be balanced if the difference between the depth of any two leaf nodes is one or less.

#### Traverse

Now, let's see how to traverse the previous tree. As you can remember, there are three types of tree traversal:

* Pre-Order Traversal:
  Parent is visited first (processed), followed by children from left to right.
* Post-Order Traversal:
  Children from left to right are processed first, followed by Parent.
* In-Order Traversal:
  The left child is processed first, then Parent, then the right child.

Let's see how to traverse in code:

```python
>>> btree.traverse("PreOrder")
[A, B, D, E, C]
>>> btree.traverse("PostOrder")
[D, E, B, C, A]
>>> btree.traverse("InOrder")
[D, B, E, A, C]
>>> btree.traverse("lana")
AssertionError: the input str MUST be one of these ["PreOrder", "InOrder", "PostOrder"]
```

Depth-first Traversal is pretty popular with graphs, but I have implemented it also with our tree class. And if you don't recall, Depth-first traversal processed Parent followed by the left-most child and its sub-tree.

So, the depth-first traversal of our tree will be:

```python
>>> btree.level_nodes()
[['A'], ['B', 'C'], ['D', 'E']]
```

#### Note

Our tree can accept any data type when created. So, the following is a tree created using numbers, characters:

![](http://www.mediafire.com/convkey/91b2/4gxijox1eghdyypzg.jpg)

```python
>>> expression = ["+", ["*", 2, ["-", 10, 7]], ["+", 3, ["*", 2, 4]]]
>>> btree = BinaryTree(expression)
>>> btree.get_root().left
*
>>> btree.get_root().right.right.right
*
>>> btree.is_balanced()
True
>>> btree.count_leaf()
6
>>> btree.height()
3
>>> btree.traverse("PreOrder")
[+, *, 2, –, 10, 7, +, 3, *, 2, 4]
>>> btree.traverse("PostOrder")
[2, 10, 7, -, *, 3, 2, 4, *, +, +]
>>> btree.traverse("InOrder")
[2, *, 10, –, 7, +, 3, +, 2, *, 4]
>>> len(btree)
11
```

---

# Binary Search Tree

![BST UML](http://www.mediafire.com/convkey/959c/nuf5m1qihdzko8hzg.jpg)

In the last part, we have been handling different data types. In this part, we will be dealing with just numbers (int, float). Binary Search Tree is a tree that any node `x`, all the key values in the left sub-tree of `x` are ≤ the key of `x` and all the keys in the right sub-tree of `x` are > the key of `x`.

Our module can be initialized by a list of number like so:

```python
>>> lst = [7,10,12,22,30,11,19,25,9,20,14]
>>> btree = BST(lst)
>>> btree.get_root()
14
>>> btree.get_root().right.left.left
19
>>> btree.get_root().left.right
12
>>> btree.get_root().left.right.left
11
>>> btree.get_root().left.right.right
None
```

The previous tree can be visualized as the following pic:

![](http://www.mediafire.com/convkey/d215/jappb83z430td2bzg.jpg)

#### Traverse

Now, let's see how to traverse the previous tree. As you can remember, there are three types of tree traversal:

- Pre-Order Traversal:
  Parent is visited first (processed), followed by children from left to right.
- Post-Order Traversal:
  Children from left to right are processed first, followed by Parent.
- In-Order Traversal:
  The left child is processed first, then Parent, then the right child.

Let's see how to traverse in code:

```python
>>> btree.traverse("PreOrder")
[14, 10, 9, 7, 12, 11, 22, 20, 19, 30, 25]
>>> btree.traverse("PostOrder")
[7, 9, 11, 12, 10, 19, 20, 25, 30, 22, 14]
>>> btree.traverse("InOrder")
[7, 9, 10, 11, 12, 14, 19, 20, 22, 25, 30]
>>> btree.traverse("lana")
AssertionError: the input str MUST be one of these ["PreOrder", "InOrder", "PostOrder"]
```

We can also get the maximum and minimum numbers of the tree:

```python
>>> btree.get_max()
30
>>> btree.get_min()
7
```

In Binary Search Tree, you can find the maximum number in the most right child, and the least number in the most left node.

#### Insert

Now, we have a `BST` that contains numbers. Let's insert some other numbers and see how it would look like:

```python
>>> btree.insert(40)
>>> btree.insert(13)
>>> btree.get_root().left.right.right
13
>>> btree.get_root().right.right.right
40
```

Now, the tree is like:

![](http://www.mediafire.com/convkey/624f/v7blc90bdt1hz9zzg.jpg)

As you can see, the number `13` is inserted in that position because it's less than `14` and bigger than both `10` and `12`. And the same happens with `40` which is bigger than all, so it must be in the most right node.

#### Remove

In Removal, there are three cases:

- The node is a leaf node (doesn't have children), then the removal is done without any change.

  ![](http://www.mediafire.com/convkey/3d30/spoa1q3o8xfl33mzg.jpg)

- The node has just one child, then the node is replaced by the child.

  ![](http://www.mediafire.com/convkey/1a00/4lm9ucradli8vr2zg.jpg)

- The node has both (left, right) children, then it's replaced by the minimum number in the right sub-tree.

  ![](http://www.mediafire.com/convkey/78d4/kmmama477pqk4qvzg.jpg)

Let's see how it's done in our `btree`:

```python
>>> btree.remove(25)
```

![](http://www.mediafire.com/convkey/4909/ahdoziildrdahiczg.jpg)

```python
>>> btree.remove(9)
```

![](http://www.mediafire.com/convkey/4988/n9k1ae7gn1o5r6hzg.jpg)

```python
>>> btree.remove(14)
```

![](http://www.mediafire.com/convkey/a99a/zf0ax9hdnahlbh5zg.jpg)

```python
>>> btree.remove(100)
ValueError: Cant find the given number
>>> btree.get_root()
19
>>> btree.get_root().left.left
7
>>> btree.get_root().right.left.left
None
>>> btree.get_root().right.right.left
None
```



#### Search

BST are mainly used to sort numbers to retrieve them in `log(n)` time where `n` is the count of the numbers. Whenever an element is to be searched, it starts searching from the root node. Then if the
data is less than the key value, it searches for the element in the left subtree. Otherwise,
it searches for the element in the right subtree.

```python
>>> btree.search(11)
True
>>> btree.search(25)
False
```

![](http://www.mediafire.com/convkey/56d4/jwuss80ns0vsbbmzg.jpg)