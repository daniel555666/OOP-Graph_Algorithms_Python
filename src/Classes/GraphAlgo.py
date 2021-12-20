import json

from src.Classes.DiGraph import DiGraph
from src.interfaces.GraphAlgoInterface import GraphAlgoInterface



class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g=None):
        self.g = DiGraph(g)

    def load_from_json(self, file_name: str) -> bool:
        file = open(file_name, "r")
        GraphDict = json.load(file)
        file.close()
        graph = DiGraph()
        for n in GraphDict["Nodes"]:
            pos = n["pos"].split(",")
            xyz = (float(pos[0]), float(pos[1]), float(pos[2]))
            node_id = int(n["id"])
            graph.add_node(node_id, xyz)
        for e in GraphDict["Edges"]:
            graph.add_edge(int(e["src"]), int(e["dest"]), float(e["w"]))
        self.g = graph

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass


if __name__ == '__main__':
    ga = GraphAlgo()
    ga.load_from_json("../../data/A0.json")
    a = 5
