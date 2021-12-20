from src.Classes.CEdge import CEdge
from src.interfaces.GraphInterface import GraphInterface
from src.Classes.CNode import CNode


class DiGraph(GraphInterface):
    def __init__(self, Nodes:dict =None, Edges:dict =None):
        self.EdgesOut = {}
        self.EdgesIn = {}
        self.MC = 0
        if(Nodes == None):
            self.Nodes = {}
        else:
            self.Nodes = Nodes
        if(Edges == None):
            self.Edges = {}
        else:
            self.Edges = Edges
            for e in self.Edges:
                self.EdgesIn[e["src"]] = self.EdgesIn.get(e["src"], []) + [CEdge(src=e["src"], dest=e["dest"], w=e["w"])]
                self.EdgesOut[e["dest"]] = self.EdgesOut.get(e["dest"], []) + [CEdge(src=e["dest"], dest=e["src"], w=e["w"])]

    def v_size(self) -> int:
        """
        @return: The number of vertices in this graph
        """        
        return len(self.Nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """        
        return len(self.Edges)

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """        
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if f"{id1}_{id2}" not in self.Edges:
            self.Edges[f"{id1}_{id2}"] = CEdge(src=id1, dest=id2, w=weight)
            self.EdgesOut[id1] = self.EdgesOut.get(id1, []) + [CEdge(src=id1, dest=id2, w=weight)]
            self.EdgesIn[id2] = self.EdgesIn.get(id2, []) + [CEdge(src=id2, dest=id1, w=weight)]
            return True
        return False
                    
    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        https://stackoverflow.com/questions/11277432/how-can-i-remove-a-key-from-a-python-dictionary
        """
        if f"{node_id1}_{node_id2}" in self.Edges:
            del self.Edges[f"{node_id1}_{node_id2}"]
            # TODO need to fix because it will delete all the in and out edges instead of just 1
            del self.EdgesOut[node_id1]
            del self.EdgesIn[node_id2]
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if node_id not in self.Nodes:
            self.Nodes[node_id] = CNode(id=node_id, pos=pos)
            return True
        return False