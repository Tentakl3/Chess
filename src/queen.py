import pygame

class Queen:
    def __init__(self, color, pos):
        self.color = color
        self.type = 'queen'
        self.sprite = color + f"_{self.type}.png"
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
            elif abs(self.pos[0] - new_pos[0]) == abs(self.pos[1] - new_pos[1]):
                if (self.pos[0] - new_pos[0]) < 0 and (self.pos[1] - new_pos[1]) < 0:
                    fy, fx = self.diagonal_maping(1, 1, board)

                    if self.pos[0] < new_pos[0] <= fy and self.pos[1] < new_pos[1] <= fx:
                        if board[new_pos[0]][new_pos[1]] != None:
                            if self.color == board[new_pos[0]][new_pos[1]].color:
                                return False
                            else:
                                self.update_moves()
                                self.update_pos(new_pos)
                                return True
                        else:
                            self.update_moves()
                            self.update_pos(new_pos)
                            return True
                elif (self.pos[0] - new_pos[0]) > 0 and (self.pos[1] - new_pos[1]) > 0:
                    fy, fx = self.diagonal_maping(-1, -1, board)

                    if self.pos[0] > new_pos[0] >= fy and self.pos[1] > new_pos[1] >= fx:
                        if board[new_pos[0]][new_pos[1]] != None:
                            if self.color == board[new_pos[0]][new_pos[1]].color:
                                return False
                            else:
                                self.update_moves()
                                self.update_pos(new_pos)
                                return True
                        else:
                            self.update_moves()
                            self.update_pos(new_pos)
                            return True         
                elif (self.pos[0] - new_pos[0]) > 0 and (self.pos[1] - new_pos[1]) < 0:
                    fy, fx = self.diagonal_maping(-1, 1, board)

                    if self.pos[0] > new_pos[0] >= fy and self.pos[1] < new_pos[1] <= fx:
                        if board[new_pos[0]][new_pos[1]] != None:
                            if self.color == board[new_pos[0]][new_pos[1]].color:
                                return False
                            else:
                                self.update_moves()
                                self.update_pos(new_pos)
                                return True
                        else:
                            self.update_moves()
                            self.update_pos(new_pos)
                            return True
                elif (self.pos[0] - new_pos[0]) < 0 and (self.pos[1] - new_pos[1]) > 0:
                    fy, fx = self.diagonal_maping(1, -1, board)

                    if self.pos[0] < new_pos[0] <= fy and self.pos[1] > new_pos[1] >= fx:
                        if board[new_pos[0]][new_pos[1]] != None:
                            if self.color == board[new_pos[0]][new_pos[1]].color:
                                return False
                            else:
                                self.update_moves()
                                self.update_pos(new_pos)
                                return True
                        else:
                            self.update_moves()
                            self.update_pos(new_pos)
                            return True
                else:
                    return False
            elif self.pos[1] == new_pos[1]:
                for i in range (0,self.pos[0]):
                    if board[i][self.pos[1]] != None:
                        l = i
                for j in range (7,self.pos[0],-1):
                    if board[j][self.pos[1]] != None:
                        r = j
                if l <= new_pos[0] <= r:
                    if board[new_pos[0]][new_pos[1]] != None:
                        if self.color == board[new_pos[0]][new_pos[1]].color:
                            return False
                        else:
                            self.update_moves()
                            self.update_pos(new_pos)
                            return True
                    else:
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
                    if board[new_pos[0]][new_pos[1]] != None:
                        if self.color == board[new_pos[0]][new_pos[1]].color:
                            return False
                        else:
                            self.update_moves()
                            self.update_pos(new_pos)
                            return True
                    else:
                        self.update_moves()
                        self.update_pos(new_pos)
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def diagonal_maping(self, dy, dx, board):
        i = self.pos[0]
        j = self.pos[1]
        if dy == 1:
            if dx == 1:
                while i < 7 and j < 7:
                    i = i + dy
                    j = j + dx 
                    if board[i][j] != None:
                        return[i,j]
            else:
                while i < 7 and j > 0:
                    i = i + dy
                    j = j + dx 
                    if board[i][j] != None:
                        return[i,j]
        else:
            if dx == 1:
                while i > 0 and j < 7:
                    i = i + dy
                    j = j + dx 
                    if board[i][j] != None:
                        return[i,j]
            else:
                while i > 0 and j > 0:
                    i = i + dy
                    j = j + dx 
                    if board[i][j] != None:
                        return[i,j]
        return[i,j]

    
    def update_pos(self, new_pos):
        self.pos = new_pos