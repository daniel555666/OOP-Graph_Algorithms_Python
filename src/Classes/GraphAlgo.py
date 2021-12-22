import json
import sys
from queue import PriorityQueue

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
        graph = self.graph
        q = PriorityQueue() # need to check if the q is - or +
        for node in graph.Edges:
            node.length = sys.maxsize
            node.previous=None
            q.put(node)
        graph.Nodes.get(id1).length=0

        while not q.empty():
            current=q.get()
            dictOfCurrent=graph.all_out_edges_of_node(current.id)
            for TupleNode in dictOfCurrent.values():
                if



    def plot_graph(self) -> None:
        pass

    def get_graph(self) -> GraphInterface:
        return self.g


if __name__ == '__main__':
    ga = GraphAlgo()
    ga.load_from_json("../../data/A0.json")
    ga.g.all_in_edges_of_node(1)
    a = 5
