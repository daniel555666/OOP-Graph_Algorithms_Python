from unittest import TestCase
from src.Classes.DiGraph import DiGraph
from src.Classes.GraphAlgo import GraphAlgo


class TestDiGraph(TestCase):
    def test_v_size(self):
        self.fail()

    def test_e_size(self):
        self.fail()

    def test_get_mc(self):
        self.fail()

    def test_add_edge(self):
        self.fail()

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

    def test_all_out_edges_of_node(self):
        self.fail()
