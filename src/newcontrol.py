import math
import sys
import pygame
import random
from src.Classes.DiGraph import DiGraph
from src.Classes.GraphAlgo import GraphAlgo

g = DiGraph()
ga = GraphAlgo()

#https://www.programcreek.com/python/?CodeExample=draw+arrow
def DrawArrow(x, y, angle=0):
    def rotate(pos, angle):
        cen = (5 + x, 0 + y)
        angle *= -(math.pi / 180)
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        ret = ((cos_theta * (pos[0] - cen[0]) - sin_theta * (pos[1] - cen[1])) + cen[0],
               (sin_theta * (pos[0] - cen[0]) + cos_theta * (pos[1] - cen[1])) + cen[1])
        return ret

    p0 = rotate((0 + x, -4 + y), angle + 90)
    p1 = rotate((0 + x, 4 + y), angle + 90)
    p2 = rotate((10 + x, 0 + y), angle + 90)
    return [p0,p1,p2]
    #pygame.draw.polygon(self.screen, color, [p0, p1, p2])


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
        src_edge_list.append([x1,y1])
        dest_edge_list.append([x2,y2])
        arrow_head_list.append(DrawArrow(x2,y2))

    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        window.fill(white)
        for vert in node_list:
            pygame.draw.circle(window, black, vert, 2)
        for edge in range(len(src_edge_list)):
            pygame.draw.line(window,black ,src_edge_list[edge], dest_edge_list[edge])
            # pygame.draw.polygon(window,black,(src_edge_list[edge][0],src_edge_list[edge][1]),(dest_edge_list[edge][0],dest_edge_list[edge][1]))
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    GUI("./data/A5.json")
