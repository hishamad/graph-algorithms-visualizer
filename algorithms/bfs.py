from config import *
from utils import *


def bfs(draw, adjacency_list, nodes, edges, control_buttons):
    cont = True
    s = 0
    q = [s]
    nodes[s].visit()
    prev = [None] * len(nodes)
    while q and cont:
        for event in pygame.event.get():
            cont = handle_control_menu(event, control_buttons, draw)
            if not cont:
                return
        u = q.pop(0)
        nodes[u].current()
        update(draw)

        for neighbour in adjacency_list[u]:
            for event in pygame.event.get():
                cont = handle_control_menu(event, control_buttons, draw)
                if not cont:
                    return
            if not nodes[neighbour].visited:
                q.append(neighbour)
                nodes[neighbour].visit()
                prev[neighbour] = u
                edges[u][neighbour].undirected_visit(edges[neighbour][u])

        update(draw)

        for neighbour in adjacency_list[u]:
            for event in pygame.event.get():
                cont = handle_control_menu(event, control_buttons, draw)
                if not cont:
                    return
            if nodes[neighbour].visited:
                edges[u][neighbour].undirected_done(edges[neighbour][u])

        nodes[u].done()
        update(draw)
    if not cont:
        return
    reconstruct_path(draw, s, prev, nodes, edges, control_buttons)


def reconstruct_path(draw, s, prev, nodes, edges, control_buttons):
    e = 11
    curr = e
    while prev[curr]:
        for event in pygame.event.get():
            cont = handle_control_menu(event, control_buttons, draw)
        nodes[curr].shortest_path()
        nodes[prev[curr]].shortest_path()
        edges[curr][prev[curr]].undirected_shortest_path(edges[prev[curr]][curr])
        curr = prev[curr]
        update(draw)

    edges[curr][s].undirected_shortest_path(edges[s][curr])
    nodes[s].shortest_path()
    update(draw)



