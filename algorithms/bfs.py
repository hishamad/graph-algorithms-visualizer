from utils import *

reset, back, speed = False, False, 300


def update_and_handle_events(graph, up_graph=True):
    global reset, back, speed
    reset, back = update(graph, speed, up_graph)
    if reset or back:
        raise Error


def bfs(graph, start=0, end=11):
    global reset, back
    q = [start]

    visited = [False] * len(graph.nodes)
    visited[start] = True
    prev = [None] * len(graph.nodes)

    while q:
        try:
            u = q.pop(0)
            if u == end:
                break

            if u != end and u != start:
                graph.nodes[u].current()
            update_and_handle_events(graph)

            for neighbour in graph.graph_rep[u]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    if neighbour != end and neighbour != start:
                        graph.nodes[neighbour].visit()
                    visited[neighbour] = True
                    prev[neighbour] = u
                    graph.edges[u][neighbour].undirected_visit(graph.edges[neighbour][u])
            update_and_handle_events(graph)

            for neighbour in graph.graph_rep[u]:
                if visited[neighbour]:
                    graph.edges[u][neighbour].undirected_done(graph.edges[neighbour][u])

            if u != end and u != start:
                graph.nodes[u].done()

            update_and_handle_events(graph)

        except Error:
            break

    if reset or back:
        return reset, back
    reconstruct_path(start, end, prev, graph)
    return reset, back


def reconstruct_path(s, e, prev, graph):
    curr = e
    while prev[curr]:
        try:
            if prev[curr] == s:
                break
            if curr != e and curr != s:
                graph.nodes[curr].shortest_path()
                graph.nodes[prev[curr]].shortest_path()
            graph.edges[curr][prev[curr]].undirected_shortest_path(graph.edges[prev[curr]][curr])
            curr = prev[curr]
            update_and_handle_events(graph)
        except Error:
            return

    try:
        graph.edges[curr][s].undirected_shortest_path(graph.edges[s][curr])
        update_and_handle_events(graph)
    except Error:
        return
