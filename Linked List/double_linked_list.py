class Node():
	def __init__(self, value=None):
		self.data = value
		self.prev = None
		self.next = None

	def __repr__(self):
		return str(self.data)


class DoubleLinkedList():
	def __init__(self):
		self.__root = Node()

	
	def __repr__(self):
		output = "["
		tmp = self.__root
		if tmp.data != None:
			while(tmp.next != None):
				output += str(tmp.data) + ", "
				tmp = tmp.next
			output += str(tmp.data)
		return output+"]"


	def __len__(self):
		length = 0
		tmp = self.__root
		if tmp.data == None:
			return length
		while(tmp.next != None):
			length += 1
			tmp = tmp.next
		return length+1


	def __getitem__(self, num):
		if len(self) <= num or num <= -1:
			raise IndexError
		counter = 0
		tmp = self.__root
		if num == 0:
			return tmp
		while(tmp.next != None):
			tmp = tmp.next
			counter += 1
			if counter == num:
				return tmp


	def is_empty(self):
		if len(self) == 0:
			return True
		return False


	def add_front(self, item):
		if self.__root.data == None:
			self.__root.data = item
		else:
			tmp = Node()
			tmp.data = self.__root.data
			tmp.next = self.__root.next
			new = Node()
			new.data = item
			new.next = tmp
			new.prev = None
			tmp.prev = new
			self.__root = new


	def add_end(self, item):
		if self.__root.data == None:
			self.__root.data = item
		else:
			tmp = self.__root
			while(tmp.next != None):
				tmp = tmp.next
			new = Node()
			new.data = item
			new.next = None
			new.prev = tmp
			tmp.next = new


	def remove_front(self):
		if len(self)>0:
			tmp = self.__root.next
			tmp.prev = None
			self.__root = tmp


	def remove_end(self):
		if len(self)>0:
			tmp = self.__root
			while(tmp.next.next != None):
				tmp = tmp.next
			tmp.next = None


	def clear(self):
		self.__root = Node()


	def reverse(self):
		output = DoubleLinkedList()
		if self.__root.data == None:
			return DoubleLinkedList()
		tmp = self.__root.next
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

