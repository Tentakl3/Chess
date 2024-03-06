import sys
import pygame

from settings import Settings
from board import Board
from drag import Drag
from button import Button
from sound import Sound

class Chess:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.board = Board()
        self.drag = Drag()
        self.sound = Sound()
        self.players = ['black', 'white']
        self.switch = True
        self.winner = ''
        self.i = 0
        self.bg = pygame.image.load("images/temp_background.png")

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.chess_board = self.board.create_board()
        self.chess_board_surf = self.board.create_board_surf(self.i)

        pygame.display.set_caption("Chess")
        self.start_button = Button(400, 400, 'start', 1)
        self.off_button = Button(400, 600, 'off', 1)

        self.start_window = True
        self.play_window = False
        self.options_window = False
        self.final_window = False

    def run_game(self):
        self.selected_piece = None
        self.drop_pos = None
        while True:
            piece, x, y = self.drag.get_square_under_mouse(self.chess_board)
            mouse_pos = pygame.mouse.get_pos()
            self._check_events(piece, x, y, mouse_pos)
            self.screen.fill(pygame.Color(self.settings.bg_color))
         
            if self.play_window:
                self.screen.blit(self.bg, (0, 0))
                self.screen.blit(self.chess_board_surf, self.settings.board_pos)
                self.board.draw_pieces(self.screen, self.chess_board)
                self.board.draw_selector(self.screen, piece, x, y)
                self.drop_pos = self.drag.draw_drag(self.screen, self.selected_piece, self.chess_board)
            elif self.start_window:
                self.screen.blit(self.bg, (0, 0))
                self.start_button.draw_button(self.screen)
                self.off_button.draw_button(self.screen)
                
                
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self, piece, x, y, mouse_pos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    if self.i <= 2:
                        self.i = self.i + 1
                    else:
                        self.i = 0
                    self.chess_board_surf = self.board.create_board_surf(self.i)
                elif event.key == pygame.K_r:
                    self.chess_board = self.board.create_board()
                    self.switch = True
                    self.play_window = True
                    self.final_window = False

            elif self.start_window:
                if self.start_button.rect.collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # TODO animate buttons
                        """
                        self.start_button.animate(self.screen)
                        """
        
                        self.start_window = False
                        self.play_window = True
                if self.off_button.rect.collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        sys.exit()
                        
            elif self.play_window:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if piece != None:
                        self.selected_piece = piece, x, y
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.drop_pos:
                        piece, old_x, old_y = self.selected_piece
                        new_x, new_y, = self.drop_pos
                        if self.switch:
                            if self.selected_piece[0].color == 'white':
                                if self.selected_piece[0].valid_move([new_y, new_x], self.chess_board):
                                    self.switch = False
                                    if self.chess_board[new_y][new_x] != None:
                                        if self.chess_board[new_y][new_x].type != 'king':
                                            self.sound.play('sounds/move-self.mp3')
                                            self.chess_board[old_y][old_x] = None
                                            self.chess_board[new_y][new_x] = piece
                                        else:
                                            self.sound.play('sounds/notify.mp3')
                                            self.play_window = False
                                            self.final_window = True
                                            self.winner = 'white'
                                    else:
                                        self.sound.play('sounds/move-self.mp3')
                                        self.chess_board[old_y][old_x] = None
                                        self.chess_board[new_y][new_x] = piece
                                else: 
                                    self.chess_board[old_y][old_x] = piece
                            else:
                                self.chess_board[old_y][old_x] = piece
                        else:
                            if self.selected_piece[0].color == 'black':
                                if self.selected_piece[0].valid_move([new_y, new_x], self.chess_board):
                                    self.switch = True
                                    if self.chess_board[new_y][new_x] != None:
                                        if self.chess_board[new_y][new_x].type != 'king':
                                            self.sound.play('sounds/move-self.mp3')
                                            self.chess_board[old_y][old_x] = None
                                            self.chess_board[new_y][new_x] = piece
                                        else:
                                            self.sound.play('sounds/notify.mp3')
                                            self.play_window = False
                                            self.final_window = True
                                            self.winner = 'black'
                                    else:
                                        self.sound.play('sounds/move-self.mp3')
                                        self.chess_board[old_y][old_x] = None
                                        self.chess_board[new_y][new_x] = piece
                            else:
                                self.chess_board[old_y][old_x] = piece

                    self.selected_piece = None
                    self.drop_pos = None


if __name__ == "__main__":
    chess = Chess()
    chess.run_game()