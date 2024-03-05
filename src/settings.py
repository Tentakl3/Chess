import pygame

class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.board_pos = (144,144)
        self.tilesize = 64
        self.bg_color = "grey"
        self.style = [[(120, 119, 118), (86, 85, 84)], [(234, 235, 200), (119, 154, 88)], [(235, 209, 166), (165, 117, 80)], [(229, 228, 200), (60, 95, 135)]]