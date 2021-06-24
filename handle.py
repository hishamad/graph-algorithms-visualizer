from config import *
from components.graph import *
from draw import *




def handle_start_end_node(gr):
    draw(gr)
    start = choose_node(gr)
    gr.nodes[start].start_end()
    draw(gr)
    end = choose_node(gr)
    gr.nodes[end].start_end()
    draw(gr)
    return start, end

def choose_node(gh):
    node = -1
    while node == -1:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for i, node in enumerate(gh.nodes):
                        if node.on_top(pygame.mouse.get_pos()):
                            node = i
                            break

    return node