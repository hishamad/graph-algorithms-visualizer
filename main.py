import sys
import pygame
from pygame import gfxdraw
from networkx.generators.random_graphs import gnp_random_graph

pygame.font.init()

# Window setting
WIDTH, HEIGHT = 1600, 1200
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Graph Algorithms Visualizer')

FONT = pygame.font.SysFont('New Times Roman, Arial', 32)

# Colours
WHITE = (255, 255, 255)
GREY = (35, 35, 35)
BLUE = (12, 117, 240)
DARK_BLUE = (34, 40, 81)
ORANGE = (250, 157, 20)
PINK = (175, 19, 132)

# Menu
MENU = pygame.Rect(0, 1050, WIDTH, 300)

FPS = 10

NODE_RADIUS = 50

LINE_THICKNESS = 5


class Node:
    def __init__(self, x, y, colour):
        self.radius = NODE_RADIUS
        self.x = x
        self.y = y
        self.colour = colour

    def display(self):
        gfxdraw.aacircle(WINDOW, self.x, self.y, self.radius, self.colour)
        gfxdraw.filled_circle(WINDOW, self.x, self.y, self.radius, self.colour)

    def visit(self):
        self.colour = ORANGE

    def backtrack(self):
        self.colour = PINK


class Edge:
    def __init__(self, x, y, x_2, y_2, colour):
        self.start = (x, y)
        self.end = (x_2, y_2)
        self.colour = colour

    def display(self):
        pygame.draw.line(WINDOW, self.colour, self.start, self.end, LINE_THICKNESS)


def generate_random_graph():
    # Generate Random Graph
    n = 12
    p = 0.3
    g = gnp_random_graph(n, p, seed=None, directed=False)
    return g


def generate_nodes(nodes):
    i, j = 0, 0

    for x in range(200, WIDTH, 400):  # [200, 600, 1000, 1400]
        for y in range(150, 1100, 400):  # [100, 500, 900]
            if i % 2 == 0:
                nodes.append(Node(x, y, BLUE))
            else:
                if j % 2 == 0:
                    y -= 50
                    nodes.append(Node(x, y, BLUE))

                else:
                    y -= 50
                    nodes.append(Node(x, y, BLUE))
            j += 1
        i += 1


def draw(g):
    WINDOW.fill(GREY)
    pygame.draw.rect(WINDOW, DARK_BLUE, MENU)

    # Generating the graph
    nodes = []
    edges = []
    generate_nodes(nodes)

    # Drawing the edges
    for edge in g.edges():
        edges.append(Edge(nodes[edge[0]].x, nodes[edge[0]].y, nodes[edge[1]].x, nodes[edge[1]].y, WHITE))
        edges[-1].display()

    # Drawing the nodes
    for i, node in enumerate(nodes):
        node.display()
        num = FONT.render(f'{i}', True, WHITE)
        if i < 10:
            WINDOW.blit(num, (node.x - 8, node.y - 15))
        else:
            WINDOW.blit(num, (node.x - 18, node.y - 15))

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    g = generate_random_graph()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    g = generate_random_graph()
                    pos = pygame.mouse.get_pos()

        draw(g)


if __name__ == '__main__':
    main()
