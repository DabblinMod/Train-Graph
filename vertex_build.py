class Vertex:
	#the constructor
	def __init__(self, value):
		self.value=value
		self.edges={} #an empty dictionary

	#add_edge method here
	def add_edge(self, adj_value, weight):
			#adding a vertex to the list of edges
			#add using the name of the vertex value
			print("Adding edge to " , adj_value)
			self.edges[adj_value] = weight
			
	def get_edges(self):#returns a list of the keys
		#method will return a list of the names of the vertices
		#that are connected to the self.
		return list(self.edges.keys())
