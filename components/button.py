from config import *

class Button:
    def __init__(self, x, y, width, height, colour, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text

    def display(self):
        pygame.draw.rect(WINDOW, True, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0, 5, 5, 5, 5)
        pygame.draw.rect(WINDOW, self.colour, (self.x, self.y, self.width, self.height),  0, 5, 5, 5, 5)
        text = FONT.render(self.text, 1, WHITE)
        WINDOW.blit(text,
                    (self.x + (self.width / 2 - text.get_width() / 2),
                     self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        else:
            return False
