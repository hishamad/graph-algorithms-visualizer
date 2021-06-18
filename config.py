import os
import time
import sys
import pygame
from pygame import gfxdraw
from networkx.generators.random_graphs import gnp_random_graph

pygame.init()
pygame.font.init()

# Window setting
WIDTH, HEIGHT = 1600, 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Graph Algorithms Visualizer')
FPS = 600

# Font
FONT = pygame.font.Font(os.path.join('resources', 'seguisym.ttf'), 30)

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
BROWN = (255, 229, 204)
LIGHT_GREY = (128, 128, 128)

# Menu
MENU = pygame.Rect(0, 850, WIDTH, 150)
MENU_BORDER = pygame.Rect(797, 850, 5, 150)

# Graph settings
NODE_RADIUS = 50
LINE_THICKNESS = 5

