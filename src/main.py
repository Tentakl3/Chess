import sys
import pygame

from settings import Settings
from board import Board
from drag import Drag

class Chess:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.board = Board()
        self.drag = Drag()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.chess_board = self.board.create_board()
        self.chess_board_surf = self.board.create_board_surf()

        pygame.display.set_caption("Chess")

    def run_game(self):
        self.selected_piece = None
        self.drop_pos = None
        while True:
            piece, x, y = self.drag.get_square_under_mouse(self.chess_board)
            self._check_events(piece, x, y)

            self.screen.fill(pygame.Color(self.settings.bg_color))
            self.screen.blit(self.chess_board_surf, self.settings.board_pos)
            self.board.draw_pieces(self.screen, self.chess_board)
            self.board.draw_selector(self.screen, piece, x, y)
            self.drop_pos = self.drag.draw_drag(self.screen, self.selected_piece, self.chess_board)
            
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self, piece, x, y):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if piece != None:
                    self.selected_piece = piece, x, y
            if event.type == pygame.MOUSEBUTTONUP:
                if self.drop_pos:
                    piece, old_x, old_y = self.selected_piece
                    new_x, new_y, = self.drop_pos
                    if self.selected_piece[0].valid_move([new_y, new_x], self.chess_board): 
                        if self.chess_board[new_y][new_x] == None:
                            self.chess_board[old_y][old_x] = None
                            self.chess_board[new_y][new_x] = piece
                        else:
                            if self.chess_board[old_y][old_x].color != self.chess_board[new_y][new_x].color:
                                self.chess_board[old_y][old_x] = None
                                self.chess_board[new_y][new_x] = piece
                            else: 
                                self.chess_board[old_y][old_x] = piece

                self.selected_piece = None
                self.drop_pos = None


if __name__ == "__main__":
    chess = Chess()
    chess.run_game()