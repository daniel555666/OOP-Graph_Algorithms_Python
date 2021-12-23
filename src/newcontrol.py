import math
import sys
import pygame
import random
from src.Classes.DiGraph import DiGraph
from src.Classes.GraphAlgo import GraphAlgo

g = DiGraph()
ga = GraphAlgo()


# def DrawArrow(x1: int, y1: int, x2: int, y2: int):
#     dx = x2 - x1 + 5
#     dy = y2 - y1
#     angle = math.atan2(dy, dx)
#
#     len = int(math.sqrt(dx * dx + dy * dy))


#https://www.programcreek.com/python/?CodeExample=draw+arrow
def DrawArrow(x1,y1,x2,y2,size,widtha=5):
    dx = float(x2-x1)
    dy = float(y2-y1)
    D = float(math.sqrt(dx * dx + dy * dy))
    xm = float(D - size)
    xn = float(xm)
    ym = float(widtha)
    yn = -widtha
    sin = dy / D
    cos = dx / D
    x = xm * cos - ym * sin + x1
    ym = xm * sin + ym * cos + y1
    xm = x
    x = xn * cos - yn * sin + x1
    yn = xn * sin + yn * cos + y1
    xn = x
    return [(x2,y2),  (int(xm),  int(ym)),  (int(xn), int(yn))]




def GUI(file_name):
    ga.load_from_json(file_name=file_name)
    g = ga.get_graph()
    width = 1200
    height = 700
    pygame.init()
    black = [0, 0, 0]
    white = [255, 255, 255]
    size = [width, height]
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("EX3 Dolev Daniel Yakov")

    node_list = []
    src_edge_list = []
    dest_edge_list = []
    arrow_head_list = []
    # for edge in g.():
    #     #TODO
    #     pass

    incrementY = 50
    incrementX = 50
    minX = 100000000
    maxX = (-1)*100000000
    minY = 100000000
    maxY = (-1) * 100000000
    for node in g.get_all_v().values():
        minX = min(minX,node.x)
        maxX = max(maxX,node.x)
        minY = min(minY, node.y)
        maxY = max(maxY, node.y)

    scaleX = abs(maxX-minX)
    scaleY = abs(maxY-minY)

    factorX = width/scaleX * 0.8
    factorY = height/scaleY * 0.8

    for node in g.get_all_v().values():
        x = (node.x - minX)*factorX+ incrementX
        y = (node.y - minY) * factorY + incrementY
        node_list.append([x,y])

    for edge in ga.graph.Edges.values():
        x1 = incrementX + (g.get_all_v().get(edge.src).x-minX)*factorX
        y1 = incrementY + (g.get_all_v().get(edge.src).y-minY)*factorY
        x2 = incrementX + (g.get_all_v().get(edge.dest).x-minX)*factorX
        y2 = incrementY + (g.get_all_v().get(edge.dest).y-minY)*factorY
        if x1 > x2 :
            y1 = y1 - 5
            y2 = y2 - 5
        else:
            y1 = y1 + 5;
            y2 = y2 + 5;
        src_edge_list.append([x1,y1])
        dest_edge_list.append([x2,y2])
        arrow_head_list.append(DrawArrow(x1,y1,x2,y2,25))

    clock = pygame.time.Clock()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)


    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        window.fill(white)

        for edge in range(len(src_edge_list)):
            pygame.draw.line(window,black ,src_edge_list[edge], dest_edge_list[edge])
            pygame.draw.polygon(window,[255,0,0],arrow_head_list[edge])
        i =0
        for nodeV in node_list:
            pygame.draw.circle(window, black, nodeV, 10)
            textsurface = myfont.render(f"{i}", False, white)
            i += 1
            window.blit(textsurface,(nodeV[0]-7,nodeV[1]-5))
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    GUI("./data/A5.json")
