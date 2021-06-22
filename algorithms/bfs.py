from utils import *

reset, back, speed = False, False, 400


def update_and_handle_events(graph, up_graph=True):
    global reset, back, speed
    reset, back = update(graph, speed, up_graph)
    if reset or back:
        raise Error


def bfs(graph):
    global reset, back
    s = 0
    q = [s]
    graph.nodes[s].visit()
    prev = [None] * len(graph.nodes)
    while q:
        try:
            u = q.pop(0)
            graph.nodes[u].current()
            update_and_handle_events(graph)

            for neighbour in graph.graph_rep[u]:
                if not graph.nodes[neighbour].visited:
                    q.append(neighbour)
                    graph.nodes[neighbour].visit()
                    prev[neighbour] = u
                    graph.edges[u][neighbour].undirected_visit(graph.edges[neighbour][u])
                    update_and_handle_events(graph)

            for neighbour in graph.graph_rep[u]:
                if graph.nodes[neighbour].visited:
                    graph.edges[u][neighbour].undirected_done(graph.edges[neighbour][u])

            graph.nodes[u].done()
            update_and_handle_events(graph)

        except Error:
            break

    if reset or back:
        return reset, back
    reconstruct_path(s, prev, graph)
    return reset, back


def reconstruct_path(s, prev, graph):
    e = 11
    curr = e
    while prev[curr]:
        try:
            graph.nodes[curr].shortest_path()
            graph.nodes[prev[curr]].shortest_path()
            graph.edges[curr][prev[curr]].undirected_shortest_path(graph.edges[prev[curr]][curr])
            curr = prev[curr]
            update_and_handle_events(graph)
        except Error:
            return

    try:
        graph.edges[curr][s].undirected_shortest_path(graph.edges[s][curr])
        graph.nodes[s].shortest_path()
        update_and_handle_events(graph)
    except Error:
        return
