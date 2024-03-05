import pygame
import time

class Button:
    def __init__(self, x, y, type_button, scale):
        self.j = 1
        self.button = type_button
        self.image = pygame.image.load(f'images/{self.button}_button_{self.j}.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw_button(self, surface): 
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def animate(self, surface):
        while self.j <= 4:
            self.j += 1
            time.sleep(0.2)
            self.image = pygame.image.load(f'images/{self.button}_button_{self.j}.png')
            self.draw_button(surface)
