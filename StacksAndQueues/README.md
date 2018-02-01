# Introduction

---

This folder consists of three classes:

* Stack
* Queue
* Priority Queue.
* Dequeue

I know these classes are too easy and they can be implemented easily, but it won't harm.

**Note:**
The Visualizations inside this file are for illustration purposes, the code doesn't produce any visualizations.

---

# Stack

![Stack UML](http://www.mediafire.com/convkey/40ec/fwn1wbg8bdmwr6dzg.jpg)

Let's see how to create a `Stack`:

```python
>>> s = Stack()
```

![Empty Stack](http://www.mediafire.com/convkey/3faa/cnub4yes7hxs3crzg.jpg)

Let's now use the provided methods:

```python
>>> s.push(2)
>>> s.push("Hello")
>>> s.push([5,8])
>>> len(s)
3
>>> s
[2, "Hello", [5,8]]
```

Now, the stack would look like this:

![](http://www.mediafire.com/convkey/bf33/dwfp0a7njdxr0c5zg.jpg)

```python
>>> s.peek()
[5,8]
>>> s.pop()
[5,8]
>>> s
[2, "Hello"]
```

![](http://www.mediafire.com/convkey/8715/r1v7jb5l0bqh815zg.jpg)

```python
>>> s.clear()
>>> s.is_empty()
True
>>> len(s)
0
```

---

# Queue

![Queue UML](http://www.mediafire.com/convkey/efcb/4rlnx938en4lj49zg.jpg)

Let's see how to create a `Queue` and use the provided methods:

> > ```python
> > >>> q = Queue()
> > >>> q.enqueue(1)
> > >>> q.enqueue(0)
> > >>> q.enqueue(1)
> > >>> q.enqueue(8)
> > >>> q.enqueue(9)
> > >>> q.enqueue(-1)
> > >>> len(q)
> > 6
> > >>> q
> > [-1, 9, 8, 1, 0, 1]
> > ```
> >
> > And the `Queue` would look like so:
> >
> > ![](http://www.mediafire.com/convkey/828e/1a6sa4bzer26z80zg.jpg)

```python
>>> q.get_head()
-1
>>> q.get_tail()
9
>>> q.dequeue()
>>> q
[-1, 9, 8, 1, 0]
```

![](http://www.mediafire.com/convkey/9567/7t80jhk7zyphhumzg.jpg)

```python
>>> q.is_empty()
False
>>> q.clear()
True
>>> q
[]
```

---

# Priority Queue

![Priority Queue UML](http://www.mediafire.com/convkey/fa4f/avo76fjm1wsnoyazg.jpg)

`PriorityQueue` is the same as the `Queue` but the items inside it are sorted in descending order. Let's see an example:

```python
>>> q = PriorityQueue()
>>> q.enqueue(1)
>>> q.enqueue(0)
>>> q.enqueue(1)
>>> q.enqueue(8)
>>> q.enqueue(9)
>>> q.enqueue(-1)
```

Which would look like this:

![](http://www.mediafire.com/convkey/315c/9p7xrdotz5xigt8zg.jpg)

Let's try more methods:

```python
>>> q.clear(
>>> q.is_empty()
True
>>> len(q)
0
```

---

# Dequeue

![Double-ended Queue](http://www.mediafire.com/convkey/e15a/ktaeg1ezxvwh7zczg.jpg)

`Dequeue` is the same as `Queue` but we can add items in both sides. Let's see how:

```python
>>> q = Dequeue()
>>> q.add_front(0)
>>> q.add_end(1)
>>> q.add_end(8)
>>> q.add_front(9)
>>> len(q)
4
>>> q
[9, 0, 1, 8]
```

Which would look like so:

![](http://www.mediafire.com/convkey/b576/9trckeetaxipcjmzg.jpg)

> > ```python
> > >>> q.pop()
> > 8
> > >>> q.eject()
> > 9
> > >>> q
> > [0, 1]
> > >>> q.clear()
> > >>> len(q)
> > 0
> > ```
> >
> > 