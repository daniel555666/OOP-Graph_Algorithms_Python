from src.CEdge import CEdge
from src.GraphInterface import GraphInterface
from src.CNode import CNode


class DiGraph(GraphInterface):
    def __init__(self, Nodes=None, Edges=None):
        self.MC = 0
        if(Nodes == None):
            self.Nodes = {}
        else:
            self.Nodes = Nodes
        if(Edges == None):
            self.Edges = {}
        else:
            self.Edges = Edges
        self.EdgesOut = {}
        self.EdgesIn = {}

    def v_size(self) -> int:
        return len(self.Edges)

    def e_size(self) -> int:
        pass

    def get_mc(self) -> int:
        pass

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        self.Edges[f"{id1}_{id2}"] = CEdge(src=id1, dest=id2, w=weight)
        self.EdgesOut[id1] = self.EdgesOut.get(id1, []) + [CEdge(src=id1, dest=id2, w=weight)]
        self.EdgesIn[id2] = self.EdgesIn.get(id2, []) + [CEdge(src=id2, dest=id1, w=weight)]

    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        self.Nodes[node_id] = CNode(id=node_id, pos=pos)
        return True
