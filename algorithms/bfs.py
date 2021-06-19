from config import *


def bfs(draw, adjacency_list, nodes, edges):
    s = 0
    q = [s]
    nodes[s].visit()
    prev = [None] * len(nodes)

    while q:
        u = q.pop(0)
        nodes[u].current()
        update(draw)

        # Make it possible to exit the game even when the algorithm is still running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for neighbour in adjacency_list[u]:
            if not nodes[neighbour].visited:
                q.append(neighbour)
                nodes[neighbour].visit()
                prev[neighbour] = u
                edges[u][neighbour].undirected_visit(edges[neighbour][u])

        update(draw)

        for neighbour in adjacency_list[u]:
            if nodes[neighbour].visited:
                edges[u][neighbour].undirected_done(edges[neighbour][u])

        nodes[u].done()
        update(draw)

    reconstruct_path(draw, s, prev, nodes, edges)


def reconstruct_path(draw, s, prev, nodes, edges):
    e = 11
    curr = e
    while prev[curr]:
        nodes[curr].visit()
        nodes[prev[curr]].visit()
        edges[curr][prev[curr]].undirected_visit(edges[prev[curr]][curr])
        curr = prev[curr]
        update(draw)

    edges[curr][s].undirected_visit(edges[s][curr])
    nodes[s].visit()
    update(draw)


def update(draw):
    draw()
    time.sleep(0.75)
