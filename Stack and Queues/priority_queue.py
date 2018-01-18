class PriorityQueue():
	def __init__(self):
		self.container = []

	def __repr__(self):
		output = "["
		for item in self.container:
			output += str(item) + ", "
		if self.container:
			output = output[:-2]
		return output+"]"

	def __len__(self):
		return len(self.container)

	def enqueue(self, item):
		if self.container:
			for i, num in enumerate(self.container):
				if item >= num:
					self.container.insert(i, item)
					return
			self.container.append(item)
		else:
			self.container.append(item)

	def dequeue(self):
		return self.container.pop(0)

	def get_head(self):
		return self.container[0]

	def get_tail(self):
		return self.container[-1]

	def is_empty(self):
		return self.container == 0

	def clear(self):
		self.container = []




if __name__ == "__main__":
	q = PriorityQueue()
	q.enqueue(1)
	q.enqueue(0)
	q.enqueue(1)
	q.enqueue(8)
	q.enqueue(9)
	q.enqueue(-1)
	print(q)
	q.dequeue()
	print(q)
	q.clear()
	print(q)