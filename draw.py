from config import *
from components.button import *

# Buttons
reset_graph_button = Button(50, 900, 310, 70, ORANGE, 'Reset ↺')
bfs_button = Button(400, 900, 310, 70, ORANGE, 'Breadth-First Search')
buttons = [reset_graph_button, bfs_button]

def draw_graph(nodes, edges):
    for edge in edges:
        for k, v in edge.items():
            v.display()

    for i, node in enumerate(nodes):
        node.display()
        num = FONT.render(f'{i}', True, WHITE)
        if i < 10:
            WINDOW.blit(num, (node.x - 8, node.y - 20))
        else:
            WINDOW.blit(num, (node.x - 18, node.y - 20))


def draw_menu():
    WINDOW.fill(GREY)
    pygame.draw.rect(WINDOW, DARK_BLUE, MENU)
    pygame.draw.rect(WINDOW, WHITE, MENU_BORDER)


def draw(buttons, nodes, edges):
    # 1) Draw menu
    draw_menu()

    # 2) Adding the buttons
    for btn in buttons:
        btn.display()

    # Drawing the edges
    draw_graph(nodes, edges)

    pygame.display.update()