import pygame.draw
import os
import math
from buttons import *


def draw_graph(graph):
    already = [[False for _ in range(len(graph.nodes))] for _ in range(len(graph.nodes))]
    for i, edges in enumerate(graph.edges):
        for k, edge in edges.items():
            edge.display()
            if graph.weighted and not already[i][k]:
                weight = FONT.render(f'{edge.weight}', True, WHITE)
                x = edge.start[0] + (edge.end[0] - edge.start[0]) / 2
                y = edge.start[1] + (edge.end[1] - edge.start[1]) / 2
                if edge.end[0] - edge.start[0] == 0:
                    weight = pygame.transform.rotozoom(weight, -90, 1)
                    WINDOW.blit(weight, (x, y))
                else:
                    angle = math.degrees(math.atan((edge.end[1] - edge.start[1])/(edge.end[0] - edge.start[0])))
                    weight = pygame.transform.rotozoom(weight, -angle, 1)
                    if edge.end[1] - edge.start[1] <= 0:
                        WINDOW.blit(weight, (x - weight.get_width(), y - weight.get_height()))
                    else:
                        WINDOW.blit(weight, (x, y - weight.get_height()))
                already[i][k] = True
                already[k][i] = True

    for i, node in enumerate(graph.nodes):
        node.display()
        # if i == 0:
        #     num = FONT.render('S', True, WHITE)
        # elif i == len(graph.nodes) - 1:
        #     num = FONT.render('E', True, WHITE)
        # else:
        num = FONT.render(f'{i}', True, WHITE)
        WINDOW.blit(num, (node.x - num.get_width() / 2, node.y - num.get_height() / 2))


def draw_menu():

    background = pygame.image.load(os.path.join('resources', 'background.jpg')).convert()
    WINDOW.blit(background, (0,0))
    title = BIG_FONT.render("Graph Algorithms Visualizer", True, WHITE)
    WINDOW.blit(title, (0.5*WIDTH-title.get_width()/2, 0.065*HEIGHT))
    for btn in menu_buttons:
        btn.display()
    pygame.display.update()


def draw_guide_rect():
    pygame.draw.rect(WINDOW, WHITE, GUIDE_RECT, width=3)
    pygame.draw.circle(WINDOW, BLUE, (3.5*GUIDE_RECT.x, 1.05*GUIDE_RECT.y), GUIDE_RADIUS)
    pygame.draw.circle(WINDOW, RED, (3.5*GUIDE_RECT.x, 1.12*GUIDE_RECT.y), GUIDE_RADIUS)
    pygame.draw.circle(WINDOW, GREEN, (3.5*GUIDE_RECT.x, 1.19*GUIDE_RECT.y), GUIDE_RADIUS)
    pygame.draw.circle(WINDOW, ORANGE, (3.5*GUIDE_RECT.x, 1.26*GUIDE_RECT.y), GUIDE_RADIUS)
    pygame.draw.circle(WINDOW, PINK, (3.5*GUIDE_RECT.x, 1.33*GUIDE_RECT.y), GUIDE_RADIUS)
    start_end = GUIDE_FONT.render("Start/End", True, WHITE)
    processing = GUIDE_FONT.render("Processing", True, WHITE)
    waiting = GUIDE_FONT.render("Waiting", True, WHITE)
    processed = GUIDE_FONT.render("Processed", True, WHITE)
    shortest = GUIDE_FONT.render("Shortest Path/MST", True, WHITE)
    WINDOW.blit(start_end, (5*GUIDE_RECT.x, 1.05*GUIDE_RECT.y-start_end.get_height()/2))
    WINDOW.blit(processing, (5*GUIDE_RECT.x, 1.12*GUIDE_RECT.y-processing.get_height()/2))
    WINDOW.blit(waiting, (5*GUIDE_RECT.x, 1.19*GUIDE_RECT.y-waiting.get_height()/2))
    WINDOW.blit(processed, (5*GUIDE_RECT.x, 1.26*GUIDE_RECT.y-processed.get_height()/2))
    WINDOW.blit(shortest, (5*GUIDE_RECT.x, 1.33*GUIDE_RECT.y-shortest.get_height()/2))


def draw(graph):
    # Draw menu
    WINDOW.fill(GREY)
    pygame.draw.rect(WINDOW, DARK_BLUE, CONTROL_MENU)

    # Draw the guide rectangle
    draw_guide_rect()

    # Adding the control_buttons0
    for btn in control_buttons:
        btn.display()

    # Drawing the edges
    draw_graph(graph)

    pygame.display.update()
