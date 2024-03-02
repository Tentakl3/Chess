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
            l = 0
            r = 7
            if self.pos[1] == new_pos[1] and self.pos[0] == new_pos[0]:
                return False
            elif self.pos[1] == new_pos[1]:
                for i in range (0,self.pos[0]):
                    if board[i][self.pos[1]] != None:
                        l = i
                for j in range (7,self.pos[0],-1):
                    if board[j][self.pos[1]] != None:
                        r = j
                if l <= new_pos[0] <= r:
                    self.update_moves()
                    self.update_pos(new_pos)
                    return True
                else:
                    return False
            elif self.pos[0] == new_pos[0]:
                l = 0
                r = 7
                for i in range (0,self.pos[1]):
                    if board[self.pos[0]][i] != None:
                        l = i
                for j in range (7,self.pos[1],-1):
                    if board[self.pos[0]][j] != None:
                        r = j
                if l <= new_pos[1] <= r:
                    self.update_moves()
                    self.update_pos(new_pos)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    
    def update_pos(self, new_pos):
        self.pos = new_pos