import unittest as unit_test
from graph_search import find_path
from graph_search import read_file

# Test cases for read_file function
class TestGraph(unit_test.TestCase):

    #Check if file exists before trying to read it
    def test_read_file_not_found(self):                                
        graph = read_file("not_exist.csv")                             
        self.assertIsNone(graph) 

    # Test case for wrong file extension
    def test_read_file_wrong_extension(self):                          
        graph = read_file("graph.json")                                
        self.assertIsNone(graph) 
    
    # Test case for file with incomplete columns
    # This test assumes that the file "bad_graph.csv" exists and contains lines with fewer than 3 columns.
    def test_read_file_incomplete_columns(self):
      graph = read_file("bad_graph.csv")
      self.assertIsNone(graph) 

    # Test case for file with invalid cost values
    # This test assumes that the file "bad_cost.csv" exists and contains lines where the cost value is not a valid integer.
    def test_read_file_invalid_cost(self):                              
      graph = read_file("bad_cost.csv")                   
      self.assertIsNone(graph) 
      
    # Test case for valid file
    def test_read_valid_file(self):                                    
        graph = read_file("graph.csv")                                 
        self.assertIsNotNone(graph)                                    
        self.assertIsInstance(graph, dict) 


# Test cases for find_path function
class TestGraphPath(unit_test.TestCase):
    
    def setUp(self):
        self.graph = read_file("graph.csv")

    def test_path_A_to_B(self):
        path, cost = find_path(self.graph, 'A', 'B')
        self.assertEqual(path, ['A', 'B'])
        self.assertEqual(cost, 5)

    def test_path_B_to_A(self):
        path, cost = find_path(self.graph, 'B', 'A')
        self.assertEqual(path, ['B', 'A'])
        self.assertEqual(cost, 5)

    def test_path_C_to_F(self):
        path, cost = find_path(self.graph, 'C', 'F')
        self.assertEqual(path, ['C', 'G', 'H', 'F'])
        self.assertEqual(cost, 10)

    def test_path_F_to_G(self):
        path, cost = find_path(self.graph, 'F', 'G')
        self.assertEqual(path, ['F', 'H', 'G'])
        self.assertEqual(cost, 8)

    def test_path_F_to_C(self):
        path, cost = find_path(self.graph, 'F', 'C')
        self.assertEqual(path, ['F', 'H', 'G', 'C'])
        self.assertEqual(cost, 10)

    def test_path_f_to_c(self):
        path, cost = find_path(self.graph, 'f', 'c')
        self.assertEqual(path, ['F', 'H', 'G', 'C'])
        self.assertEqual(cost, 10)

    def test_path_A_to_I(self):
        path, cost = find_path(self.graph, 'A', 'I')
        self.assertIsNone(path)
        self.assertEqual(cost, float('inf'))

    # value of cost decimal and negative cost
    def test_decimal_cost(self):
        graph = {
            'A': {'B': 1.5, 'C': 5.0},
            'B': {'A': 1.5, 'C': 2.5},
            'C': {'A': 5.0, 'B': 2.5},
        }
        path, cost = find_path(graph, 'A', 'C')
        self.assertEqual(path, ['A', 'B', 'C'])
        self.assertAlmostEqual(cost, 4.0)

    def test_negative_cost(self):
        graph = {
            'A': {'B': 5,  'C': 10},
            'B': {'A': 5,  'C': -3},
            'C': {'A': 10, 'B': -3},
        }
        path, cost = find_path(graph, 'A', 'C')
        self.assertEqual(path, ['A', 'B', 'C'])
        self.assertEqual(cost, 2)

if __name__ == '__main__':

    unit_test.main()