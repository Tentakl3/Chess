import pygame

from settings import Settings
from pawn import Pawn
from tower import Tower

class Board:

    def __init__(self):
        self.settings = Settings()

    def create_board_surf(self):
        board_surf = pygame.Surface((self.settings.tilesize*8, self.settings.tilesize*8))
        dark = False
        for y in range(8):
            for x in range(8):
                rect = pygame.Rect(x*self.settings.tilesize, y*self.settings.tilesize, self.settings.tilesize, self.settings.tilesize)
                pygame.draw.rect(board_surf, pygame.Color('black' if dark else 'white'), rect)
                dark = not dark
            dark = not dark

        return board_surf
    
    def create_board(self):
        board = []
        for y in range(8):
            board.append([])
            for x in range(8):
                board[y].append(None)
            
        for x in range(0,8):
            board[1][x] = Pawn('black', [1,x])
        for x in range(0,8):
            board[6][x] = Pawn('white', [6,x])

        
        board[7][0] = Tower('white', [7,0])
        board[7][7] = Tower('white', [7,7])
        """
        board[7][1] = ('white', 'horse')
        board[7][6] = ('white', 'horse')

        board[7][2] = ('white', 'bishop')
        board[7][5] = ('white', 'bishop')

        board[7][3] = ('white', 'queen')
        """

        board[0][0] = Tower('black', [0,0])
        board[0][7] = Tower('black', [0,7])
        """
        board[0][1] = ('black', 'horse')
        board[0][6] = ('black', 'horse')

        board[0][2] = ('black', 'bishop')
        board[0][5] = ('black', 'bishop')

        board[0][3] = ('black', 'queen')
        """

        return board
    
    def draw_pieces(self, screen, board):
        for y in range(8):
            for x in range(8): 
                piece = board[y][x]
                if piece:
                    ficha = piece.sprite
                    s1 = pygame.image.load(f'images/{ficha}')
                    pos = pygame.Rect(self.settings.board_pos[0] + x * self.settings.tilesize+1, self.settings.board_pos[1] + y * self.settings.tilesize + 1, self.settings.tilesize, self.settings.tilesize)
                    screen.blit(s1, s1.get_rect(center=pos.center))

    def draw_selector(self, screen, piece, x, y):
        if piece != None:
            rect = (self.settings.board_pos[0] + x * self.settings.tilesize, self.settings.board_pos[1] + y * self.settings.tilesize, self.settings.tilesize, self.settings.tilesize)
            pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)