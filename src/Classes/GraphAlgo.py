import json
from typing import List

from src.Classes import SaveLoad
from src.Classes.DiGraph import DiGraph
from src.interfaces.GraphAlgoInterface import GraphAlgoInterface
from src.interfaces.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=None):
        self.graph = DiGraph(graph)

    def load_from_json(self, file_name: str) -> bool:
        self.g = SaveLoad.load(file_name)
        a = 5

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass

    def get_graph(self) -> GraphInterface:
        return self.g

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        # TODO

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        # TODO


if __name__ == '__main__':
    ga = GraphAlgo()
    ga.load_from_json("../../data/A0.json")
    ga.g.all_in_edges_of_node(1)
    a = 5
