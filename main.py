from config import *
from components.graph import *
from algorithms.bfs import *
from algorithms.dfs import *
from algorithms.dij import *
from algorithms.prim import *
from draw import *
from handle import *

menu_visible, is_dfs, is_bfs, is_dij, is_prim = True, False, False, False, False

graph = Graph(adjacency_list)
weighted_graph = Graph(adjacency_matrix, True)


def main():
    global menu_visible, is_dfs, is_bfs, is_dij, is_prim, graph, weighted_graph
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    handle_control_buttons(pos)
                    handle_menu_buttons(pos)

        control_buttons[0].hover_effect(control_buttons)
        menu_buttons[0].hover_effect(menu_buttons)

        if menu_visible:
            draw_menu()
        elif is_dij or is_prim:
            draw(weighted_graph)
        else:
            draw(graph)


def handle_back_button():
    global menu_visible, is_dfs, is_bfs, is_dij, is_prim, graph, weighted_graph
    menu_visible = True
    graph = Graph(adjacency_list)
    weighted_graph = Graph(adjacency_matrix, True)
    is_dfs, is_bfs, is_dij, is_prim = False, False, False, False


def handle_reset(gr, reset, back):
    if reset and gr.weighted:
        gr = Graph(adjacency_matrix, True)
    elif reset:
        gr = Graph(adjacency_list)
    elif back:
        handle_back_button()
    return gr


def handle_menu_buttons(pos):
    global menu_visible, is_bfs, is_dfs, is_dij, is_prim
    for i, btn in enumerate(menu_buttons):
        if btn.on_top(pos):
            menu_visible = False
            if i == 0:
                is_bfs = True
            elif i == 1:
                is_dfs = True
            elif i == 2:
                is_dij = True
            elif i == 3:
                is_prim = True


def handle_control_buttons(pos):
    global weighted_graph, graph, is_bfs, is_dfs, is_dij, is_prim
    if reset_graph_button.on_top(pos):
        graph = Graph(adjacency_list)
        weighted_graph = Graph(adjacency_matrix, True)
    elif back_button.on_top(pos):
        handle_back_button()
    elif start_button.on_top(pos) and is_bfs:
        graph = Graph(adjacency_list)
        start, end = handle_start_end_node(graph)
        reset, back = bfs(graph, start, end)
        graph = handle_reset(graph, reset, back)
    elif start_button.on_top(pos) and is_dfs:
        graph = Graph(adjacency_list)
        start, end = handle_start_end_node(graph)
        reset, back = dfs(graph, start, end)
        graph = handle_reset(graph, reset, back)
    elif start_button.on_top(pos) and is_dij:
        weighted_graph = Graph(adjacency_matrix, True)
        start, end = handle_start_end_node(weighted_graph)
        reset, back = dij(weighted_graph, start, end)
        weighted_graph = handle_reset(weighted_graph, reset, back)
    elif start_button.on_top(pos) and is_prim:
        weighted_graph = Graph(adjacency_matrix, True)
        reset, back = prim(weighted_graph)
        weighted_graph = handle_reset(weighted_graph, reset, back)

main()