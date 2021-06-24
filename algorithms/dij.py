from utils import *

MAXINT = 2147483648

reset, back, speed = False, False, 150


def update_and_handle_events(graph, up_graph=True):
    global reset, back, speed
    reset, back = update(graph, speed, up_graph)
    if reset or back:
        raise Error


def dij(graph, start=0, end=11):
    global reset, back
    n = len(graph.graph_rep)
    calc_dist = [MAXINT] * n
    calc_dist[start] = 0
    parent = [-1] * n
    q = list(range(n))

    while q:
        try:
            mini = MAXINT
            for j in range(start, n):
                if calc_dist[j] < mini and j in q:
                    mini = calc_dist[j]
                    u = j

            if u == end:
                break
            q.remove(u)
            if u != end and u != start:
                graph.nodes[u].done()
                update_and_handle_events(graph)

            for v in range(start, n):
                if graph.graph_rep[u][v] and v in q:
                    if v != start and v != end:
                        graph.nodes[v].visit()
                        graph.edges[u][v].undirected_visit(graph.edges[v][u])
                        update_and_handle_events(graph)
                    if calc_dist[u] + graph.graph_rep[u][v] < calc_dist[v]:
                        calc_dist[v] = calc_dist[u] + graph.graph_rep[u][v]
                        parent[v] = u
                    graph.edges[u][v].undirected_done(graph.edges[v][u])
                    update_and_handle_events(graph)
        except Error:
            break
    if reset or back:
        return reset, back
    e = end
    while parent[e]:
        try:
            if parent[e] == start:
                break
            if e != start and e != end:
                graph.nodes[e].shortest_path()
                graph.nodes[parent[e]].shortest_path()
            graph.edges[e][parent[e]].undirected_shortest_path(graph.edges[parent[e]][e])
            update_and_handle_events(graph)
            e = parent[e]
        except Error:
            break
    if not reset and not back:
        graph.edges[e][start].undirected_shortest_path(graph.edges[start][e])
        update_and_handle_events(graph)

    return reset, back
