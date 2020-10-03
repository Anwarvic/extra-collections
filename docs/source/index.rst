Extra Collections
==================

.. image:: ./img/light-logo.png
   :height: 200
   :align: center

👋 "extra-collections" (or "extra" for short) is a python3 pacakge that provides
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

**Fun fact:**

🤤 extra-collection was originally developed as a way to teach myself how to
code and there were no intentions to release it at all. But after spending more
than 18 months playing with different data structres, I've found out that I've
implemented 16 different data-structures. Just then, I decided to push it to 20
data structures and release it. Why 20 you ask? Because it is a nice round
number 😁.


👨🏻‍💻 Installation
-------------
To install the current release (Ubuntu, Windows):

.. code-block:: shell

   pip install extra-collections

To update extra-collections to the latest version, add --upgrade flag to the
above commands.


🦾 Available Data Structures
-------------------------
In this release, you can find +20 data structures that can be categorized into
two categories:

⚡️ Linear Data Structures:
~~~~~~~~~~~~~~~~~~~~~~~~~
* 1️⃣ :ref:`linked_list`
* 2️⃣ :ref:`doubly_linked_list`
* 3️⃣ :ref:`circular_linked_list`
* 4️⃣ :ref:`stack`
* 5️⃣ :ref:`queue`
* 6️⃣ :ref:`deque`
* 7️⃣ :ref:`priority_queue`
* 8️⃣ :ref:`skip_list`

🔥 Non-linear Data Structures:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
* 2️⃣0️⃣:ref:`suffix_trie`


🚀 Quick tour
--------------
First, you need to enable the python shell:

.. code-block:: shell

   $ python

To immediately use a data strucutre, you can import it directly from the package
and start using it right-away. The following code uses a :ref:`bst`:

.. code-block:: python

   >>> from extra import BST
   >>> bst = BST([8, 5, 2, 7, 15, 10, 3])
   >>> bst
         __8___
        /      \\
     __5       _15
    /   \\    /
   2     7   10
    \\
     3
   >>> bst.insert(30)
   >>> bst
         __8___
        /      \\
     __5       _15
    /   \\    /   \
   2     7   10    30
    \\
     3
   >>> bst.remove(3)
   >>> bst
         __8___
        /      \\
     __5       _15
    /   \\    /   \
   2     7   10    30
   >>> len(bst)
   7



.. toctree::
   :hidden:

   rst/lists/linked_list
   rst/lists/doubly_linked_list
   rst/lists/circular_linked_list
   rst/lists/stack
   rst/lists/queue
   rst/lists/deque
   rst/lists/priority_queue
   rst/lists/skip_list
   rst/trees/tree
   rst/trees/binary_tree
   rst/trees/bst
   rst/trees/splay_tree
   rst/trees/avl
   rst/trees/red_black_tree
   rst/trees/min_heap
   rst/trees/max_heap
   rst/trees/treap
   rst/trees/trie
   rst/trees/radix_trie
   rst/trees/suffix_trie

