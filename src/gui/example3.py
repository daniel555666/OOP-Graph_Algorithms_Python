import pygame
import pygame_menu
import random
import math as Math
from pygame import math
from pygame.constants import RESIZABLE
from DiGraph import DiGraph
# from GraphAlgo import GraphAlgo
from GraphAlgoInterface import GraphAlgoInterface

from src.Classes.GraphAlgo import GraphAlgo


class GUI():
    def __init__(self, graphAlgo: GraphAlgoInterface) -> None:
        self.graphAlgo = graphAlgo
        self.minX = self.minY = float('inf')
        self.maxX = self.maxY = float('-inf')
        self.findMaxAndMin()
        self.unitX = 0
        self.unitY = 0
        pygame.init()
        pygame.font.init()

        self.backgroundColor = (34, 189, 173)
        self.nodeColor = (227, 77, 148)
        self.buttonColor = (132, 176, 242)
        self.GAME_FONT = pygame.font.SysFont('comicsans', 15)
        self.screen = pygame.display.set_mode(
            [750, 500], RESIZABLE)  # Set up the drawing window

        self.run()

    def run(self):
        graphBotton = Button(self.buttonColor, 2, 2, 70, 20, 'Graph Optins')

        # Run until the user asks to quit
        running = True
        while running:
            #
            self.unitX = (self.screen.get_width() /
                          abs(self.maxX - self.minX) * 0.85)
            self.unitY = (self.screen.get_height() /
                          abs(self.maxY - self.minY) * 0.8)
            # Fill the background with white
            self.screen.fill(self.backgroundColor)
            # Did the user click the window close button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if graphBotton.isOver(pygame.mouse.get_pos()):
                        graphMenu = self.buildMenuGraph()
                        graphMenu.mainloop(self.screen)

            # Draw a solid blue circle in the center
            graphBotton.draw(self.screen, (0, 0, 0))
            self.drawEdges()
            self.drawNodes()
            # Flip the display
            pygame.display.flip()
        # Done! Time to quit.
        pygame.quit()

    def drawNodes(self):
        for node in self.graphAlgo.graph.nodes.values():
            x = (node.location[0] - self.minX) * self.unitX + 25
            y = (node.location[1] - self.minY) * self.unitY + 25

            pygame.draw.circle(self.screen, self.nodeColor, (x, y), 15)
            # You can use `render` and then blit the text surface ...
            text_surface = self.GAME_FONT.render(
                str(node.key), 10, (255, 255, 255))
            self.screen.blit(text_surface, (x - 5, y - 10))

    def findMaxAndMin(self):
        for node in self.graphAlgo.graph.nodes.values():
            if (node.location == None or node.location == ()):
                node.location = (random.uniform(0, 0.85), random.uniform(0, 0.8))
            x = node.location[0]
            y = node.location[1]

            if (self.minX > x):
                self.minX = x
            elif (self.maxX < x):
                self.maxX = x
            if (self.minY > y):
                self.minY = y
            elif (self.maxY < y):
                self.maxY = y

    def drawEdges(self):
        allEdges = self.graphAlgo.graph.edges
        for edge in allEdges.keys():
            srcX = self.graphAlgo.graph.nodes[edge[0]].location[0]
            srcX = (srcX - self.minX) * self.unitX + 25
            srcY = self.graphAlgo.graph.nodes[edge[0]].location[1]
            srcY = (srcY - self.minY) * self.unitY + 25

            destX = self.graphAlgo.graph.nodes[edge[1]].location[0]
            destX = (destX - self.minX) * self.unitX + 25
            destY = self.graphAlgo.graph.nodes[edge[1]].location[1]
            destY = (destY - self.minY) * self.unitY + 25

            # pygame.draw.line(self.screen, (0, 0, 0),(srcX, srcY), (destX, destY), 3)
            self.arrow((srcX, srcY), (destX, destY), 25, 10)
            w = str(allEdges[edge])
            try:
                w = f"{allEdges[edge]:.2f}"
            except:
                pass
            text_surface = self.GAME_FONT.render(w, 5, (255, 255, 255))
            self.screen.blit(
                text_surface, ((srcX * 0.25 + destX * 0.75), (srcY * 0.25 + destY * 0.75)))

    def arrow(self, start, end, d, h):
        dx = float(end[0] - start[0])
        dy = float(end[1] - start[1])
        D = float(Math.sqrt(dx * dx + dy * dy))
        xm = float(D - d)
        xn = float(xm)
        ym = float(h)
        yn = -h
        sin = dy / D
        cos = dx / D
        x = xm * cos - ym * sin + start[0]
        ym = xm * sin + ym * cos + start[1]
        xm = x
        x = xn * cos - yn * sin + start[0]
        yn = xn * sin + yn * cos + start[1]
        xn = x
        points = [(end[0], end[1]), (int(xm), int(ym)), (int(xn), int(yn))]

        pygame.draw.line(self.screen, (0, 0, 0), start, end)
        pygame.draw.polygon(self.screen, (0, 0, 0), points)

    def buildMenuGraph(self):
        graph = self.graphAlgo.graph
        menu = pygame_menu.Menu('Graph Options', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
        menu.add.button(f'Node Size is {graph.v_size()}', None)
        menu.add.button(f'Node Edge is {graph.e_size()}', None)
        menu.add.button('Add Edge', self.addEdge)
        menu.add.button('Close', menu.disable)
        return menu

    def addEdge(self):
        graph = self.graphAlgo.graph
        menu = pygame_menu.Menu('Add Edge', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
        menu.add.text_input('Src: ')
        menu.add.text_input('Dest: ')
        menu.add.text_input('Weight: ')
        menu.add.button(f'Enter', print)
        menu.add.button('Close', menu.disable)
        menu.mainloop(self.screen)
        return menu


class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 10)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


if __name__ == '__main__':
    graphAlgo = GraphAlgo()
    graphAlgo.load_from_json("./data/G1.json")
    gui = GUI(graphAlgo)