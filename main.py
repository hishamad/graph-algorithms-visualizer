import sys
from config import *
from components.graph import *
from algorithms.bfs import *
from algorithms.dfs import *
from draw import *


menu_visible, is_dfs, is_bfs = True, False, False


adjacency_list = [[1, 3, 4], [0, 4], [4], [0, 4], [0, 1, 2, 3, 5, 6], [4, 7, 8], [4, 9, 10], [5, 8, 11], [5, 7],
                      [6], [6], [7]]

graph = Graph(adjacency_list)
weighted_graph = Graph(adjacency_list, True)


def main():
    global menu_visible, is_dfs, is_bfs, adjacency_list, graph

    menu_visible = True
    is_bfs, is_dfs = False, False
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
                    elif bfs_button.on_top(pos):
                        menu_visible = False
                        is_bfs = True
                    elif dfs_button.on_top(pos):
                        menu_visible = False
                        is_dfs = True

        control_buttons[0].hover_effect(control_buttons)
        menu_buttons[0].hover_effect(menu_buttons)

        if menu_visible:
            draw_menu()
        else:
            draw(graph)


def handle_back_button():
    global menu_visible, is_dfs, is_bfs, adjacency_list, graph
    menu_visible = True
    graph = Graph(adjacency_list)
    is_dfs = False
    is_bfs = False


main()
