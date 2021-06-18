import sys
import time

import pygame
from pygame import gfxdraw
from networkx.generators.random_graphs import gnp_random_graph

pygame.font.init()

# Window setting
WIDTH, HEIGHT = 1600, 1200
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Graph Algorithms Visualizer')
FPS = 600

# Font
FONT = pygame.font.SysFont('New Times Roman, Arial', 32)

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
MENU = pygame.Rect(0, 900, WIDTH, 300)
MENU_BORDER = pygame.Rect(797, 900, 5, 300)

# Graph settings
NODE_RADIUS = 50
LINE_THICKNESS = 5


class Node:
    def __init__(self, x, y, colour):
        self.radius = NODE_RADIUS
        self.x = x
        self.y = y
        self.colour = colour
        self.visited = False

    def display(self):
        gfxdraw.aacircle(WINDOW, self.x, self.y, self.radius, self.colour)
        gfxdraw.filled_circle(WINDOW, self.x, self.y, self.radius, self.colour)

    def visit(self):
        self.colour = GREEN
        self.visited = True

    def current(self):
        self.colour = RED

    def done(self):
        self.colour = ORANGE


class Edge:
    def __init__(self, x, y, x_2, y_2, colour):
        self.start = (x, y)
        self.end = (x_2, y_2)
        self.colour = colour

    def display(self):
        pygame.draw.line(WINDOW, self.colour, self.start, self.end, LINE_THICKNESS)

    def visit(self):
        self.colour = GREEN

    def done(self):
        self.colour = WHITE

class Button:
    def __init__(self, x, y, width, height, colour, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text

    def display(self):
        pygame.draw.rect(WINDOW, True, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(WINDOW, self.colour, (self.x, self.y, self.width, self.height), 0)
        text = FONT.render(self.text, 1, WHITE)
        WINDOW.blit(text,
                    (self.x + (self.width / 2 - text.get_width() / 2),
                     self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        else:
            return False


def generate_random_graph():
    n = 12
    p = 0.2
    g = gnp_random_graph(n, p, seed=None, directed=False)
    return g


def construct_graph(adjacency_list):
    nodes = []
    edges = [{} for x in adjacency_list]
    i, j = 0, 0

    for x in range(200, WIDTH, 400):  # [200, 600, 1000, 1400]
        for y in range(150, 1000, 300):  # [100, 500, 900]
            if i % 2 == 0:
                x += 50
            else:
                y -= 75
            nodes.append(Node(x, y, LIGHT_GREY))
            j += 1
        i += 1

    for node, neighbours in enumerate(adjacency_list):
        for neighbour in neighbours:
            edges[node][neighbour] = Edge(nodes[node].x, nodes[node].y, nodes[neighbour].x, nodes[neighbour].y, WHITE)

    return nodes, edges


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
    # Buttons
    reset_graph_button = Button(50, 975, 310, 70, ORANGE, 'Reset')
    bfs_button = Button(50, 1075, 310, 70, ORANGE, 'Breadth-First Search')
    buttons = [reset_graph_button, bfs_button]
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

        draw(buttons, nodes, edges)


main()
