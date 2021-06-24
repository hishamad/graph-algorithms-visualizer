from utils import *

reset, back, speed = False, False, 200


def update_and_handle_events(graph, up_graph=True):
    global reset, back, speed
    reset, back = update(graph, speed, up_graph)
    if reset or back:
        raise Error


def dfs(graph, end=11):
    global reset, back
    visited = [False] * len(graph.nodes)
    s = 0
    stack = [s]

    graph.nodes[s].start_end()
    graph.nodes[end].start_end()

    while stack:
        try:
            u = stack[-1]
            stack.pop()
            if u != end and u != s:
                graph.nodes[u].current()
            update_and_handle_events(graph)
            if not visited[u]:
                visited[u] = True
                if u != end and u != s:
                    graph.nodes[u].visit()
                update_and_handle_events(graph)

            for v in graph.graph_rep[u]:
                if not visited[v]:
                    if v != end and v != s:
                        graph.nodes[v].visit()
                    graph.edges[u][v].undirected_visit(graph.edges[v][u])
                    update_and_handle_events(graph)
                    graph.edges[u][v].undirected_done(graph.edges[v][u])
                    update_and_handle_events(graph)
                    stack.append(v)
            if u != end and u != s:
                graph.nodes[u].done()
            update_and_handle_events(graph)
        except Error:
            break

    return reset, back
