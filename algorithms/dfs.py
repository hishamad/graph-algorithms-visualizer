from utils import *

reset, back, speed = False, False, 200


def update_and_handle_events(graph, up_graph=True):
    global reset, back, speed
    reset, back = update(graph, speed, up_graph)
    if reset or back:
        raise Error


def dfs(graph):
    global reset, back
    visited = [False] * len(graph.nodes)
    s = 0
    stack = [s]

    while stack:
        try:
            u = stack[-1]
            stack.pop()
            graph.nodes[u].done()
            if not visited[u]:
                visited[u] = True
                update_and_handle_events(graph)

            for v in graph.adjacency_list[u]:
                if not visited[v]:
                    graph.edges[u][v].undirected_visit(graph.edges[v][u])
                    graph.nodes[v].visit()
                    update_and_handle_events(graph)
                    graph.edges[u][v].undirected_done(graph.edges[v][u])
                    update_and_handle_events(graph)
                    stack.append(v)

        except Error:
            break

    return reset, back
