import math
from buttons import *


def draw_graph(graph):
    # Append the already processed edge so you print it once
    already = [[False for _ in range(len(graph.nodes))] for _ in range(len(graph.nodes))]
    for i, edges in enumerate(graph.edges):
        for k, edge in edges.items():
            edge.display()
            if graph.weighted and not already[i][k]:
                weight = FONT.render(f'{edge.weight}', True, WHITE)
                x = edge.start[0] + (edge.end[0] - edge.start[0]) / 2
                y = edge.start[1] + (edge.end[1] - edge.start[1]) / 2
                if edge.end[0] - edge.start[0] == 0:
                    weight = pygame.transform.rotozoom(weight, -90, 1)
                    WINDOW.blit(weight, (x, y))
                else:
                    angle = math.degrees(math.atan((edge.end[1] - edge.start[1])/(edge.end[0] - edge.start[0])))
                    weight = pygame.transform.rotozoom(weight, -angle, 1)
                    if edge.end[1] - edge.start[1] <= 0:
                        WINDOW.blit(weight, (x - weight.get_width(), y - weight.get_height()))
                    else:
                        WINDOW.blit(weight, (x, y - weight.get_height()))
                already[i][k] = True
                already[k][i] = True

    for i, node in enumerate(graph.nodes):
        node.display()
        if i == 0:
            num = FONT.render('S', True, WHITE)
        elif i == len(graph.nodes) - 1:
            num = FONT.render('E', True, WHITE)
        else:
            num = FONT.render(f'{i}', True, WHITE)
        WINDOW.blit(num, (node.x - num.get_width() / 2, node.y - num.get_height() / 2))


def draw_menu():
    WINDOW.fill(LIGHT_GREY)
    for btn in menu_buttons:
        btn.display()
    pygame.display.update()


def draw(graph):
    # 1) Draw menu
    WINDOW.fill(GREY)
    pygame.draw.rect(WINDOW, DARK_BLUE, CONTROL_MENU)

    # 2) Adding the control_buttons0
    for btn in control_buttons:
        btn.display()

    # Drawing the edges
    draw_graph(graph)

    pygame.display.update()
