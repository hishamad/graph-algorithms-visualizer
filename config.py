import os
import pygame

pygame.init()
pygame.font.init()

# Window setting
infoObject = pygame.display.Info()
W_FACTOR = 0.75
WIDTH = int(infoObject.current_w * W_FACTOR)
HEIGHT = int(infoObject.current_h * W_FACTOR)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Graph Algorithms Visualizer')

# Font
FONT = pygame.font.Font(os.path.join('resources', 'seguisym.ttf'), WIDTH//55)
BIG_FONT = pygame.font.Font(os.path.join('resources', 'seguisym.ttf'), WIDTH//22)

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (35, 35, 35)
BLUE = (12, 117, 240)
DARK_BLUE = (34, 40, 81)
ORANGE = (250, 157, 20)
PINK = (175, 19, 132)
RED = (250, 30, 60)
GREEN = (36, 108, 52)
BROWN = (106, 87, 80)
LIGHT_GREY = (62, 66, 71)

# Control Menu
CM_FACTOR = 0.1
CONTROL_MENU = pygame.Rect(0, HEIGHT-CM_FACTOR*HEIGHT, WIDTH, CM_FACTOR*HEIGHT)

# Guide
GUIDE_RECT = pygame.Rect(0.006 * WIDTH, 0.65 * HEIGHT, 0.13 * WIDTH, 0.24 * HEIGHT)
GUIDE_RADIUS = WIDTH//int(0.1*WIDTH)
GUIDE_FONT = pygame.font.Font(os.path.join('resources', 'seguisym.ttf'), WIDTH//80)

# Graph settings
NODE_RADIUS = WIDTH//int(0.018*WIDTH)
LINE_THICKNESS = WIDTH//int(0.12*WIDTH)

# Graph representations
adjacency_list = [[1, 3, 4], [0, 4], [4], [0, 4], [0, 1, 2, 3, 5, 6],
                  [4, 7, 8], [4, 9, 10], [5, 8, 11], [5, 7], [6], [6], [7]]

adjacency_matrix = [[0, 5, 0, 4, 9, 0, 0, 0, 0, 0, 0, 0],
                    [5, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
                    [4, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
                    [9, 7, 6, 3, 0, 7, 9, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 7, 0, 0, 8, 2, 0, 0, 0],
                    [0, 0, 0, 0, 9, 0, 0, 0, 0, 5, 7, 0],
                    [0, 0, 0, 0, 0, 8, 0, 0, 4, 0, 0, 8],
                    [0, 0, 0, 0, 0, 2, 0, 4, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0]]
