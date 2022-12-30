from bfs_graph import Graph
from vertex_build import Vertex

#create graph object
call_graph=Graph()

#vertexes to go on graph
#each vertex is a radio station
rockney=Vertex("Rockney Station")
fp=Vertex("Flander's Puk Station")
wagon=Vertex("Wagon Station")
gizdome=Vertex("Giz Dome Station")
forty_station=Vertex("The 40th Station")
twenty_station=Vertex("The 20th Station")
raven=Vertex("Raven Station")
asht=Vertex("Sass Ashtern Station")
karneval=Vertex("Karneval W5 Station")

#add vertices / vertex objects to the graph
call_graph.add_vertex(rockney)
call_graph.add_vertex(wagon)
call_graph.add_vertex(gizdome)
call_graph.add_vertex(forty_station)
call_graph.add_vertex(twenty_station)
call_graph.add_vertex(raven)
call_graph.add_vertex(asht)
call_graph.add_vertex(karneval)

#add edges / connections between stations
call_graph.add_a_edge(wagon, gizdome, 5) #single direction edge
call_graph.add_edge(wagon, forty_station, 7)
call_graph.add_edge(rockney, wagon, 3) #rest are undirected
call_graph.add_edge(rockney, gizdome, 5)
call_graph.add_edge(rockney, forty_station, 12)
call_graph.add_edge(twenty_station, raven, 1)
call_graph.add_edge(twenty_station, asht, 9)
call_graph.add_edge(forty_station, twenty_station, 3)
call_graph.add_edge(forty_station, gizdome, 5)
call_graph.add_edge(forty_station, raven, 8)
call_graph.add_edge(raven, wagon, 19)
call_graph.add_edge(raven, asht, 3)
call_graph.add_edge(raven, karneval, 6)
call_graph.add_edge(gizdome, twenty_station, 2)
call_graph.add_edge(gizdome, asht, 11)
call_graph.add_edge(asht, karneval, 4)
call_graph.add_edge(asht, twenty_station, 9)

###do not remove or change
call_graph.breadth_first("Rockney Station", "Karneval W5 Station")
print(call_graph.graph_dict)