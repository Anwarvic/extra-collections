<h1 align="center">
<!-- <p>Extra-Collections</p> -->
<img src="./docs/source/img/dark-logo.png" height=200 alt="logo">
</h1>

# Extra-Collections
👋 `extra-collections` (or `extra` for short) is a python3 pacakge that provides
an **intuitive**, **pythonic**, **easy** implementation of the most common data
structures used in software projects. Some of these data structures are simple
such as :ref:`stack` or :ref:`queue`; and some are much complicated such as
:ref:`skip_list` or :ref:`red_black_tree`.

🧐 The name of the pacakge was inspired by the 
`collections <https://docs.python.org/3.8/library/collections.html>`_ built-in
python package which provides simple implementations for some of the basic data
structures. "extra" provides an additional set of data structures, hence the
name.. "extra-collections".

🤯 extra-collections, in its first release, provides 20 different data
structures to perform different tasks in a very fast and optimized way. Its aim
is to make working with these complicated data structres as simple as dealing
with a simple linked list which makes things easier to use for everyone
espcially if you're starting your journey into coding.

📒 extra-collections provides API documentations to quickly understand and use
those data structures on any given task. At the same time, I did my best to 
make these python modules as consistent as they could be. So dealing with the 
most complicated data structrue will as easy as the easiest one.

### **Fun fact:**

🤤 extra-collection was originally developed as a way to teach myself how to
code and there were no intentions to release it at all. But after spending more
than 18 months playing with different data structres, I've found out that I've
implemented 16 different data-structures. Just then, I decided to push it to 20
data structures and release it. Why 20 you ask? Because it is a nice round
number 😁.


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
* 1️⃣ :ref:`linked_list`
* 2️⃣ :ref:`doubly_linked_list`
* 3️⃣ :ref:`circular_linked_list`
* 4️⃣ :ref:`stack`
* 5️⃣ :ref:`queue`
* 6️⃣ :ref:`deque`
* 7️⃣ :ref:`priority_queue`
* 8️⃣ :ref:`skip_list`

### 🔥 Non-linear Data Structures:
* 9️⃣   :ref:`tree`
* 1️⃣0️⃣ :ref:`binary_tree`
* 1️⃣1️⃣ :ref:`bst`
* 1️⃣2️⃣ :ref:`avl`
* 1️⃣3️⃣ :ref:`splay_tree`
* 1️⃣4️⃣ :ref:`red_black_tree`
* 1️⃣5️⃣ :ref:`min_heap`
* 1️⃣6️⃣ :ref:`max_heap`
* 1️⃣7️⃣ :ref:`treap`
* 1️⃣8️⃣ :ref:`trie`
* 1️⃣9️⃣ :ref:`radix_trie`
* 2️⃣0️⃣ :ref:`suffix_trie`


## 🚀 Quick tour
First, you need to enable the python shell:

```shell
$ python
```

To immediately use a data strucutre, you can import it directly from the package
and start using it right-away. The following code uses a :ref:`bst`:

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
:ref:`contribution_guidelines`. By participating, you are expected to uphold
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
- Insert/delete/get_index/delete_index/set_index methods must raise errors when
needed.
- All methods should return the data stored not the used objects.
- Any module can be emptied except for the `SuffixTrie`.


## 📕 Resources

The following are the main resources that helped me while working on this
awesome project:

- [Introduction to Algorithms Course (MIT 6.046J/18.410J)](https://www.youtube.com/playlist?list=PLDC836E1A1076378E>).
- "Data Structures and Algorithms in Python" book.
- [GeeksforGeeks](https://www.geeksforgeeks.org/) Forum.