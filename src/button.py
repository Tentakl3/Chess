import pygame

class Button:
    def __init__(self, x, y, type_button, scale):
        self.image = pygame.image.load(f'images/button_{type_button}.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False

    def draw_button(self, surface): 
        surface.blit(self.image, (self.rect.x, self.rect.y))