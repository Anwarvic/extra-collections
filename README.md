<h1 align="center">
<!-- <p>Extra-Collections</p> -->
<img src="https://extra-collections.readthedocs.io/en/latest/_images/light-logo.png" height=400 alt="logo">

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fe844ba14d8c4b18bc67e74d5005da06)](https://www.codacy.com/gh/Anwarvic/extra-collections/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Anwarvic/extra-collections&amp;utm_campaign=Badge_Grade)

[![python3.6](https://github.com/Anwarvic/extra-collections/workflows/python3.6/badge.svg)](https://github.com/Anwarvic/extra-collections/actions?query=workflow%3Apython3.6)
[![python3.7](https://github.com/Anwarvic/extra-collections/workflows/python3.7/badge.svg)](https://github.com/Anwarvic/extra-collections/actions?query=workflow%3Apython3.7)
[![python3.8](https://github.com/Anwarvic/extra-collections/workflows/python3.8/badge.svg)](https://github.com/Anwarvic/extra-collections/actions?query=workflow%3Apython3.8)

[![Documentation Status](https://readthedocs.org/projects/extra-collections/badge/?version=latest)](https://extra-collections.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/extra-collections.svg)](https://badge.fury.io/py/extra-collections)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

</h1>

# Extra-Collections
👋 `extra-collections` (or `extra` for short) is a python3 pacakge that provides
a **pythonic**, **intuitive**, and **easy** implementation of the most common
data structures used in software projects. Some of these data structures are
simple such as
[stack](https://extra-collections.readthedocs.io/en/latest/rst/lists/stack.html)
or [queue](https://extra-collections.readthedocs.io/en/latest/rst/lists/queue.html);
and some are much complicated such as
[skip_list](https://extra-collections.readthedocs.io/en/latest/rst/lists/skip_list.html)
or [red_black_tree](https://extra-collections.readthedocs.io/en/latest/rst/trees/red_black_tree.html).

🧐 The name of the pacakge was inspired by the 
[collections](https://docs.python.org/3.8/library/collections.html) python
package which provides simple implementations for some of the basic data
structures. "extra" provides an additional set of data structures, hence the
name.. "extra-collections".

🤯 extra-collections, in its first release, provides 20 different data
structures each performs different functionality in a very fast and optimized
way. Its aim is to make working with these complicated data structres as simple
as dealing with a simple linked list which makes things easier to use for
everyone espcially if they're starting their journey into coding.

📒 extra-collections provides API documentations to quickly understand and use
those data structures on any given task. At the same time, I did my best to 
make these python modules as consistent as they could be. So dealing with the 
most complicated data structrue will as easy as the easiest one.

### **Fun fact #1:**

🤫 extra-collection was originally developed as a way to teach myself how to
code and there were no intentions to release it at all. But after spending more
than 18 months playing with different data structres, I've found out that I've
implemented 16 different data-structures. Just then, I decided to push it to 20
data structures and release it. Why 20 you ask? Because it is a nice round
number 😁.

### **Fun fact #2:**

🤤 The first version of extra-collection was releases on 20/10/2020. I wanted
to release it on 20/20/2020 but my brother told me there are only 12 months in
a year. I didn't believe him, but he sweared.


## 👨🏻‍💻 Installation
To install the current release (Ubuntu, Windows, Mac):

```bash
pip install extra-collections
```

To update extra-collections to the latest version, add `--upgrade` flag to the
above commands.


## 🦾 Available Data Structures
In this release, you can find 2️⃣0️⃣ data structures that can be categorized into
two categories:

### ⚡️ Linear Data Structures:
* 1️⃣ [Linked List](https://extra-collections.readthedocs.io/en/latest/rst/lists/linked_list.html)
* 2️⃣ [Doubly Linked List](https://extra-collections.readthedocs.io/en/latest/rst/lists/doubly_linked_list.html)
* 3️⃣ [Circular Linked List](https://extra-collections.readthedocs.io/en/latest/rst/lists/circular_linked_list.html)
* 4️⃣ [Stack](https://extra-collections.readthedocs.io/en/latest/rst/lists/stack.html)
* 5️⃣ [Queue](https://extra-collections.readthedocs.io/en/latest/rst/lists/queue.html)
* 6️⃣ [Deque](https://extra-collections.readthedocs.io/en/latest/rst/lists/deque.html)
* 7️⃣ [Priority Queue](https://extra-collections.readthedocs.io/en/latest/rst/lists/priority_queue.html)
* 8️⃣ [Skip List](https://extra-collections.readthedocs.io/en/latest/rst/lists/skip_list.html)

### 🔥 Non-linear Data Structures:
* 9️⃣   [Tree](https://extra-collections.readthedocs.io/en/latest/rst/trees/tree.html)
* 1️⃣0️⃣ [Binary Tree](https://extra-collections.readthedocs.io/en/latest/rst/trees/binary_tree.html)
* 1️⃣1️⃣ [Binary Search Tree](https://extra-collections.readthedocs.io/en/latest/rst/trees/bst.html)
* 1️⃣2️⃣ [AVL Tree](https://extra-collections.readthedocs.io/en/latest/rst/trees/avl.html)
* 1️⃣3️⃣ [Splay Tree](https://extra-collections.readthedocs.io/en/latest/rst/trees/splay_tree.html)
* 1️⃣4️⃣ [Red-Black Tree](https://extra-collections.readthedocs.io/en/latest/rst/trees/red_black_tree.html)
* 1️⃣5️⃣ [Min Heap](https://extra-collections.readthedocs.io/en/latest/rst/trees/min_heap.html)
* 1️⃣6️⃣ [Max Heap](https://extra-collections.readthedocs.io/en/latest/rst/trees/max_heap.html)
* 1️⃣7️⃣ [Treap](https://extra-collections.readthedocs.io/en/latest/rst/trees/treap.html)
* 1️⃣8️⃣ [Trie](https://extra-collections.readthedocs.io/en/latest/rst/trees/trie.html)
* 1️⃣9️⃣ [Radix Trie](https://extra-collections.readthedocs.io/en/latest/rst/trees/radix_trie.html)
* 2️⃣0️⃣ [Suffix Trie](https://extra-collections.readthedocs.io/en/latest/rst/trees/suffix_trie.html)


## 🚀 Quick tour
First, you need to enable the python shell:

```shell
$ python
```

To immediately use a data strucutre, you can import it directly from the package
and start using it right-away. The following code uses a [bst](https://extra-collections.readthedocs.io/en/latest/rst/trees/bst.html):

```python
>>> from extra import BST
>>> bst = BST([8, 5, 2, 7, 15, 10, 3])
>>> bst
      __8___
     /      \
  __5       _15
 /   \     /
2     7   10
 \
  3
>>> bst.insert(30)
>>> bst
      __8___
     /      \
  __5       _15
 /   \     /   \
2     7   10    30
 \
  3
>>> bst.remove(3)
>>> bst
      __8___
     /      \
  __5       _15
 /   \     /   \
2     7   10    30
>>> len(bst)
7
```

## 🤝 Contribution guidelines
If you want to contribute to extra-collections, be sure to review the 
[contribution guidelines](https://extra-collections.readthedocs.io/en/latest/contribution.html). 
By participating, you are expected to uphold
this code.

This project uses GitHub issues for tracking requests and bugs, questions and
even discussion. Please, if you have any question, direct it to Stack Overflow
under <a href="https://stackoverflow.com/questions/tagged/extra-collections">
<img src="./docs/source/img/stackoverflow-tag.png" height="20">
</a>


## 🚧 Design Principles

Here, I will walk you through some of the design principles that I followed
while creating this package:

- Can't create nested modules.
- Replace `'\n'` with `'\\n'` when seen as an input value.
- `None` can't be used as an input value. (Could be changed in future releases).
- Class constructors can be used for initialization as well as declaration.
- Methods with no `_` are for public use. The other are not; unless you know
what you're doing. 
- All public methods must raise appropriate errors when needed. The Other
methods must raise only `AssertionError` when needed.
- Search/remove methods shouldn't raise any errors.
- Insert/delete/get-index/delete-index/set-index methods must raise errors when
needed.
- All methods should return the data stored not the used objects.
- Any module can be emptied except for the `SuffixTrie`.


## 📕 Resources

The following are the main resources that helped me while working on this
awesome project:

- [Introduction to Algorithms Course (MIT 6.046J/18.410J)](https://www.youtube.com/playlist?list=PLDC836E1A1076378E>).
- "[Data Structures and Algorithms in Python](https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275)" book.
- [GeeksforGeeks](https://www.geeksforgeeks.org/) Forum.
- [Best Data Structures and Algorithms Books](https://www.interviewbit.com/blog/data-structures-and-algorithms-books/) 
