from config import *
from components.button import *

# Control Buttons
CB_WIDTH = 0.08 * WIDTH
CB_HEIGHT = 0.05 * HEIGHT

back_button = Button(pygame.Rect(0.01*WIDTH, 0.93 * HEIGHT, CB_WIDTH, CB_HEIGHT), GREEN, '< Back')
reset_graph_button = Button(pygame.Rect(0.5 * WIDTH + (2.5 * CB_WIDTH) - CB_WIDTH, 0.93 * HEIGHT, CB_WIDTH, CB_HEIGHT),
                            GREEN, 'Reset ↺')
start_button = Button(pygame.Rect(0.5 * WIDTH - 2.5 * CB_WIDTH, 0.93 * HEIGHT, CB_WIDTH, CB_HEIGHT), GREEN, 'Start')
pause_button = Button(pygame.Rect(0.5 * WIDTH - 0.5 * CB_WIDTH, 0.93 * HEIGHT, CB_WIDTH, CB_HEIGHT), RED, 'Pause')

control_buttons = [start_button, pause_button, reset_graph_button, back_button]

# Menu buttons
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
