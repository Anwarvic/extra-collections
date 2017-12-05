class Stack():
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

	def push(self, item):
		self.__container.append(item)

	def pop(self):
		return self.__container.pop()

	def peek(self):
		return self.__container[-1]

	def is_empty(self):
		return len(self.__container) == 0

	def clear(self):
		self.__container = []



if __name__ == "__main__":
	s = Stack()
	s.push(2) #2
	s.push(4) #2 4
	s.push(8) #2 4 8
	print s
	print s.peek()
	print s
	print s.pop()
	print s


