from config import *
from draw import *


def handle_control_menu(event, graph):
    reset = False
    back = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if control_buttons[1].on_top(pygame.mouse.get_pos()):
            control_buttons[1].hovered()
            control_buttons[1].text = 'Continue'
            draw(graph)
            reset, back = check_pause()
            control_buttons[1].text = 'Pause'
            control_buttons[1].not_hovered_pause()
            draw(graph)
            if reset:
                control_buttons[2].hovered()
                draw(graph)
                return reset, back
            elif back:
                control_buttons[3].hovered()
                draw(graph)
                return reset, back
        elif control_buttons[2].on_top(pygame.mouse.get_pos()):
            reset = True
            control_buttons[2].hovered()
            draw(graph)
            return reset, back
        elif control_buttons[3].on_top(pygame.mouse.get_pos()):
            back = True
            return reset, back



    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    return reset, back


def update(graph, speed, up_graph=True):
    for event in pygame.event.get():
        reset, back = handle_control_menu(event, graph)
        if reset or back:
            return reset, back

    if up_graph:
        draw(graph)
        pygame.time.wait(speed)

    return False, False


def check_pause():
    run = True
    reset = False
    back = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if control_buttons[2].on_top(pygame.mouse.get_pos()):
                        reset = True
                        return reset, back
                    elif control_buttons[3].on_top(pygame.mouse.get_pos()):
                        back = True
                        return reset, back
                    elif control_buttons[1].on_top(pygame.mouse.get_pos()):
                        return reset, back

    return reset, back


class Error(Exception):
    pass
