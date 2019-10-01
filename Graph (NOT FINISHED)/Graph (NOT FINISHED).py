from collections import defaultdict

class Vertex():
	def __init__(self, name=None):
		self.name = name
		self.__visited = False

	def __repr__(self):
		return "Vertex({})".format(self.name)

	def __eq__(self, other):
		return self.name == other.name	#case-sensitive

	def is_visited(self):
		return self.__visited

	def make_visited(self):
		self.__visited = True


class Edge():
	def __init__(self, weight, start_vertex, end_vertex):
		self.weight = weight
		self.start = start_vertex
		self.end = end_vertex

	def __repr__(self):
		if self.weight:
			return "{}->{} ({})".format(self.start, self.end, self.weight)
		else:
			return "{}->{}".format(self.start, self.end)




class Graph():
	def __init__(self, vertices, edges, directed):
		self.vertices = vertices
		self.edges = edges
		self.directed = directed
		self.graph = defaultdict(set)
		for vertex in vertices:
			for edge in self.get_edges(vertex):
				if vertex == edge.start:
					self.graph[vertex.name].add( (edge.end.name, edge.weight) )
				else:
					self.graph[vertex.name].add( (edge.start.name, edge.weight) )

	

	def get_edges(self, vertex):
		if self.directed:
			output = [edge for edge in self.edges if edge.start == vertex]
		else:
			output = [edge for edge in self.edges if edge.start == vertex or edge.end == vertex]
		return output

	
	stack = []
	def depth_first_tranverse(self, vertex):
		global stack
		vertices = self.graph[vertex.name]
		i = 0
		while True:
			other = vertices[i][0]
			if not other.is_visited():
				other.make_visited()
				stack.append(vertex)
				break
			else:
				i += 1




		








lst = [Vertex("S"), Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D")]
sa = Edge(None, Vertex("S"), Vertex("A"))
sb = Edge(None, Vertex("S"), Vertex("B"))
sc = Edge(None, Vertex("S"), Vertex("C"))
ad = Edge(None, Vertex("A"), Vertex("D"))
bd = Edge(None, Vertex("B"), Vertex("D"))
cd = Edge(None, Vertex("C"), Vertex("D"))
edges = [sa, sb, sc, ad, bd, cd]
g = Graph(lst, edges, directed=False)

print g.graph['S'][0][0]
print g.graph['A']
print g.graph['B']
print g.graph['C']
print g.graph['D']
# print g.get_edges(Vertex("S"))
# print g.get_edges(Vertex("A"))
# print g.get_edges(Vertex("B"))
# print g.get_edges(Vertex("C"))
# print g.get_edges(Vertex("D"))
