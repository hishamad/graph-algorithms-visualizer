import time

from config import *
from components.button import *

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
        if i == 0:
            num = FONT.render(f'S', True, WHITE)
        elif i == len(nodes) - 1:
            num = FONT.render(f'E', True, WHITE)
        else:
            num = FONT.render(f'{i}', True, WHITE)
        if i < 10 or i == len(nodes) - 1:
            WINDOW.blit(num, (node.x - 8, node.y - 20))
        else:
            WINDOW.blit(num, (node.x - 18, node.y - 20))


def draw_menu(VISIBLE):
    WINDOW.fill(GREY)
    pygame.display.update()


def draw(buttons, nodes, edges):
    # 1) Draw menu
    WINDOW.fill(GREY)
    pygame.draw.rect(WINDOW, DARK_BLUE, CONTROL_MENU)

    # 2) Adding the buttons
    for btn in buttons:
        btn.display()

    # Drawing the edges
    draw_graph(nodes, edges)

    pygame.display.update()
