import sys
import pygame
import random
from src.Classes.DiGraph import DiGraph
from src.Classes.GraphAlgo import GraphAlgo

g = DiGraph()
ga = GraphAlgo()


def GUI(file_name):
    ga.load_from_json(file_name=file_name)
    g = ga.get_graph()

    pygame.init()
    black = [0, 0, 0]
    white = [255, 255, 255]
    size = [1200, 700]
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("EX3 Dolev Daniel Yakov")

    node_list = []
    snow_list = []
    # for edge in g.():
    #     #TODO
    #     pass
    for node in g.get_all_v().values():
        print(node)
        x = int(random.randrange(0, 1200))
        y = int(random.randrange(0, 700))
        node_list.append([x, y])
        # snow_list.append([x, y])
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        window.fill(white)
        for i in node_list:
            pygame.draw.circle(window, black, node_list[i], 2)

        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    GUI("./data/T0.json")
