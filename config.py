import os
import time
import sys
import pygame
from pygame import gfxdraw
from networkx.generators.random_graphs import gnp_random_graph

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
CM_FACTOR = 0.1
CONTROL_MENU = pygame.Rect(0, HEIGHT-CM_FACTOR*HEIGHT, WIDTH, CM_FACTOR*HEIGHT)

# Graph settings
NODE_RADIUS = WIDTH//int(0.018*WIDTH)
LINE_THICKNESS = WIDTH//int(0.12*WIDTH)

