from src.Classes.DiGraph import DiGraph
from src.Classes.GraphAlgo import GraphAlgo

ga = GraphAlgo()

tsp_list = None
shortest_path_list = None

width = 1200
height = 700
incrementY = 50
incrementX = 50
minX = 100000000
maxX = (-1) * 100000000
minY = 100000000
maxY = (-1) * 100000000
scaleX = 0
scaleY = 0
factorX = 0
factorY = 0
center_node = None


def getminmax():
    global minX
    global maxX
    global minY
    global maxY
    global scaleX
    global scaleY
    global factorX
    global factorY

    for node in ga.graph.get_all_v().values():
        minX = min(minX, node.x)
        maxX = max(maxX, node.x)
        minY = min(minY, node.y)
        maxY = max(maxY, node.y)

    scaleX = abs(maxX - minX)
    scaleY = abs(maxY - minY)

    factorX = width / scaleX * 0.8
    factorY = height / scaleY * 0.8
