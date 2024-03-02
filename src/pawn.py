import pygame

class Pawn:
    def __init__(self, color, pos):
        self.color = color
        self.sprite = color + "_pawn.png"
        self.pos = pos 
        self.moves = 0

    def update_moves(self):
        self.moves += 1

    def valid_move(self, new_pos, board):
        if new_pos[0] != None:
            if self.pos[1] == new_pos[1] and self.pos[0] == new_pos[0]:
                return False
            elif self.moves < 1:
                if self.pos[1] == new_pos[1]:
                    if self.color == 'white':

                        if 0 < (self.pos[0] - new_pos[0]) <= 2:
                            if board[new_pos[0]][new_pos[1]] == None:
                                self.update_moves()
                                self.update_pos(new_pos)
                                return True
                            else:
                                return False
                        else:
                            return False  
                    
                    else:

                        if 0 > (self.pos[0] - new_pos[0]) >= -2:
                            if board[new_pos[0]][new_pos[1]] == None:
                                self.update_moves()
                                self.update_pos(new_pos)
                                return True
                            else:
                                return False
                        else:
                            return False  
                            
                elif abs(self.pos[1] - new_pos[1]) == 1:
                    if self.color == 'white':

                        if 0 < (self.pos[0] - new_pos[0]) <= 1:
                                if board[new_pos[0]][new_pos[1]] != None:
                                    self.update_moves()
                                    self.update_pos(new_pos)
                                    return True
                                else:
                                    return False
                        else:
                            return False
                        
                    else:

                        if 0 > (self.pos[0] - new_pos[0]) >= -1:
                                if board[new_pos[0]][new_pos[1]] != None:
                                    self.update_moves()
                                    self.update_pos(new_pos)
                                    return True
                                else:
                                    return False
                        else:
                            return False

                    
                else:
                    return False

            else:
                if self.pos[1] == new_pos[1]:
                    if self.color == 'white':

                        if  (self.pos[0] - new_pos[0]) == 1:
                            if board[new_pos[0]][new_pos[1]] == None:
                                self.update_moves()
                                self.update_pos(new_pos)
                                return True
                            else:
                                return False                
                        else:
                            return False
                    
                    else:

                        if  (self.pos[0] - new_pos[0]) == -1:
                            if board[new_pos[0]][new_pos[1]] == None:
                                self.update_moves()
                                self.update_pos(new_pos)
                                return True
                            else:
                                return False                
                        else:
                            return False
                    
                elif abs(self.pos[1] - new_pos[1]) == 1:
                    if self.color == 'white':

                        if (self.pos[0] - new_pos[0]) == 1:
                                if board[new_pos[0]][new_pos[1]] != None:
                                    self.update_moves()
                                    self.update_pos(new_pos)
                                    return True
                                else:
                                    return False
                        else:
                            return False
                        
                    else:

                        if (self.pos[0] - new_pos[0]) == -1:
                                if board[new_pos[0]][new_pos[1]] != None:
                                    self.update_moves()
                                    self.update_pos(new_pos)
                                    return True
                                else:
                                    return False
                        else:
                            return False
                    
                else:
                    return False
        else:
            return False

    
    def update_pos(self, new_pos):
        self.pos = new_pos