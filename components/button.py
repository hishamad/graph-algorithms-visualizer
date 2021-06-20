from config import *


class Button:
    def __init__(self, rect, colour, text):
        self.colour = colour
        self.text = text
        self.rect = rect

    def display(self):
        pygame.draw.rect(WINDOW, True, (self.rect.x - 2, self.rect.y - 2, self.rect.width + 4, self.rect.height + 4), 0,
                         1, 1, 1, 1)
        pygame.draw.rect(WINDOW, self.colour, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 0, 1, 1, 1,
                         1)
        text = FONT.render(self.text, 1, WHITE)
        WINDOW.blit(text,
                    (self.rect.x + (self.rect.width / 2 - text.get_width() / 2),
                     self.rect.y + (self.rect.height / 2 - text.get_height() / 2)))

    def on_top(self, pos):
        return self.rect.collidepoint(pos)

    def not_hovered(self):
        self.colour = GREEN

    def hovered(self):
        self.colour = GREY

    def not_hovered_pause(self):
        self.colour = RED

    @staticmethod
    def hover_effect(control_buttons):
        for button in control_buttons:
            if button.on_top(pygame.mouse.get_pos()):
                button.hovered()
            else:
                if button.text == 'Pause':
                    button.not_hovered_pause()
                else:
                    button.not_hovered()
