import pygame

from settings import Settings

class Drag:
    def __init__(self):
        self.settings = Settings()

    def get_square_under_mouse(self, board):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - self.settings.board_pos
        x, y = [int(v // self.settings.tilesize) for v in mouse_pos]
        try: 
            if x >= 0 and y >= 0:
                return (board[y][x], x, y)
        except IndexError:
            pass
        return None, None, None
    
    def draw_drag(self, screen, selected_piece, chess_board):
        if selected_piece != None:
            piece, x, y = self.get_square_under_mouse(chess_board)
            if x != None:
                rect = (self.settings.board_pos[0] + x * self.settings.tilesize, self.settings.board_pos[1] + y * self.settings.tilesize, self.settings.tilesize, self.settings.tilesize)
                pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)

            ficha = selected_piece[0].sprite
            s1 = pygame.image.load(f'images/{ficha}')
            pos = pygame.Vector2(pygame.mouse.get_pos())
            screen.blit(s1, s1.get_rect(center=pos))
            selected_rect = pygame.Rect(self.settings.board_pos[0] + selected_piece[1] * self.settings.tilesize, self.settings.board_pos[1] + selected_piece[2] * self.settings.tilesize, self.settings.tilesize, self.settings.tilesize)
            pygame.draw.line(screen, pygame.Color('red'), selected_rect.center, pos)

            return (x, y)