import pygame

from settings import Settings
from pawn import Pawn
from tower import Tower
from horse import Horse
from bishop import Bishop
from queen import Queen
from king import King

class Board:

    def __init__(self):
        self.settings = Settings()

    def create_board_surf(self, i):
        board_surf = pygame.Surface((self.settings.tilesize*8, self.settings.tilesize*8))
        dark = False
        for y in range(8):
            for x in range(8):
                rect = pygame.Rect(x*self.settings.tilesize, y*self.settings.tilesize, self.settings.tilesize, self.settings.tilesize)
                pygame.draw.rect(board_surf, pygame.Color(self.settings.style[i][0] if dark else self.settings.style[i][1]), rect)
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

        board[7][1] = Horse('white', [7,1])
        board[7][6] = Horse('white', [7,6])

        
        board[7][2] = Bishop('white', [7,2])
        board[7][5] = Bishop('white', [7,5])

        board[7][3] = Queen('white', [7,3])

        board[7][4] = King('white', [7,4])


        board[0][0] = Tower('black', [0,0])
        board[0][7] = Tower('black', [0,7])

        board[0][1] = Horse('black', [0,1])
        board[0][6] = Horse('black', [0,6])

        board[0][2] = Bishop('black', [0,2])
        board[0][5] = Bishop('black', [0,5])

        board[0][3] = Queen('black', [0,3])

        board[0][4] = King('black', [0,4])
 

        return board
    
    def draw_pieces(self, screen, board):
        for y in range(8):
            for x in range(8): 
                piece = board[y][x]
                if piece:
                    ficha = piece.sprite
                    s1 = pygame.image.load(f'images/{ficha}')
                    s1 = pygame.transform.scale(s1, (self.settings.tilesize, self.settings.tilesize))
                    pos = pygame.Rect(self.settings.board_pos[0] + x * self.settings.tilesize + 1, self.settings.board_pos[1] + y * self.settings.tilesize + 1, self.settings.tilesize, self.settings.tilesize)
                    screen.blit(s1, s1.get_rect(center=pos.center))

    def draw_selector(self, screen, piece, x, y):
        if piece != None:
            rect = (self.settings.board_pos[0] + x * self.settings.tilesize, self.settings.board_pos[1] + y * self.settings.tilesize, self.settings.tilesize, self.settings.tilesize)
            pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)