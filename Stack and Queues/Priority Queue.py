class PriorityQueue():
	def __init__(self):
		self.__container = []

	def __repr__(self):
		output = "["
		for item in self.__container:
			output += str(item) + ", "
		if self.__container:
			output = output[:-2]
		return output+"]"

	def __len__(self):
		return len(self.__container)

	def enqueue(self, item):
		if self.__container:
			for i, num in enumerate(self.__container):
				if item >= num:
					self.__container.insert(i, item)
					return
			self.__container.append(item)
		else:
			self.__container.append(item)

	def dequeue(self):
		return self.__container.pop(0)

	def get_head(self):
		return self.__container[0]

	def get_tail(self):
		return self.__container[-1]

	def is_empty(self):
		return self.__container == 0

	def clear(self):
		self.__container = []




if __name__ == "__main__":
	q = PriorityQueue()
	q.enqueue(1)
	q.enqueue(0)
	q.enqueue(1)
	q.enqueue(8)
	q.enqueue(9)
	q.enqueue(-1)
	print q
	q.dequeue()
	print q
	q.clear()
	print q