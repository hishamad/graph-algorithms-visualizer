import time
from config import *
from components.button import *

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

menu_buttons = [bfs_button, dfs_button]


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
        WINDOW.blit(num, (node.x - num.get_width() / 2, node.y - num.get_height() / 2))


def draw_menu():
    WINDOW.fill(LIGHT_GREY)
    for btn in menu_buttons:
        btn.display()
    pygame.display.update()


def draw(control_buttons, nodes, edges):
    # 1) Draw menu
    WINDOW.fill(GREY)
    pygame.draw.rect(WINDOW, DARK_BLUE, CONTROL_MENU)

    # 2) Adding the control_buttons0
    for btn in control_buttons:
        btn.display()

    # Drawing the edges
    draw_graph(nodes, edges)

    pygame.display.update()
