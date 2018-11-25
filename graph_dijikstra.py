import random
class Dijikstra_graphs:
  def __init__ (self,graph):
    if graph != None:
      self.graph = graph
    else:
      self.graph = {} 
      return 'Empty dictionary initiated'
      
  def add_vertex(self,new_vertex):
    if new_vertex in self.graph:
      return 'vertex alrerady present in graph'
    if new_vertex not in self.graph:
      self.graph[new_vertex] = {}
      return 'Vertex Added to graph'
    

      
  def add_edge_weight(self,edge_weight):
    if edge_weight[0] in self.graph:
      self.graph[edge_weight[0]][edge_weight[1]] = edge_weight[2]
      return 'Edge added to Vertex'
      
    else:
      return 'Vertex not present in graph'
    
  def print_graph(self):
    for vertex in self.graph:
      for edge in self.graph[vertex]:
          print("vertex {} is linked to {} with weight of {}".format(vertex,edge,self.graph[vertex][edge]))
          
  def shortest_path(self):
    visited_vertex =     []
    unvisited_vertexes =  list(self.graph.keys())
    loop = 0 
    while len(unvisited_vertexes) != 0:
      unvisited = unvisited_vertexes.pop(0)
      if 
      
    
 

    
node_dictionary = {
                     1:{2:1,3:6},
                     2:{1:1,3:2,4:1},
                     3:{1:6,2:2,4:2,5:5},
                     4:{2:1,3:2,5:5},
                     5:{3:5,4:5}
                  }  



graph = Dijikstra_graphs(node_dictionary)
graph.shortest_path()
#print(graph.add_vertex(5))
#print(graph.add_edge_weight([5,4,5]))
#graph.print_graph()








