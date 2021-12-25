from unittest import TestCase
from Classes.GraphAlgo import GraphAlgo
import os


class TestGraphAlgo(TestCase):
    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "../data/short1.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga = GraphAlgo()
        ga.load_from_json(abs_file_path)


    def test_plot_graph(self):
        """
        because of the problem with python that needs the absolute path if the file you
        try to open is in a directory that is not in the Which is not smaller than her in her hierarchy or neighbor
        in the location of the function activation
        we use the absolute path for the checks.
        ** update we learned to use os.path to fix that
        """
        script_dir = os.path.dirname(__file__)
        rel_path = "../data/T1.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga = GraphAlgo()
        ga.load_from_json(abs_file_path)
        ga.plot_graph()
        self.assertNotEqual(ga.get_graph().get_all_v().get(0).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(1).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(2).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(3).x, None)
        rel_path = "../data/T2.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga.load_from_json(abs_file_path)
        ga.plot_graph()
        self.assertNotEqual(ga.get_graph().get_all_v().get(0).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(1).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(2).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(3).x, None)
        rel_path = "../data/T3.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga.load_from_json(abs_file_path)
        ga.plot_graph()
        self.assertNotEqual(ga.get_graph().get_all_v().get(0).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(1).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(2).x, None)
        self.assertNotEqual(ga.get_graph().get_all_v().get(3).x, None)
