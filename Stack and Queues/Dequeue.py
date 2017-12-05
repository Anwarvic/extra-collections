class Dequeue():
	def __init__(self):
		self.__container = []

	def __repr__(self):
		output = "["
		for item in self.__container:
			output += str(item)
			if item != self.__container[-1]:
				output += ", "
		return output+"]"

	def __len__(self):
		return len(self.__container)

	def add_front(self, item):
		self.__container.insert(0, item)

	def add_end(self, item):
		self.__container.append(item)

	def pop(self):
		return self.__container.pop()

	def eject(self):
		return self.__container.pop(0)

	def peek(self):
		return self.__container[-1]

	def is_empty(self):
		return self.__container == 0

	def clear(self):
		self.__container = []




if __name__ == "__main__":
	q = Dequeue()
	q.add_front(0)
	q.add_end(1)
	q.add_end(8)
	q.add_front(9)
	print q
	print q.pop()
	print q
	print q.eject()
	print q
	q.clear()
	print len(q)