class TreeNode():
	def __init__(self):
		self.number = None
		self.left = None
		self.right = None

	def __repr__(self):
		return str(self.number)

	def get_max_node(self):
		if self.right == None:
			return self.number
		else:
			return self.right.get_max_node()

	def get_min_node(self):
		if self.left == None:
			return self.number
		else:
			return self.left.get_min_node()

	def traverse_node(self, method):
		assert method in ["PreOrder", "InOrder", "PostOrder"], \
			'the input str MUST be one of these ["PreOrder", "InOrder", "PostOrder"]'
		output = []
		# -------------------- PreOrder --------------------
		if method == "PreOrder":
			if self.number != None:
				output.append(self)
				if self.left != None:
					output.extend(self.left.traverse_node("PreOrder"))
				if self.right != None:
					output.extend(self.right.traverse_node("PreOrder"))
			return output

		# -------------------- PostOrder --------------------
		elif method == "PostOrder":
			if self.number != None:
				if self.left != None:
					output.extend(self.left.traverse_node("PostOrder"))
				if self.right != None:
					output.extend(self.right.traverse_node("PostOrder"))
				output.append(self)
			return output
		# -------------------- InOrder --------------------
		elif method == "InOrder":
			if self.number != None:
				if self.left != None:
					output.extend(self.left.traverse_node("InOrder"))
				output.append(self)
				if self.right != None:
					output.extend(self.right.traverse_node("InOrder"))
			return output





class BST():
	def __init__(self, lst):
		def ensure_type(lst):
			assert type(lst) == list
			for item in lst:
				if type(item) not in [int, float]:
					raise ValueError, "List items must all be numbers"

		def construct(lst):
			length = len(lst)
			if length <= 0:
				return 
			elif length == 1:
				node = TreeNode()
				node.number = lst[0]
				return node
			median_idx = length/2
			node = TreeNode()
			node.number = lst[median_idx]
			node.left = construct(lst[:median_idx])
			node.right = construct(lst[median_idx+1:])
			return node
		
		lst = sorted(lst)
		ensure_type(lst) #for Error checking
		self.__root = construct(lst)


	def __len__(self):
		def length(tree_node):
			size = 0
			if tree_node.left == None and tree_node.right == None:
				size += 1
			elif tree_node.left == None and tree_node.right != None:
				size += length(tree_node.right) + 1
			elif tree_node.left != None and tree_node.right == None:
				size += length(tree_node.left) + 1
			elif tree_node.left != None and tree_node.right != None:
				size += 1
				size += length(tree_node.left)
				size += length(tree_node.right)
			return size
		if self.__root == None:
			return 0
		else:
			return length(self.__root)


	def get_root(self):
		return self.__root

	def insert(self, num):
		if type(num) not in [int, float]:
			raise ValueError, "To insert an item, it has to be a number"
		def insert_node(tree_node, num):
			if num == tree_node.number:
				return #do nothing
			elif num > tree_node.number:
				if tree_node.right == None:
					node = TreeNode()
					node.number = num
					tree_node.right = node
				else:
					insert_node(tree_node.right, num)
			elif num < tree_node.number:
				if tree_node.left == None:
					node = TreeNode()
					node.number = num
					tree_node.left = node
				else:
					insert_node(tree_node.left, num)
		if self.__root == None:
			self.__root = TreeNode()
			self.__root.number = num
		else:
			insert_node(self.__root, num)


	def get_max(self):
		return self.__root.get_max_node()


	def get_min(self):
		return self.__root.get_min_node()


	def remove(self, num):
		def remove_node(tree_node, num):
			# print tree_node.number
			if tree_node.number == num:
				if tree_node.left == None and tree_node.right == None: #leaf node
					tree_node.number = None
					del tree_node.left
					del tree_node.right
					# tree_node = None
				elif tree_node.left == None and tree_node.right != None:
					tree_node.number = tree_node.right.number
					tree_node.left = None
					tree_node.right = None
				elif tree_node.left != None and tree_node.right == None:
					tree_node.number = tree_node.left.number
					tree_node.left = None
					tree_node.right = None
				else:
					min_value = tree_node.right.get_min_node()
					self.remove(min_value)
					tree_node.number = min_value
					
			elif num > tree_node.number:
				try:
					remove_node(tree_node.right, num)
				except AttributeError:
					raise ValueError, "Can't find the given number"	
			elif num < tree_node.number:
				try:
					remove_node(tree_node.left, num)
				except AttributeError:
					raise ValueError, "Can't find the given number"	
				

		if type(num) not in [float, int]:
			raise ValueError, "List items are all numbers"
		remove_node(self.__root, num)


	def traverse(self, method):
		return self.__root.traverse_node(method)

	def search(self, num):
		def search_sub_tree(tree_node, num):
			if tree_node.number == num:
				return True
			elif tree_node.left == None and tree_node.right == None:
				return False
			if tree_node.left != None and num < tree_node.number:
				return search_sub_tree(tree_node.left, num)
			if tree_node.right != None and num > tree_node.number:
				return search_sub_tree(tree_node.right, num)
			else:
				return False

		return search_sub_tree(self.__root, num)







if __name__ == "__main__":
	lst = [7,10,12,22,30,11,19,25,9,20,14]
	btree = BST(lst)
	print btree.traverse("PreOrder")
	print btree.traverse("PostOrder")
	print btree.traverse("InOrder")
	btree.insert(40)
	btree.insert(13)
	btree.remove(25)
	btree.remove(9)
	btree.remove(14)
	print btree.search(10)
	print btree.get_root().left.left



