import pygame.time

from components.graph import *
from algorithms.bfs import *
from draw import *


def main():
    adjacency_list = [[1, 3, 4], [0, 4], [4], [0, 4], [0, 1, 2, 3, 5, 6], [4, 7, 8], [4, 9, 10], [5, 8, 11], [5, 7],
                      [6], [6], [7]]

    nodes, edges = construct_graph(adjacency_list)
    menu_visible = True
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if reset_graph_button.on_top(pos):
                        nodes, edges = construct_graph(adjacency_list)
                    elif start_button.on_top(pos):
                        nodes, edges = construct_graph(adjacency_list)
                        time.sleep(1)
                        bfs(lambda: draw(control_buttons, nodes, edges), adjacency_list, nodes, edges, control_buttons)
                        nodes, edges = construct_graph(adjacency_list)
                    elif bfs_button.on_top(pos):
                        menu_visible = False
            control_buttons[0].hover_effect(control_buttons)
            menu_buttons[0].hover_effect(menu_buttons)
        if menu_visible:
            draw_menu()
        else:
            draw(control_buttons, nodes, edges)


main()
