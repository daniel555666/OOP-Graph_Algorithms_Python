import math
import sys
from threading import Timer
import pygame

from src.Classes.DiGraph import DiGraph
from src.Classes.GraphAlgo import GraphAlgo
from src.gui.Button import Button
import src.gui.constants


# ga, minX, minY, factorX, incrementX, factorY, incrementY, getminmax

def reset_center():
    src.gui.constants.center_node = None

def reset_tsp():
    src.gui.constants.tsp_list = None


def center_ga():
    (center_n, a) = src.gui.constants.ga.centerPoint()
    src.gui.constants.center_node = center_n


def tsp_ga(user_text):
    split_str = user_text.split(",")
    node_id_list = []
    for s in split_str:
        node_id_list.append(int(s))
    (tsp_l, a) = src.gui.constants.ga.TSP(node_id_list)
    src.gui.constants.tsp_list = tsp_l
    print(src.gui.constants.tsp_list)


def draw_arrow(x1, y1, x2, y2, size=12, widtha=5):
    """
    make an arrow edge.
    @param x1: node1.x
    @param x2: node2.x
    @param y1: node1.y
    @param y2: node2.y
    @param size: the size of the triangle
    @param widtha: the width of the triangle
    draw the arrow :)
    """
    y_diffrance = float(y2 - y1)
    x_diffrance = float(x2 - x1)
    distance_result = float(math.sqrt(x_diffrance * x_diffrance + y_diffrance * y_diffrance))
    minimum_x_distance = float(distance_result - size)
    node_minmimum = float(minimum_x_distance)
    dest_y_min = float(widtha)
    dest_y_max = -widtha
    divide1 = y_diffrance / distance_result
    devide2 = x_diffrance / distance_result
    trace = minimum_x_distance * devide2 - dest_y_min * divide1 + x1
    dest_y_min = minimum_x_distance * divide1 + dest_y_min * devide2 + y1
    minimum_x_distance = trace
    trace = node_minmimum * devide2 - dest_y_max * divide1 + x1
    dest_y_max = node_minmimum * divide1 + dest_y_max * devide2 + y1
    node_minmimum = trace
    return [(x2, y2), (int(minimum_x_distance), int(dest_y_min)), (int(node_minmimum), int(dest_y_max))]


def GUI(file_name):
    src.gui.constants.ga.load_from_json(file_name=file_name)
    g = src.gui.constants.ga.get_graph()
    width = 1200
    height = 700
    pygame.init()
    black = [0, 0, 0]
    white = [255, 255, 255]
    size = [width, height]
    window = pygame.display.set_mode(size)
    center_button = Button((150, 20, 30), 2, 2, 70, 20, 'center')
    # tsp_button = Button((150, 20, 30), 2, 2, 70, 20, 'tsp')

    pygame.display.set_caption("EX3 Dolev Daniel Yakov")
    node_list = []
    src_edge_list = []
    dest_edge_list = []
    arrow_head_list = []

    src.gui.constants.getminmax()

    for node in g.get_all_v().values():
        n_id = node.id
        x = (node.x - src.gui.constants.minX) * src.gui.constants.factorX + src.gui.constants.incrementX
        y = (node.y - src.gui.constants.minY) * src.gui.constants.factorY + src.gui.constants.incrementY
        node_list.append([x, y, n_id])

    for edge in src.gui.constants.ga.graph.Edges.values():
        x1 = src.gui.constants.incrementX + (
                g.get_all_v().get(edge.src).x - src.gui.constants.minX) * src.gui.constants.factorX
        y1 = src.gui.constants.incrementY + (
                g.get_all_v().get(edge.src).y - src.gui.constants.minY) * src.gui.constants.factorY
        x2 = src.gui.constants.incrementX + (
                g.get_all_v().get(edge.dest).x - src.gui.constants.minX) * src.gui.constants.factorX
        y2 = src.gui.constants.incrementY + (
                g.get_all_v().get(edge.dest).y - src.gui.constants.minY) * src.gui.constants.factorY
        if x1 > x2:
            y1 = y1 - 5
            y2 = y2 - 5
        else:
            y1 = y1 + 5
            y2 = y2 + 5
        src_edge_list.append([x1, y1])
        dest_edge_list.append([x2, y2])
        arrow_head_list.append(draw_arrow(x1, y1, x2, y2))

    clock = pygame.time.Clock()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 10)

    base_font = pygame.font.Font(None, 30)
    user_text = 'tsp'
    input_rect = pygame.Rect(0, 25, 140, 32)
    color_active = (102, 51, 153)
    color_passive = (216, 191, 216)
    color = color_passive
    active = False

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        tsp_ga(user_text)
                        user_text = 'tsp'
                        active = False
                    else:
                        user_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if center_button.isOver(pygame.mouse.get_pos()):
                    center_ga()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                        user_text = ''
                    else:
                        active = False

        window.fill(white)

        for edge in range(len(src_edge_list)):
            pygame.draw.line(window, black, src_edge_list[edge], dest_edge_list[edge])
            pygame.draw.polygon(window, [46, 139, 87], arrow_head_list[edge])

        for nodeV in node_list:
            pygame.draw.circle(window, black, [nodeV[0], nodeV[1]], 10)
            textsurface = myfont.render(f"{nodeV[2]}", False, white)
            window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))

            if src.gui.constants.center_node == nodeV[2]:
                pygame.draw.circle(window, (26, 10, 166), [nodeV[0], nodeV[1]], 10)
                textsurface = myfont.render(f"{nodeV[2]}", False, white)
                window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))
                timeout = Timer(5.0, reset_center)
                timeout.start()

            if src.gui.constants.tsp_list is not None:
                if nodeV[2] in src.gui.constants.tsp_list:
                    pygame.draw.circle(window, (140, 64, 6), [nodeV[0], nodeV[1]], 10)
                    textsurface = myfont.render(f"{nodeV[2]}", False, white)
                    window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))
                    timeout2 = Timer(5.0, reset_tsp)
                    timeout2.start()

        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(window, color, input_rect, 2)
        text_surface = base_font.render(user_text, True, (0, 0, 128))
        window.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(text_surface.get_width() + 10, 75)

        center_button.draw(window)
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    GUI("./data/A5.json")
