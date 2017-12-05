class TreeNode():
	def __init__(self):
		self.data = None
		self.left = None
		self.right = None
		self.level = None

	def __repr__(self):
		return str(self.data)


	def get_depth(self):
		return self.level

	def count_leaf(self):
		counter = 0
		if self.left == None and self.right == None:
				counter += 1
		elif self.left != None and self.right == None:
				counter += self.left.count_leaf()
		elif self.left == None and self.right != None:
				counter += self.right.count_leaf()
		else:
			counter += self.left.count_leaf()
			counter += self.right.count_leaf()
		return counter


	def is_balanced(self):
		if self.left == None and self.right == None:
			return True
		left_depth = self.left.get_depth() + 1
		right_depth = self.right.get_depth() + 1
		# print left_depth, right_depth
		if abs(left_depth - right_depth) <= 1:
			return True
		return False


	def traverse_node(self, method):
		assert method in ["PreOrder", "InOrder", "PostOrder"], \
			'the input str MUST be one of these ["PreOrder", "InOrder", "PostOrder"]'
		output = []
		# -------------------- PreOrder --------------------
		if method == "PreOrder":
			if self.data != None:
				output.append(self)
				if self.left != None:
					output.extend(self.left.traverse_node("PreOrder"))
				if self.right != None:
					output.extend(self.right.traverse_node("PreOrder"))
			return output

		# -------------------- PostOrder --------------------
		elif method == "PostOrder":
			if self.data != None:
				if self.left != None:
					output.extend(self.left.traverse_node("PostOrder"))
				if self.right != None:
					output.extend(self.right.traverse_node("PostOrder"))
				output.append(self)
			return output
		# -------------------- InOrder --------------------
		elif method == "InOrder":
			if self.data != None:
				if self.left != None:
					output.extend(self.left.traverse_node("InOrder"))
				output.append(self)
				if self.right != None:
					output.extend(self.right.traverse_node("InOrder"))
			return output
		




class BinaryTree():
	def __init__(self, lst):
		def parse(lst, level):
			length = len(lst)
			"""
			This function takes a list of items and returns a BinaryTree
			"""
			assert length<=3, "Two children only!"
			if length == 2:
				tmp = TreeNode()
				tmp.data = lst[0]
				tmp.level = level
				if type(lst[1])==list:
					tmp.left = parse(lst[1], level+1)
				else:
					node = TreeNode()
					node.data = lst[1]
					node.level = tmp.level + 1
					tmp.left = node
				return tmp
			
			elif length == 3:
				tmp = TreeNode()
				tmp.data = lst[0]
				tmp.level = level
				if type(lst[1])==list:
					tmp.left = parse(lst[1], level+1)
				else:
					node = TreeNode()
					node.data = lst[1]
					node.level = tmp.level + 1
					tmp.left = node
				if type(lst[2])==list:
					tmp.right = parse(lst[2], level+1)
				else:
					node = TreeNode()
					node.data = lst[2]
					node.level = tmp.level + 1
					tmp.right = node
				return tmp
		if len(lst) == 1:
			self.__root = TreeNode()
			self.__root.data = lst[0]
			self.__root.level = 0
		else:
			self.__root = parse(lst, 0)


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
	

	def count_leaf(self):
		if not isinstance(self.__root, TreeNode):
			return 1
		else:
			return self.__root.count_leaf()

	def height(self):
		def get_depth(tree_node):
			depth = 0
			if tree_node.left == None and tree_node.right == None:
				pass #do nothing
			elif tree_node.left != None and tree_node.right == None:
				depth += get_depth(tree_node.left) + 1
			elif tree_node.left == None and tree_node.right != None:
				depth +=  get_depth(tree_node.right) + 1
			else:
				left_depth = get_depth(tree_node.left) + 1
				right_depth = get_depth(tree_node.right) + 1
				depth += left_depth if left_depth>=right_depth else right_depth
			return depth

		if (self.__root.left == None) and (self.__root.right == None):
			return 0
		else:
			return get_depth(self.__root)


	def traverse(self, method):
		return self.__root.traverse_node(method)


	def is_balanced(self):
		"""
		The Tree is said to be balanced if the difference between the depth of any two leaf nodes
		is one or less.
		"""
		return self.__root.is_balanced()


	def level_nodes(self):
		if self.__root == None:
			return []
		else:
			max_depth = self.height()
			level_nodes = level_nodes = [[] for i in range(max_depth+1)]
			for node in self.traverse(method="PreOrder"):
				i = node.level
				level_nodes[i].append(node.data)

			return level_nodes

		


	





if __name__ == "__main__":
	lst = ["S", ["NP", ["DET", "There"]], ["S", ["VP", ["VERB", "is"], ["VP", ["NP", ["DET", "no"], ["NOUN", "asbestos"]], ["VP", ["PP", ["ADP","in"], ["NP", ["PRON", "our"]]], ["ADVP", ["ADV","now"]]]]]]]
	lst = []
	btree = BinaryTree(lst)
	# print btree.height()

	# print btree.get_root().right.left.right.right.left.left.left #in
	# from pprint import pprint
	# pprint(lst)
	lst = ["A", ["B", "D", "E"], "C"]
	btree = BinaryTree(lst)
	# print btree.count_leaf()
	# print btree.height()
	# print btree.get_root().left.left
	# print btree.is_balanced()

	# print btree.traverse("PreOrder")
	# print btree.traverse("PostOrder")
	# print btree.traverse("InOrder")
	# print btree.level_nodes()


	expression = ["+", ["*", 2, ["-", 10, 7]], ["+", 3, ["*", 2, 4]]]
	btree = BinaryTree(expression)
	print btree.get_root().left.left
	print btree.is_balanced()
	print btree.count_leaf()
	print btree.height()
	print btree.traverse("PreOrder")
	print btree.traverse("PostOrder")
	print btree.traverse("InOrder")
	print len(btree)

