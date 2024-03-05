import pygame

class Sound:

    def __init__(self):
        pass

    def play(self, path):
        self.path = path
        self.sound = pygame.mixer.Sound(path)
        pygame.mixer.Sound.play(self.sound)