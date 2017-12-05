class Node():
	def __init__(self):
		self.data = None
		self.next = None

	def __repr__(self):
		return str(self.data)


class CircularLinkedList():
	def __init__(self):
		self.__root = Node()
		self.__root.next = self.__root


	def __repr__(self):
		output = "["
		tmp = self.__root
		if tmp.data != None:
			while(tmp.next != self.__root):
				output += str(tmp.data) + ", "
				tmp = tmp.next
			output += str(tmp.data)
		return output+"]"


	def __len__(self):
		length = 0
		tmp = self.__root
		if tmp.data == None:
			return length
		while(tmp.next != self.__root):
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
		while(tmp.next != self.__root):
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
			new = Node()
			new.data = self.__root.data
			new.next = self.__root.next
			self.__root.data = item
			self.__root.next = new


	def add_end(self, item):
		if self.__root.data == None:
			self.__root.data = item
		else:
			tmp = self.__root
			while(tmp.next != self.__root):
				tmp = tmp.next
			new = Node()
			new.data = item
			new.next = self.__root
			tmp.next = new


	def remove_front(self):
		if len(self)>0:
			last = self.__root
			while(last.next != self.__root ):
				last = last.next
			tmp = self.__root.next
			self.__root = tmp
			last.next = self.__root
			# print "length", len(self)
			


	def remove_end(self):
		if len(self)>0:
			tmp = self.__root
			while(tmp.next.next != self.__root):
				tmp = tmp.next
			tmp.next = self.__root


	def clear(self):
		self.__root = Node()
		self.__root.next = self.__root


	def reverse(self):
		output = CircularLinkedList()
		tmp = self.__root
		while(tmp.next != self.__root):
			output.add_front(tmp.data)
			tmp = tmp.next
		output.add_front(tmp.data)
		return output




if __name__ == "__main__":
	l = CircularLinkedList()
	# print l
	# print len(l)
	l.add_end(1) #1
	l.add_end(0) #1 0
	l.add_end(7) #1 0 7
	# print l
	# print l[2].next
	l.add_front(0) #0 1 0 7
	l.add_front(2) #2 0 1 0 7
	l.add_front(9) #9 2 0 1 0 7
	# print l
	# rev = l.reverse()
	# print rev
	# print l[5].next
	l.remove_end() #9 2 0 1 0
	l.remove_front() #2 0 1 0
	print l[3].next
	# print l.is_empty()
	print l
	l.clear()
	print l.is_empty()




