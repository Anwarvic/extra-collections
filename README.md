

## Design Principles

Here, I will walk you through some of the design principles that I followed while creating this module:

- All nodes mush raise errors not just AssertionError

- handle '\n' if given as an input to a node

- Can't create nested nodes

- All internal variables must contain `_` unless it's important for the user to know




- Class constructors are not for initialization

- Methods with no `_` are for public use, methods with one `_` are for inheritance and methods with `__` are for private use.

- All public methods must raise Errors when needed. The Other methods must raise only AssertionError when needed.

- search/remove shouldn't raise any errors.

- insert/delete/get_index/delete_index raise errors.

- All methods should return the data not the used objects.

- Tree can be empty... must have is_empty() & clear()


## TODO

- __setitem__(), __getitem__(), __delitem__() must accept negative indices and slices

- adjust #### parts