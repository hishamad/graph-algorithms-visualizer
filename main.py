import sys
from config import *
from components.graph import *
from algorithms.bfs import *
from algorithms.dfs import *
from algorithms.dij import *

from draw import *


menu_visible, is_dfs, is_bfs, is_dij, is_prim = True, False, False, False, False


adjacency_list = [[1, 3, 4], [0, 4], [4], [0, 4], [0, 1, 2, 3, 5, 6],
                  [4, 7, 8], [4, 9, 10], [5, 8, 11], [5, 7], [6], [6], [7]]

adjacency_matrix = [[0, 5, 0, 4, 9, 0, 0, 0, 0, 0, 0, 0],
                    [5, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
                    [4, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
                    [9, 7, 6, 3, 0, 7, 9, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 7, 0, 0, 8, 2, 0, 0, 0],
                    [0, 0, 0, 0, 9, 0, 0, 0, 0, 5, 7, 0],
                    [0, 0, 0, 0, 0, 8, 0, 0, 4, 0, 0, 8],
                    [0, 0, 0, 0, 0, 2, 0, 4, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0]]

graph = Graph(adjacency_list)
weighted_graph = Graph(adjacency_matrix, True)


def main():
    global menu_visible, is_dfs, is_bfs, is_dij, is_prim, adjacency_list, graph, weighted_graph, adjacency_matrix

    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if reset_graph_button.on_top(pos):
                        graph = Graph(adjacency_list)
                        weighted_graph = Graph(adjacency_matrix, True)
                    elif back_button.on_top(pos):
                        handle_back_button()
                    elif start_button.on_top(pos) and is_bfs:
                        graph = Graph(adjacency_list)
                        reset, back = bfs(graph)
                        if reset:
                            graph = Graph(adjacency_list)
                        elif back:
                            handle_back_button()
                    elif start_button.on_top(pos) and is_dfs:
                        graph = Graph(adjacency_list)
                        reset, back = dfs(graph)
                        if reset:
                            graph = Graph(adjacency_list)
                        elif back:
                            handle_back_button()
                    elif start_button.on_top(pos) and is_dij:
                        weighted_graph = Graph(adjacency_matrix, True)
                        reset, back = dij(weighted_graph)
                        if reset:
                            weighted_graph = Graph(adjacency_matrix, True)
                        elif back:
                            handle_back_button()
                    elif start_button.on_top(pos) and is_prim:
                        weighted_graph = Graph(adjacency_matrix, True)
                        reset, back = dij(weighted_graph)
                        if reset:
                            weighted_graph = Graph(adjacency_matrix, True)
                        elif back:
                            handle_back_button()
                    elif bfs_button.on_top(pos):
                        menu_visible = False
                        is_bfs = True
                    elif dfs_button.on_top(pos):
                        menu_visible = False
                        is_dfs = True
                    elif dij_button.on_top(pos):
                        menu_visible = False
                        is_dij = True
                    elif prim_button.on_top(pos):
                        menu_visible = False
                        is_prim = True
        control_buttons[0].hover_effect(control_buttons)
        menu_buttons[0].hover_effect(menu_buttons)

        if menu_visible:
            draw_menu()
        elif is_dij or is_prim:
            draw(weighted_graph)
        else:
            draw(graph)


def handle_back_button():
    global menu_visible, is_dfs, is_bfs, is_dij, is_prim, adjacency_list, graph, adjacency_matrix, weighted_graph
    menu_visible = True
    graph = Graph(adjacency_list)
    weighted_graph = Graph(adjacency_matrix, True)
    is_dfs, is_bfs, is_dij, is_prim = False, False, False, False


main()
