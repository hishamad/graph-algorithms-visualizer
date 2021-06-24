from utils import *

reset, back, speed = False, False, 200


def update_and_handle_events(graph, up_graph=True):
    global reset, back, speed
    reset, back = update(graph, speed, up_graph)
    if reset or back:
        raise Error


def dfs(graph, start=0, end=11):
    global reset, back
    visited = [False] * len(graph.nodes)

    stack = [start]

    while stack:
        try:
            u = stack[-1]

            stack.pop()
            if u != end and u != start:
                graph.nodes[u].current()
            update_and_handle_events(graph)
            if not visited[u]:
                visited[u] = True
                if u != end and u != start:
                    graph.nodes[u].visit()
                update_and_handle_events(graph)

            for v in graph.graph_rep[u]:
                if not visited[v]:
                    if v != end and v != start:
                        graph.nodes[v].visit()
                    graph.edges[u][v].undirected_visit(graph.edges[v][u])
                    update_and_handle_events(graph)
                    graph.edges[u][v].undirected_done(graph.edges[v][u])
                    update_and_handle_events(graph)
                    stack.append(v)
            if u != end and u != start:
                graph.nodes[u].done()
            update_and_handle_events(graph)

            if u == end:
                break
        except Error:
            break

    return reset, back
