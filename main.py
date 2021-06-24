from config import *
from components.graph import *
from algorithms.bfs import *
from algorithms.dfs import *
from algorithms.dij import *
from algorithms.prim import *
from draw import *


menu_visible, is_dfs, is_bfs, is_dij, is_prim = True, False, False, False, False

graph = Graph(adjacency_list)
weighted_graph = Graph(adjacency_matrix, True)


def main():
    global menu_visible, is_dfs, is_bfs, is_dij, is_prim, graph, weighted_graph

    while True:
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


def choose_node(gh):
    node = -1
    while node == -1:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for i, node in enumerate(gh.nodes):
                        if node.on_top(pygame.mouse.get_pos()):
                            node = i
                            break

    return node


def handle_menu_buttons(pos):
    global menu_visible, is_bfs, is_dfs, is_dij, is_prim
    for i, btn in enumerate(menu_buttons):
        if btn.on_top(pos):
            menu_visible = False
            if i == 0:
                is_bfs = True
                draw_bfs_guide()
            elif i == 1:
                is_dfs = True
            elif i == 2:
                is_dij = True
            elif i == 3:
                is_prim = True


def handle_reset(reset, back):
    global graph
    if reset:
        graph = Graph(adjacency_list)
    elif back:
        handle_back_button()


def handle_weighted_reset(reset, back):
    global weighted_graph
    if reset:
        weighted_graph = Graph(adjacency_matrix, True)
    elif back:
        handle_back_button()


def handle_control_buttons(pos):
    global weighted_graph, graph, is_bfs, is_dfs, is_dij, is_prim
    if reset_graph_button.on_top(pos):
        graph = Graph(adjacency_list)
        weighted_graph = Graph(adjacency_matrix, True)
    elif back_button.on_top(pos):
        handle_back_button()
    elif start_button.on_top(pos) and is_bfs:
        graph = Graph(adjacency_list)
        draw(graph)
        start = choose_node(graph)
        graph.nodes[start].start_end()
        draw(graph)
        end = choose_node(graph)
        graph.nodes[end].start_end()
        draw(graph)
        reset, back = bfs(graph, start, end)
        handle_reset(reset, back)
    elif start_button.on_top(pos) and is_dfs:
        graph = Graph(adjacency_list)
        reset, back = dfs(graph)
        handle_reset(reset, back)
    elif start_button.on_top(pos) and is_dij:
        weighted_graph = Graph(adjacency_matrix, True)
        draw(weighted_graph)
        start = choose_node(weighted_graph)
        weighted_graph.nodes[start].start_end()
        draw(weighted_graph)
        end = choose_node(weighted_graph)
        weighted_graph.nodes[end].start_end()
        draw(weighted_graph)
        reset, back = dij(weighted_graph, start, end)

        handle_weighted_reset(reset, back)
    elif start_button.on_top(pos) and is_prim:
        weighted_graph = Graph(adjacency_matrix, True)
        reset, back = prim(weighted_graph)
        handle_weighted_reset(reset, back)


main()
