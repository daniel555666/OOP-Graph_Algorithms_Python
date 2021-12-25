from unittest import TestCase
from Classes.GraphAlgo import GraphAlgo

class TestGraphAlgo(TestCase):
    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_plot_graph(self):
        ga =GraphAlgo()
        ga.load_from_json("/Users/yakovkhodorkovski/PycharmProjects/Ex3/data/T1.json")
        ga.plot_graph()
        self.assertNotEqual(ga.get_graph().get_all_v().get(0).x , None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(1).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(2).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(3).x, None)

        ga.load_from_json("/Users/yakovkhodorkovski/PycharmProjects/Ex3/data/T2.json")
        ga.plot_graph()
        self.assertNotEqual(ga.get_graph().get_all_v().get(0).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(1).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(2).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(3).x, None)

        ga.load_from_json("/Users/yakovkhodorkovski/PycharmProjects/Ex3/data/T3.json")
        ga.plot_graph()
        self.assertNotEqual(ga.get_graph().get_all_v().get(0).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(1).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(2).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(3).x, None)

