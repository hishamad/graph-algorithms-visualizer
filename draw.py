import time
from config import *
from components.button import *
import math

# Buttons
CB_WIDTH = 0.08 * WIDTH
CB_HEIGHT = 0.05 * HEIGHT

back_button = Button(pygame.Rect(0.01*WIDTH, 0.93 * HEIGHT, CB_WIDTH, CB_HEIGHT), GREEN, '< Back')
reset_graph_button = Button(pygame.Rect(0.5 * WIDTH + (2.5 * CB_WIDTH) - CB_WIDTH, 0.93 * HEIGHT, CB_WIDTH, CB_HEIGHT),
                            GREEN, 'Reset ↺')
start_button = Button(pygame.Rect(0.5 * WIDTH - 2.5 * CB_WIDTH, 0.93 * HEIGHT, CB_WIDTH, CB_HEIGHT), GREEN, 'Start')
pause_button = Button(pygame.Rect(0.5 * WIDTH - 0.5 * CB_WIDTH, 0.93 * HEIGHT, CB_WIDTH, CB_HEIGHT), RED, 'Pause')

control_buttons = [start_button, pause_button, reset_graph_button, back_button]

MB_WIDTH = 0.2 * WIDTH
MB_HEIGHT = 0.1 * HEIGHT
bfs_button = Button(pygame.Rect(0.5 * WIDTH - 0.5 * MB_WIDTH, 0.25 * HEIGHT, MB_WIDTH, MB_HEIGHT), GREEN,
                    'Breadth-First Search')
dfs_button = Button(pygame.Rect(0.5 * WIDTH - 0.5 * MB_WIDTH, 0.25 * HEIGHT + 1.5 * MB_HEIGHT, MB_WIDTH, MB_HEIGHT),
                    GREEN, 'Depth-First Search')
dij_button = Button(pygame.Rect(0.5 * WIDTH - 0.5 * MB_WIDTH, 0.25 * HEIGHT + 3 * MB_HEIGHT, MB_WIDTH, MB_HEIGHT),
                    GREEN, "Dijkstra’s algorithm")
prim_button = Button(pygame.Rect(0.5 * WIDTH - 0.5 * MB_WIDTH, 0.25 * HEIGHT + 4.5 * MB_HEIGHT, MB_WIDTH, MB_HEIGHT),
                    GREEN, "Prim’s algorithm")
menu_buttons = [bfs_button, dfs_button, dij_button, prim_button]


def draw_graph(graph):
    # Append the already processed edge so you print it once
    already = [[False for i in range(len(graph.nodes))] for j in range(len(graph.nodes))]
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
