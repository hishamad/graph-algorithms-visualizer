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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for neighbour in adjacency_list[u]:
            if not nodes[neighbour].visited:
                q.append(neighbour)
                nodes[neighbour].visit()
                prev[neighbour] = u
                edges[u][neighbour].visit()
                edges[neighbour][u].visit()

        update(draw)

        for neighbour in adjacency_list[u]:
            if nodes[neighbour].visited:
                edges[u][neighbour].done()
                edges[neighbour][u].done()

        nodes[u].done()
        update(draw)

    e = 11
    curr = e
    while prev[curr]:
        nodes[curr].visit()
        nodes[prev[curr]].visit()
        edges[curr][prev[curr]].visit()
        edges[prev[curr]][curr].visit()
        curr = prev[curr]

        update(draw)
    edges[curr][s].visit()
    edges[s][curr].visit()
    nodes[s].visit()
    update(draw)


def update(draw):
    draw()
    time.sleep(0.75)
