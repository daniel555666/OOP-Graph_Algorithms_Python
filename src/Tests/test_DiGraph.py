from unittest import TestCase

from src.Classes.CNode import CNode
from src.Classes.DiGraph import DiGraph
from src.Classes.GraphAlgo import GraphAlgo


class TestDiGraph(TestCase):

    def test_v_size(self):
        g = DiGraph()
        g.add_node(1, (1, 2, 3))
        g.add_node(2, (1, 2, 3))
        g.add_node(3, (1, 2, 3))
        g.add_node(4, (1, 2, 3))
        nodes = g.get_all_v()
        self.assertEqual(4, len(nodes))
        print(g.get_all_v())
        self.assertEqual(nodes[1], CNode(id=1, pos=(1, 2, 3), info="white", length=None, rank=None, previous=None))
        self.assertEqual(nodes[2], CNode(id=2, pos=(1, 2, 3), info="white", length=None, rank=None, previous=None))
        self.assertEqual(nodes[3], CNode(id=3, pos=(1, 2, 3), info="white", length=None, rank=None, previous=None))
        self.assertEqual(nodes[4], CNode(id=4, pos=(1, 2, 3), info="white", length=None, rank=None, previous=None))

    def test_e_size(self):
        """
        an image for the example
        https://user-images.githubusercontent.com/62290677/147110925-fc31895e-d254-428f-af76-4840fd4f8d05.png
        """
        g = DiGraph()
        g.add_node(1, (1, 2, 3))
        g.add_node(2, (1, 2, 3))
        g.add_node(3, (1, 2, 3))
        g.add_node(4, (1, 2, 3))
        g.add_node(5, (1, 2, 3))
        g.add_edge(id1=2, id2=1, weight=2)
        g.add_edge(id1=1, id2=5, weight=5)
        g.add_edge(id1=3, id2=1, weight=3)
        g.add_edge(id1=4, id2=1, weight=4)
        print(g.all_in_edges_of_node(1))
        print(g.all_out_edges_of_node(1))
        self.assertEqual(g.all_in_edges_of_node(1), {2: (2, 2), 3: (3, 3), 4: (4, 4)})
        self.assertEqual(g.all_out_edges_of_node(1), {5: (5, 5)})
        self.assertEqual(4, g.e_size())

    def test_get_mc(self):
        g = DiGraph()
        self.assertEqual(0, g.get_mc())
        g.add_node(1, (1, 2, 3))
        self.assertEqual(1, g.get_mc())
        g.add_node(2, (1, 2, 3))
        self.assertEqual(2, g.get_mc())
        g.add_node(3, (1, 2, 3))
        self.assertEqual(3, g.get_mc())
        g.add_node(4, (1, 2, 3))
        self.assertEqual(4, g.get_mc())
        g.add_edge(id1=1, id2=2, weight=4)
        self.assertEqual(5, g.get_mc())
        g.remove_node(4)
        self.assertEqual(6, g.get_mc())
        g.remove_edge(node_id1=1, node_id2=2)
        self.assertEqual(7, g.get_mc())
        g.add_edge(id1=1, id2=2, weight=2)
        self.assertEqual(8, g.get_mc())
        g.add_edge(id1=2, id2=1, weight=1)
        self.assertEqual(9, g.get_mc())
        g.remove_node(1)
        self.assertEqual(10, g.get_mc())

    def test_add_edge(self):
        g = DiGraph()
        self.assertFalse(g.add_edge(1, 2, 3.5))

    def test_remove_node(self):
        g = DiGraph()
        ga = GraphAlgo()
        ga.load_from_json("../../data/A0.json")
        a = 5
        self.fail()

    def test_remove_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_get_all_v(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        ga = GraphAlgo()
        ga.load_from_json("../../data/A0.json")
        g = ga.get_graph()
        print(g.all_in_edges_of_node(0))
        a = 5
        self.assertEqual()

    def test_all_out_edges_of_node(self):
        self.fail()
