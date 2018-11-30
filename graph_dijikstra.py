import random
class Dijikstra_graphs:
  def __init__ (self,graph):
    if graph != None:
      self.graph = graph
    else:
      self.graph = {} 
      return 'Empty dictionary initiated'
      
  def add_vertex(self,new_vertex):
    """function to add vertex"""
    if new_vertex in self.graph:
      return 'vertex alrerady present in graph'
    if new_vertex not in self.graph:
      self.graph[new_vertex] = {}
      return 'Vertex Added to graph'
  
  def add_edge_weight(self,edge_weight):
      """function to add edge and weight to the graph"""
    if edge_weight[0] in self.graph:
      self.graph[edge_weight[0]][edge_weight[1]] = edge_weight[2]
      return 'Edge and weight added to Vertex'
    else:
      return 'Vertex not present in graph'
    
  def print_graph(self):
    """ function to print the graph with vertex , weight , and edges""""
    for vertex in self.graph:
      for edge in self.graph[vertex]:
          print("vertex {} is linked to {} with weight of {}".format(vertex,edge,self.graph[vertex][edge]))
          
  def shortest_path(self):
    """ function implementing dijkstra algorithm - selects a random source 
    vertex and returns the shortest distance from it to all """
    import math , random
    unvisited_vertexes  = list(self.graph.keys())
    known_path       = {}
    visited_vertex   =  [] 
    starting_vertex  =  random.choice(unvisited_vertexes)    
    for keys in unvisited_vertexes:
      known_path[keys] = float('inf')
      if keys == starting_vertex:
        known_path[keys] = 0
    print("Our Source Vertex is {}".format(starting_vertex))
    while len(unvisited_vertexes) != 0:
      min_value_dictionary = known_path.copy()
      for key in list(min_value_dictionary):
        if key in visited_vertex:
          del min_value_dictionary[key]
      vertex =  min(min_value_dictionary, key = min_value_dictionary.get) 
      if vertex in unvisited_vertexes:
        for edges in self.graph[vertex]:
          totalweight = known_path[vertex] + self.graph[vertex][edges]
          if totalweight < known_path[edges]:
            known_path[edges] = totalweight  
      visited_vertex.append(vertex)
      unvisited_vertexes.remove(vertex)
    for vertex in known_path:
      print("{} is connected to {} by shortest diatnce of {}".format(starting_vertex,vertex,known_path[vertex]))
    return known_path
  
graph_weighted_dictionary = {
                     1:{2:1,3:6},
                     2:{1:1,3:2,4:1},
                     3:{1:6,2:2,4:2,5:5},
                     4:{2:1,3:2,5:5},
                     5:{3:5,4:5}
                  }  
graph = Dijikstra_graphs(graph_weighted_dictionary)
#graph.shortest_path()
print(graph.add_vertex(6))
print(graph.add_edge_weight([6,4,5]))
#graph.print_graph()








