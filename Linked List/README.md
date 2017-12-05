# Introduction

This folder consists of three classes:

* Linked List.
* Double Linked List.
* Circular Linked List.



# Linked List

![LinkedList UML](http://www.mediafire.com/convkey/7e49/z7i5phjizhvhm3pzg.jpg)

Let's now see how to create a `LinkedList` and use the provided methods:

```python
>>> l = LinkedList()
>>> l
[]
>>> len(l)
0
```

As you can see, the `l` is an empty `LinkedList`. Let's add some items using either `add_front()` or `add_end()` methods:

```python
>>> l.add_end(1)
>>> l.add_end("Hello")
>>> l.add_end([7])
>>> l
[1, "Hello", [7]]
```

As you can see, you can use any data type. But for the rest of this tutorial, we will continue using numbers. Let's clear it first:

```python
>>> l.clear()
>>> l.is_empty()
True
>>> l.add_end(11)
>>> l.add_end(7)
>>> l.add_front(0)
>>> l.add_front(22)
>>> l.add_front(90)
>>> print l
[90, 22, 0, 11, 7]
```

Now, our LinkedList looks like so:

![](http://www.mediafire.com/convkey/1d5c/s7h0a0h1doq9dk5zg.jpg)

Now, let's get fancy and reverse this LinkedList:

```python
>>> l.reverse()
[7, 11, 0, 22, 90]
```

![](http://www.mediafire.com/convkey/914f/j32v80255874vn5zg.jpg)

Looks good? Naah, I think we should remove some of these nodes because **WE CAN**:

```python
>>> l.remove_end()
>>> l
[7, 11, 0, 22]
>>> l.remove_front()
[7, 11, 0]
```

![](http://www.mediafire.com/convkey/85bd/zazg7njvb1rdbzgzg.jpg)

---

# Double Linked List

![Double Linked list UML](http://www.mediafire.com/convkey/4d48/v4ampot1bcon7vuzg.jpg)

`DoubleLinkedList` is the same as `LinkedList`, they both have a pointer to the next node in the list. But `DoubleLinkedList` has a pointer to the previous node as well. It has the same methods as the Linked list.

```python
>>> l = DoubleLinkedList()
>>> l.add_end(11)
>>> l.add_end(7)
>>> l.add_front(0)
>>> l.add_front(22)
>>> l.add_front(90)
>>> print l
[90, 22, 0, 11, 7]
```

And it would look like this:

![](http://www.mediafire.com/convkey/6988/5qgcfa9v15h72bnzg.jpg)

---

# Circular Linked List

![Circular Linked List](http://www.mediafire.com/convkey/9678/20yyc8bwreqn9fqzg.jpg)

The `CircularLinkedList` is a little different than the previous lists. The tail of the `CircularLinkedList` is always connected to the head. Let's see how by an example

```python
>>> l = CircularLinkedList()
>>> l.add_end(11)
>>> l.add_end(7)
>>> l.add_end(15)
>>> l.add_end(8)
>>> l.add_front(14)
>>> l.add_front(0)
>>> l.add_front(22)
>>> l.add_front(90)
>>> print l
[90, 22, 0, 14, 11, 7, 15, 8]
```

Which would look like this:

![](http://www.mediafire.com/convkey/c2d1/uoxiwhl2ru0k14ezg.jpg)

```python
>>> len(l)
8
>>> l[7].next
90
>>> l[0]
90
```

You can also use the same methods as before:

```python
>>> l.remove_end()
>>> l.remove_end()
>>> l
[90, 22, 0, 14, 11, 7]

```

![](http://www.mediafire.com/convkey/3582/o0l1vaeb6vw1q1rzg.jpg)

```python
>>> l.remove_front()
>>> l.remove_front()
[0, 14, 11, 7]
```

>>> ![](http://www.mediafire.com/convkey/8912/815ap1is8upeb88zg.jpg)





