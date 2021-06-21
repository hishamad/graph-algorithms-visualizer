from config import *


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.nodes, self.edges = self.construct_graph()

    def construct_graph(self):
        nodes = []
        edges = [{} for x in self.adjacency_list]
        i, j = 0, 0
        for x in range(int(0.1 * WIDTH), WIDTH, int(0.25 * WIDTH)):  # [200, 600, 1000, 1400]
            for y in range(int(0.2 * HEIGHT), int(HEIGHT - 0.1 * HEIGHT), int(0.3 * HEIGHT)):  # [100, 500, 900]
                if i % 2 == 0:
                    x += int(0.025 * WIDTH)
                else:
                    y -= int(0.04 * WIDTH)
                nodes.append(Node(x, y, LIGHT_GREY))
                j += 1
            i += 1

        for node, neighbours in enumerate(self.adjacency_list):
            for neighbour in neighbours:
                edges[node][neighbour] = Edge(nodes[node].x, nodes[node].y, nodes[neighbour].x, nodes[neighbour].y, WHITE)

        return nodes, edges


class Edge:
    def __init__(self, x, y, x_2, y_2, colour):
        self.start = (x, y)
        self.end = (x_2, y_2)
        self.colour = colour

    def display(self):
        pygame.draw.line(WINDOW, self.colour, self.start, self.end, LINE_THICKNESS)

    def directed_visit(self):
        self.colour = GREEN

    def undirected_visit(self, other):
        self.colour = GREEN
        other.colour = GREEN

    def directed_done(self):
        self.colour = WHITE

    def undirected_done(self, other):
        self.colour = WHITE
        other.colour = WHITE

    def undirected_shortest_path(self, other):
        self.colour = PINK
        other.colour = PINK


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

    def shortest_path(self):
        self.colour = PINK



def generate_random_graph():
    n = 12
    p = 0.2
    g = gnp_random_graph(n, p, seed=None, directed=False)
    return g


