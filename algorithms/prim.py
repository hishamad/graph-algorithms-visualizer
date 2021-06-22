from utils import *

MAXINT = 2147483648

reset, back, speed = False, False, 150


def update_and_handle_events(graph, up_graph=True):
    global reset, back, speed
    reset, back = update(graph, speed, up_graph)
    if reset or back:
        raise Error


def prim(graph):
    global reset, back
    n = len(graph.graph_rep)
    weights = [MAXINT] * n
    weights[0] = 0
    prev = [None] * n
    in_mst = [False] * n

    prev[0] = -1

    for i in range(n):
        try:

            mini = MAXINT
            for j in range(n):
                if weights[j] < mini and not in_mst[j]:
                    mini = weights[j]
                    u = j

            in_mst[u] = True
            graph.nodes[u].done()
            update_and_handle_events(graph)

            for v in range(n):
                if 0 < graph.graph_rep[u][v] < weights[v] and not in_mst[v]:
                    weights[v] = graph.graph_rep[u][v]
                    prev[v] = u
                    graph.nodes[v].visit()
                    graph.edges[u][v].undirected_visit(graph.edges[v][u])
                    update_and_handle_events(graph)
                    graph.edges[u][v].undirected_done(graph.edges[v][u])
                    update_and_handle_events(graph)

        except Error:
            break

    if reset or back:
        return reset, back

    for i in range(1, n):
        try:
            graph.nodes[prev[i]].shortest_path()
            graph.edges[prev[i]][i].undirected_shortest_path(graph.edges[i][prev[i]])
            update_and_handle_events(graph)
            graph.nodes[i].shortest_path()
            update_and_handle_events(graph)
        except Error:
            break

    return reset, back
