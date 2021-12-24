import sys
from threading import Timer
import pygame
from src.gui.Button import Button
import src.gui.constants
from src.gui.algo_func import tsp_ga, center_ga, reset_center, reset_tsp, shortest_ga, reset_shortest, \
    reset_shortest_string, reset_tsp_string
from src.gui.graph_func import add_node_g, reset_add_node_string, remove_node_g, reset_remove_node_string


def GUI(file_name):
    src.gui.constants.ga.load_from_json(file_name=file_name)
    pygame.init()
    black = [0, 0, 0]
    white = [255, 255, 255]
    size = [src.gui.constants.width, src.gui.constants.height]
    window = pygame.display.set_mode(size)
    center_button = Button((150, 20, 30), 2, 2, 70, 20, 'center')
    pygame.display.set_caption("EX3 Dolev Daniel Yakov")
    src.gui.constants.getminmax()
    src.gui.constants.calculate_values()
    clock = pygame.time.Clock()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 10)
    base_font_tsp = pygame.font.Font(None, 20)
    input_rect_tsp = pygame.Rect(0, 25, 140, 20)
    color_active_tsp = (102, 51, 153)
    color_passive_tsp = (216, 191, 216)
    active_tsp = False

    base_font_shortest = pygame.font.Font(None, 20)
    input_rect_shortest = pygame.Rect(0, 50, 140, 20)
    color_active_shortest = (102, 51, 153)
    color_passive_shortest = (216, 191, 216)
    active_shortest = False

    base_font_add_node = pygame.font.Font(None, 20)
    input_rect_add_node = pygame.Rect(80, 1, 140, 20)
    color_active_add_node = (102, 51, 153)
    color_passive_add_node = (216, 191, 216)
    active_add_node = False

    base_font_remove_node = pygame.font.Font(None, 20)
    input_rect_remove_node = pygame.Rect(80, 22, 140, 20)
    color_active_remove_node = (102, 51, 153)
    color_passive_remove_node = (216, 191, 216)
    active_remove_node = False


    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if active_tsp == True:
                    if event.key == pygame.K_BACKSPACE:
                        src.gui.constants.user_text_tsp = src.gui.constants.user_text_tsp[:-1]
                    elif event.key == pygame.K_RETURN:
                        cost = tsp_ga(src.gui.constants.user_text_tsp)
                        src.gui.constants.user_text_tsp = "{:.4f}".format(cost)
                        timeout = Timer(5.0, reset_tsp_string)
                        timeout.start()
                        active_tsp = False
                    else:
                        src.gui.constants.user_text_tsp += event.unicode

                if active_shortest == True:
                    if event.key == pygame.K_BACKSPACE:
                        src.gui.constants.user_text_shortest = src.gui.constants.user_text_shortest[:-1]
                    elif event.key == pygame.K_RETURN:
                        cost = shortest_ga(src.gui.constants.user_text_shortest)
                        src.gui.constants.user_text_shortest = "{:.4f}".format(cost)
                        timeout = Timer(5.0, reset_shortest_string)
                        timeout.start()
                        active_shortest = False
                    else:
                        src.gui.constants.user_text_shortest += event.unicode

                if active_add_node == True:
                    if event.key == pygame.K_BACKSPACE:
                        src.gui.constants.user_text_add_node = src.gui.constants.user_text_add_node[:-1]
                    elif event.key == pygame.K_RETURN:
                        cost = add_node_g(src.gui.constants.user_text_add_node)
                        src.gui.constants.user_text_add_node = str(cost)
                        timeout = Timer(2.0, reset_add_node_string)
                        timeout.start()
                        active_add_node = False
                        pygame.display.flip()
                    else:
                        src.gui.constants.user_text_add_node += event.unicode

                if active_remove_node == True:
                    if event.key == pygame.K_BACKSPACE:
                        src.gui.constants.user_text_remove_node = src.gui.constants.user_text_remove_node[:-1]
                    elif event.key == pygame.K_RETURN:
                        cost = remove_node_g(src.gui.constants.user_text_remove_node)
                        src.gui.constants.user_text_remove_node = str(cost)
                        timeout = Timer(2.0, reset_remove_node_string)
                        timeout.start()
                        active_remove_node = False
                        pygame.display.flip()
                    else:
                        src.gui.constants.user_text_remove_node += event.unicode



            elif event.type == pygame.MOUSEBUTTONDOWN:
                if center_button.isOver(pygame.mouse.get_pos()):
                    center_ga()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_tsp.collidepoint(event.pos):
                        active_tsp = True
                        src.gui.constants.user_text_tsp = ''
                    else:
                        active_tsp = False
                        src.gui.constants.user_text_tsp = 'tsp'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_shortest.collidepoint(event.pos):
                        active_shortest = True
                        src.gui.constants.user_text_shortest = ''
                    else:
                        active_shortest = False
                        src.gui.constants.user_text_shortest = 'shortest'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_add_node.collidepoint(event.pos):
                        active_add_node = True
                        src.gui.constants.user_text_add_node = ''
                    else:
                        active_add_node = False
                        src.gui.constants.user_text_add_node = 'add node'
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect_remove_node.collidepoint(event.pos):
                        active_remove_node = True
                        src.gui.constants.user_text_remove_node = ''
                    else:
                        active_remove_node = False
                        src.gui.constants.user_text_remove_node = 'remove node'


        window.fill(white)

        for edge in range(len(src.gui.constants.src_edge_list)):
            pygame.draw.line(window, black, src.gui.constants.src_edge_list[edge],
                             src.gui.constants.dest_edge_list[edge])
            pygame.draw.polygon(window, [46, 139, 87], src.gui.constants.arrow_head_list[edge])

        for nodeV in src.gui.constants.node_list:
            pygame.draw.circle(window, black, [nodeV[0], nodeV[1]], 10)
            textsurface = myfont.render(f"{nodeV[2]}", True, white)
            window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))

            if src.gui.constants.center_node == nodeV[2]:
                pygame.draw.circle(window, (26, 10, 166), [nodeV[0], nodeV[1]], 15)
                textsurface = myfont.render(f"{nodeV[2]}", True, white)
                window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))
                timeout = Timer(5.0, reset_center)
                timeout.start()

            if src.gui.constants.tsp_list is not None:
                if nodeV[2] in src.gui.constants.tsp_list:
                    pygame.draw.circle(window, (140, 64, 6), [nodeV[0], nodeV[1]], 10)
                    textsurface = myfont.render(f"{nodeV[2]}", True, white)
                    window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))
                    timeout2 = Timer(5.0, reset_tsp)
                    timeout2.start()

            if src.gui.constants.shortest_list is not None:
                if nodeV[2] in src.gui.constants.shortest_list:
                    pygame.draw.circle(window, (140, 64, 6), [nodeV[0], nodeV[1]], 10)
                    textsurface = myfont.render(f"{nodeV[2]}", True, white)
                    window.blit(textsurface, (nodeV[0] - 7, nodeV[1] - 5))
                    timeout2 = Timer(5.0, reset_shortest)
                    timeout2.start()

        if active_tsp:
            color_tsp = color_active_tsp
        else:
            color_tsp = color_passive_tsp
        pygame.draw.rect(window, color_tsp, input_rect_tsp, 2)
        text_surface = base_font_tsp.render(src.gui.constants.user_text_tsp, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_tsp.x + 5, input_rect_tsp.y + 5))
        input_rect_tsp.w = max(text_surface.get_width() + 10, 73)

        if active_shortest:
            color_shortest = color_active_shortest
        else:
            color_shortest = color_passive_shortest
        pygame.draw.rect(window, color_shortest, input_rect_shortest, 2)
        text_surface = base_font_shortest.render(src.gui.constants.user_text_shortest, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_shortest.x + 5, input_rect_shortest.y + 5))
        input_rect_shortest.w = max(text_surface.get_width() + 10, 73)

        if active_add_node:
            color_add_node = color_active_add_node
        else:
            color_add_node = color_passive_add_node
        pygame.draw.rect(window, color_add_node, input_rect_add_node, 2)
        text_surface = base_font_add_node.render(src.gui.constants.user_text_add_node, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_add_node.x + 5, input_rect_add_node.y + 5))
        input_rect_add_node.w = max(text_surface.get_width() + 10, 73)

        if active_remove_node:
            color_remove_node = color_active_remove_node
        else:
            color_remove_node = color_passive_remove_node
        pygame.draw.rect(window, color_remove_node, input_rect_remove_node, 2)
        text_surface = base_font_remove_node.render(src.gui.constants.user_text_remove_node, True, (0, 0, 128))
        window.blit(text_surface, (input_rect_remove_node.x + 5, input_rect_remove_node.y + 5))
        input_rect_remove_node.w = max(text_surface.get_width() + 10, 73)

        center_button.draw(window)
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    GUI("./data/A2.json")
