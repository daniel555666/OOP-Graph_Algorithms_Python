import json
from src.Classes.DiGraph import DiGraph


def load(file_name):
    file = open(file_name, "r")
    graph_dict = json.load(file)
    file.close()
    graph = DiGraph()
    for n in graph_dict["Nodes"]:
        pos = n["pos"].split(",")
        xyz = (float(pos[0]), float(pos[1]), float(pos[2]))
        node_id = int(n["id"])
        graph.add_node(node_id, xyz)
    for e in graph_dict["Edges"]:
        graph.add_edge(int(e["src"]), int(e["dest"]), float(e["w"]))
    return graph
