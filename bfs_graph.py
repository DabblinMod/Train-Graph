from vertex_build import Vertex

class Graph: #this will be a BFS Graph
    #bidirectional / undirected
    def __init__(self):
        self.graph_dict={} #holds the vertices on the graph as a dictionary
       
    def add_vertex(self, obj):
    #key is the string name of the vertex, and its value is its obj memory
        self.graph_dict[obj.value]=obj
        
    def add_a_edge(self, from_vertex, to_vertex, weight):
        #calls the Vertex add_edge function within the Vertex class
       self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    
    def add_edge(self, from_vertex, to_vertex, weight):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
        
    def breadth_first(self, start_vertex, end_vertex):
        #take the start vertex and use it to get the current value
        #build a loop to check the other vertices
        queue=[start_vertex]
        seen={} #refers to already checked vertices
        print(f"Starting at {start_vertex} and final stop is {end_vertex}\n")
        while queue: #as long as queue isn't empty
            current_vertex=queue.pop(0) #retrieves current vertex
            node=self.graph_dict[current_vertex] #stores vertex object
            #use a loop to go through the connections the current loop has
            print(f"Current vertex is: {current_vertex}")
            seen[current_vertex]=True #to display the node has been visited.
            for next_station, value in node.edges.items():
                #you call the vertex node's edges, which all have a vertex value = a weight
                print(f"If you take this ride, the next station is {next_station} and it \
                takes {value} hours to get to.")
            print("\n")
            #pick the path you want to go
            chosen_vertex=input("Choose your next destination: ")
            if chosen_vertex==end_vertex:
                print("We have reached our destination")
                return "We have reached our destination"
            else:
                queue.append(chosen_vertex)
                print(f"Current queue is: {queue}")