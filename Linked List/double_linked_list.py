class Node():
	"""Basic object for the Node used for double linked lists"""
	def __init__(self, value=None):
		self.data = value
		self.prev = None
		self.next = None

	def __repr__(self):
        data = self.data
        nxt = self.next.data if self.next else None
        prv = self.prev.data if self.prev else None
        return "Node: (value: {}, previous: {}, next: {})".format(data, prv, nxt)


class DoubleLinkedList():
	"""Basic object for the double linked list"""
	def __init__(self, value):
		self.head = self.tail = Node(value)

	
	def __repr__(self):
		"""Represents the double linked list as a string"""
		output = "["
		tmp = self.head
		if tmp.data != None:
			while(tmp.next != None):
				output += str(tmp.data) + ", "
				tmp = tmp.next
			output += str(tmp.data)
		return output+"]"


	def __len__(self):
		"""Gets the length of the double linked list"""
		#TODO: make it O(1)
		length = 0
		tmp = self.head
		if tmp.data == None:
			return length
		while(tmp.next != None):
			length += 1
			tmp = tmp.next
		return length+1


	def __getitem__(self, num):
		"""Retrieves the element at the given index."""
		#TODO: make it support -ve indexing
		if len(self) <= num or num <= -1:
			raise IndexError
		counter = 0
		tmp = self.head
		if num == 0:
			return tmp
		while(tmp.next != None):
			tmp = tmp.next
			counter += 1
			if counter == num:
				return tmp


	def is_empty(self):
		"""Checks if double linked list is empty"""
		if len(self) == 0:
			return True
		return False


	def add_front(self, item):
		"""Adds node at the head of the linked list with complexity of O(1)"""
		if self.head.data == None:
			self.head.data = item
		else:
			tmp = Node()
			tmp.data = self.head.data
			tmp.next = self.head.next
			new = Node()
			new.data = item
			new.next = tmp
			new.prev = None
			tmp.prev = new
			self.head = new


	def add_end(self, item):
		"""Adds node at the tail of the linked list with complexity of O(n)"""
		if self.head.data == None:
			self.head.data = item
		else:
			tmp = self.head
			while(tmp.next != None):
				tmp = tmp.next
			new = Node()
			new.data = item
			new.next = None
			new.prev = tmp
			tmp.next = new


	def remove_front(self):
		"""Removes the linked list head with complexity of O(1)"""
		if len(self)>0:
			tmp = self.head.next
			tmp.prev = None
			self.head = tmp


	def remove_end(self):
		"""Removes the linked list tail with complexity of O(n)"""
		if len(self)>0:
			tmp = self.head
			while(tmp.next.next != None):
				tmp = tmp.next
			tmp.next = None


	def clear(self):
		"""Removes all nodes within the linked list with complexity of O(1)"""
		self.head = Node()


	def reverse(self):
		"""Reverses the whole linked list with complexity of O(n)"""
		output = DoubleLinkedList()
		if self.head.data == None:
			return DoubleLinkedList()
		tmp = self.head.next
		while(tmp.next != None):
			output.add_front(tmp.prev.data)
			tmp = tmp.next
		output.add_front(tmp.prev.data)
		output.add_front(tmp.data)
		return output






if __name__ == "__main__":
	l = DoubleLinkedList()
	print l
	l.add_end(1) #1
	l.add_end(0) #1 0
	l.add_end(7) #1 0 7
	print l
	print l.reverse()
	l.add_front(0) #0 1 0 7
	l.add_front(2) #2 0 1 0 7
	l.add_front(9) #9 2 0 1 0 7
	print l
	print l[4].prev
	l.remove_end() #9 2 0 1 0
	l.remove_front() #2 0 1 0
	print l
	print l[0].prev
	print l[0].next
	rev = l.reverse()
	print rev
	l.clear()
	print len(l)

