import pygame

class Tower:
    def __init__(self, color, pos):
        self.color = color
        self.sprite = color + "_tower.png"
        self.pos = pos 
        self.moves = 0

    def update_moves(self):
        self.moves += 1

    def valid_move(self, new_pos, board):
        if new_pos[0] != None:
            if self.pos[1] == new_pos[1]:
                if 0 < abs(self.pos[0] - new_pos[0]) <= 7:
                    if board[new_pos[0]][new_pos[1]] == None: 
                        self.update_moves()
                        self.update_pos(new_pos)
                        return True
                    else:
                        return False
            if self.pos[0] == new_pos[0]:
                if 0 < abs(self.pos[1] - new_pos[1]) <= 7:
                    if board[new_pos[0]][new_pos[1]] == None: 
                        self.update_moves()
                        self.update_pos(new_pos)
                        return True
                    else:
                        return False
        else:
            return False

    
    def update_pos(self, new_pos):
        self.pos = new_pos