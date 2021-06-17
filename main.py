import pygame



# Window setting
WIDTH, HEIGHT = 1600, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Graph Algorithms Visualizer')

# Colours
WHITE = (255,255,255)
BLUE = (12, 117, 240)
DARK_BLUE = (34, 40, 81)
ORANGE = (250, 157, 20)
PINK = (175, 19, 132)

# Menu
MENU = pygame.Rect(0, 900, WIDTH, 100)

FPS = 60

NODE_RADIUS = 50
NODE_THICKNESS = 10

LINE_THICKNESS = 20


class Node:
    def __init__(self, x, y, colour):
        self.radius = NODE_RADIUS
        self.x = x
        self.y = y
        self.colour = colour

    def display(self):
        pygame.draw.circle(WIN, self.colour, (self.x, self.y), self.radius, width=0)


class Line:
    def __init__(self, x, y, x_2, y_2, colour):
        self.start = (x, y)
        self.end = (x_2, y_2)
        self.colour = colour


    def display(self):
        pygame.draw.line(WIN, self.colour, self.start, self.end, LINE_THICKNESS)


node_1 = Node(100, 100, BLUE)
node_2 = Node(300, 100, ORANGE)
node_3 = Node(150, 300, BLUE)

line_1 = Line(100+NODE_RADIUS, 100, 300-NODE_RADIUS, 100, ORANGE)

def draw():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, DARK_BLUE, MENU)
    node_1.display()
    node_2.display()
    node_3.display()
    line_1.display()
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        draw()


if __name__ == '__main__':
    main()