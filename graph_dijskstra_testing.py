import unittest
import sys 
import io
import re
from graph_dijikstra import  Dijikstra_graphs

class Dijikstra_graphs_testing(unittest.TestCase):
  
  def setUp(self):
    graph_weighted_dictionary = {
                
                                   1:{2:1,3:6},
                                   2:{1:1,3:2,4:1},
                                   3:{1:6,2:2,4:2,5:5},
                                   4:{2:1,3:2,5:5},
                                   5:{3:5,4:5}
                                 } 
    self.graph =  Dijikstra_graphs(graph_weighted_dictionary)
  
  def test_object_of_class(self):
    self.assertIsInstance(self.graph,Dijikstra_graphs)
      
  def test_add_vertex(self):    
    add_vertex = self.graph.add_vertex(5)
    self.assertEqual(add_vertex,'vertex alrerady present in graph')
    add_vertex = self.graph.add_vertex(6)
    self.assertEqual(add_vertex,'Vertex Added to graph')
    
  def test_add_edge_weight(self): 
    add_edge_weight = self.graph.add_edge_weight(12)
    self.assertEqual(add_edge_weight,'Vertex not present in graph')
    add_vertex = self.graph.add_vertex(6)
    add_edge_weight = self.graph.add_edge_weight([6,2,12])
    self.assertEqual(add_edge_weight,'Edge added to Vertex')
  
  def test_shortest_path(self):
    shortest_path = self.graph.shortest_path()
    self.assertNotEqual(shortest_path,shortest_path)
    
      
    
    

    
if __name__ == '__main__':
  unittest.main()      