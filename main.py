from config import *
from components.graph import *
from algorithms.bfs import *
from draw import *


def main():
    adjacency_list = [[1, 3, 4], [0, 4], [4], [0, 4], [0, 1, 2, 3, 5, 6], [4, 7, 8], [4, 9, 10], [5, 8, 11], [5, 7],
                      [6], [6], [7]]

    nodes, edges = construct_graph(adjacency_list)
    while True:
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

            if reset_graph_button.is_over(pos):
                reset_graph_button.colour = GREY
            elif bfs_button.is_over(pos):
                bfs_button.colour = GREY
            else:
                reset_graph_button.colour = GREEN
                bfs_button.colour = GREEN

        draw(buttons, nodes, edges)


main()
