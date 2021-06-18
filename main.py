from config import *
from components.button import *
from components.graph import *

# Buttons
reset_graph_button = Button(50, 900, 310, 70, ORANGE, 'Reset ↺')
bfs_button = Button(400, 900, 310, 70, ORANGE, 'Breadth-First Search')
buttons = [reset_graph_button, bfs_button]


def draw_graph(nodes, edges):
    for edge in edges:
        for k, v in edge.items():
            v.display()

    for i, node in enumerate(nodes):
        node.display()
        num = FONT.render(f'{i}', True, WHITE)
        if i < 10:
            WINDOW.blit(num, (node.x - 8, node.y - 15))
        else:
            WINDOW.blit(num, (node.x - 18, node.y - 15))


def draw_menu():
    WINDOW.fill(GREY)
    pygame.draw.rect(WINDOW, DARK_BLUE, MENU)
    pygame.draw.rect(WINDOW, WHITE, MENU_BORDER)


def update(draw):
    draw()
    time.sleep(0.75)


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

def draw(buttons, nodes, edges):
    # 1) Draw menu
    draw_menu()

    # 2) Adding the buttons
    for btn in buttons:
        btn.display()

    # Drawing the edges
    draw_graph(nodes, edges)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    adjacency_list = [[1, 3, 4], [0, 4], [4], [0, 4], [0, 1, 2, 3, 5, 6], [4, 7, 8], [4, 9, 10], [5, 8, 11], [5, 7], [6], [6], [7]]


    nodes, edges = construct_graph(adjacency_list)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if reset_graph_button.is_over(pos):
                        nodes, edges = construct_graph(adjacency_list)

                    elif bfs_button.is_over(pos):
                        bfs(lambda: draw(buttons, nodes, edges), adjacency_list, nodes, edges)

            if reset_graph_button.is_over(pos):
                reset_graph_button.colour = GREY
            elif bfs_button.is_over(pos):
                bfs_button.colour = GREY
            else:
                reset_graph_button.colour = GREEN
                bfs_button.colour = GREEN


        draw(buttons, nodes, edges)


main()
