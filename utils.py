from config import *
from draw import draw_menu

def handle_control_menu(event, control_buttons, draw):
    cont = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if control_buttons[1].on_top(pygame.mouse.get_pos()):
            control_buttons[0].not_hovered()
            control_buttons[1].hovered()
            control_buttons[1].text = 'Continue'
            draw()
            cont, back = check_pause(control_buttons)
            control_buttons[1].text = 'Pause'
            control_buttons[1].not_hovered_pause()
            draw()
            if not cont:
                control_buttons[2].hovered()
                draw()
                return False
            elif back:
                control_buttons[3].hovered()
                draw()
                return False
        elif control_buttons[2].on_top(pygame.mouse.get_pos()):
            control_buttons[2].hovered()
            draw()
            return False
        elif control_buttons[0].on_top(pygame.mouse.get_pos()):
            control_buttons[0].hovered()
            draw()
        elif control_buttons[3].on_top(pygame.mouse.get_pos()):
            return False

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    return cont


def update(draw):
    draw()
    time.sleep(0.5)

def check_pause(control_buttons):
    run = True
    cont = True
    back = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if control_buttons[2].on_top(pygame.mouse.get_pos()):
                        cont = False
                        return cont, back
                    elif control_buttons[3].on_top(pygame.mouse.get_pos()):
                        back = True
                        return cont, back
                    elif control_buttons[1].on_top(pygame.mouse.get_pos()):
                        return cont, back

    return cont, back