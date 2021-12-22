from src.Classes.DiGraph import DiGraph
from src.Classes.GraphAlgo import GraphAlgo
import matplotlib.pyplot as plt

gStatic = DiGraph()
gaStatic = GraphAlgo()
def drawGraph(filename):
    Nodes = gStatic.get_all_v()
    x_list = []
    y_list = []
    for node in Nodes:
        x_list.append(node.x)
        y_list.append(node.y)

    fig, ax = plt.subplots()
    ax.scatter(x_list, y_list)

    for i, txt in enumerate(Nodes):
        ax.annotate(Nodes[i], (x[i] + 0.005, y[i] + 0.005))  # arrowprops=dict(arrowstyle="simple")
    plt.xlabel("x axis ")
    plt.ylabel("y axis ")
    plt.title("The title of the graph")
    plt.plot(x, y)
    plt.show()



if __name__ == '__main__':
    gaStatic.load_from_json("../../data/A0.json")
    g = gaStatic.get_graph()
    drawGraph("dolev")

