#!/usr/bin/python3

# TTT

# Playing tic tac toe
# I did the minmax algo implementation during week 3 of principles of computing 2 on coursera 
# https://www.coursera.org/learn/principles-of-computing-2/supplement/qMWrV/tttboard-class
# this time I m trying to code the class taking care of the game and board state by myself as well

from random import choice
from minimax import monte_carlo, mm
from tests import test_basic_fct, test_random_games, test_board_loading, test_minimax_games, test_monte_carlo_games
from copy import deepcopy

STATEm2 = "X-- OOX XOX"

class Board:
    def __init__(self):
        # board size
        self._size = 3
        # boards state {(row,col) : "X O -"}
        self._state = {}
        # winning lines (arrays of 3 coord tuples) 
        self._winning_lines = []
        # adding diagonals
        self._winning_lines.append(list(zip([0,1,2],[0,1,2])))
        self._winning_lines.append(list(zip([0,1,2],[2,1,0])))
        # populate the board 
        for r in range(self._size):
            row = []
            col = []
            for c in range(self._size):
                self._state[(r, c)] = "-"
                row.append((r, c))
                col.append((c, r))
            self._winning_lines.append(row)
            self._winning_lines.append(col)

        # Board variables
        # First player is X
        self._curr_player = "X"
        # register played moves in order
        self._played_move = []
        # decreasing list of move left
        self._empty_cells = list(self._state.keys())
        # storing game result either "X", "O" or "-" (Draw)
        self._winner = ""
        # latest move (usefull for minimax)
        self._latest_move = (-1,-1)
        
    def __str__(self):
        output = ""
        for row in range(self._size):
            for col in range(self._size):
                output += self._state[(row, col)]
                if col < (self._size - 1 ):
                    output += "|"
            #if row < (self._size - 1):
            #	output += "\n - - \n"
            output += "\n"
        return output
        
    def get_current_player(self):
        return self._curr_player
    
    def get_empty_cells(self):
        """ return tuples of position with - """
        return [pos for pos in self._state.keys() if self._state[pos] == "-"]

    def get_X_cells(self):
        """ return tuples of position with X """
        return [pos for pos in self._state.keys() if self._state[pos] == "X"]
    
    def get_O_cells(self):
        """ return tuples of position with O """
        return [pos for pos in self._state.keys() if self._state[pos] == "O"]

    def get_played_cells(self):
        return get_X_cells(self) + get_O_cells(self)

    def has_a_winner(self):
        for line in self._winning_lines:
            content = ""
            for pos in line:
                content += self._state[pos]
            if content == "XXX":
                self._winner = "X"
                assert self._curr_player == "X", f"player is {self._curr_player}"
                return True
            elif content == "OOO":
                self._winner = "O"
                assert self._curr_player == "O", f"player is {self._curr_player}"
                return True
                
        return False

    def is_draw_game(self):
        if self.get_empty_cells() == [] and not self.has_a_winner():
            self._winner = "-"
            return True
        return False

    def get_winner(self):
        #print("winner is:",self._winner)
        assert self.is_valid_symbol(self._winner), "{} invalid winner".format(self._winner)
        return self._winner

    def game_is_over(self):
        return self.is_draw_game() or self.has_a_winner()

    def is_valid_symbol(self, symbol):
        if symbol in ["X","O","-"]:
            return True
        return False

    def switch_player(self):
        if self._curr_player == "X":
            self._curr_player = "O"
        else:
            self._curr_player = "X"
    
    def play_at(self, pos):
        # dont play if game is over
        if self.game_is_over():
            print("Not cool man")
            return
        # if self.is_empty():
            # print("### Game starting now ###")
        assert pos in self.get_empty_cells(), "{} out of bound or already played".format(pos)
        self._state[pos] = self._curr_player
        self._latest_move = pos
        #print("now playing is:", self._curr_player)
        #print(self)
        
        if self.has_a_winner():
            pass
            # self.prompt_end_game(self._winner)
        elif self.is_draw_game():
            pass
            # self.prompt_end_game("-")
        else:
            self.switch_player()
        
    def prompt_end_game(self, winner):
        assert winner in ["X", "O", "-"]
        if winner == "-":
            print("Draw Game")
        else:
            print("The winner is {}\n".format(winner))
         

    def random_play(self):
        check = self._size ** 2
        while not self.game_is_over() :
            pos = choice(self.get_empty_cells())
            self.play_at(pos)
            check -= 1
            assert check > -1

    def is_empty(self):
        if set(list(self._state.values())) == set("-"):
            return True
        return False
        
    def get_latest_move(self):
        return self._latest_move 
        
    def get_board_state(self):
        return self._state

    def clone(self):
        return deepcopy(self)

    def reset(self):
        self.__init__()

    def load(self, state):
        """
        state : a string such as "X-- OOX XOX"
        """
        symbols = [c for c in list(state) if self.is_valid_symbol(c)]
        assert len(symbols) == self._size ** 2
        for r in range(self._size):
            for c in range(self._size):
                assert (r, c) in self.get_empty_cells(), "invalid entry"
                symbol = symbols[c + (self._size * r)]
                self._state[(r, c)] = symbol
        assert self.is_valid_board_state(), "invalid board state"
        if len(self.get_X_cells()) == len(self.get_O_cells()):
            self._curr_player = "X"
        else:
            self._curr_player = "O"            

    def is_valid_board_state(self):
        # check symbols
        for symbol in self._state.values():
            if not self.is_valid_symbol(symbol):
                return false
        xs = len(self.get_X_cells())
        os = len(self.get_O_cells())
        # check numbers of entries
        if xs != 0 and (xs != os and xs != os+1):
            print("X : {} O {}".format(xs,os))
            return False
        if xs == 0 and os != 0:
            return False 
        return True

    def get_coord_from_index(self, index):
        index_to_coord = {}
        for r in range(self._size):
            for c in range(self._size):
                index_to_coord[c + (self._size * r)] = (r, c)
        return index_to_coord[index]
        
    def prompt_human(self):
        if self.is_empty():
            print("Play by providing a number between 1 and 9\n")
        hum_move = int((input("Your move ?")).rstrip())-1
        move_coord = self.get_coord_from_index(hum_move)
        if not hum_move in range(9):
            print("Play by providing a number between 1 and 9\n")
            self.prompt_human()
        elif not move_coord in self.get_empty_cells():
            print("Move already played, play somewhere else\n")
            self.prompt_human()
        else:                          
            self.play_at(move_coord)

    def human_vs_human(self):
        while not self.game_is_over():
            self.prompt_human()

    def human_vs_random(self):
        while not self.game_is_over():
            self.prompt_human()
            if not self.game_is_over():
                self.play_at(choice(self.get_empty_cells()))

    def montecarlo_vs_montecarlo(self):
        check = self._size ** 2
        while not self.game_is_over() :
            self.play_at(monte_carlo(self))
            check -= 1
            assert check > -1
        print(self)
        self.prompt_end_game(self.get_winner())
    
                      
    def human_vs_montecarlo(self):
        while not self.game_is_over():
            print(self)
            print("now playing is:", self._curr_player)
            
            self.prompt_human()
            if not self.game_is_over():
                self.play_at(monte_carlo(self))
        self.prompt_end_game(self.get_winner())
        print(self)     
    
    # def update():
        # """
        # - scan board state
        # - check its a valid state according to rules
        # - update all the class variables
        # """
        # for r in range(self._size):
            # for c in range(self._size):
                # pos = (r, c)
                # symbol = self._state[pos]
                # assert self.is_valid_symbol(symbol), "unauthorised symbol"
                # if symbol == "X":
                    # self._played_move.append(pos)
                # if symbol == "O":
                    # pass
                # if symbol == "-":
                    # pass
                    
def main():
    b = Board()
    b.load("--- --- ---")
    print(b)
    while not b.game_is_over():
        b.play_at(mm(b)[0])
        print(b)


    # b.human_vs_montecarlo()
    #b.montecarlo_vs_montecarlo()
    # test_monte_carlo_games(b,20)
    
    #print(b.get_empty_cells())
    #print("minimax res : ", cheated(b))
    # print("minimax res : ", minimax_move(b))
    # b.human_vs_random()
    # b.human_vs_human()
    #test_basic_fct(b)
    # test_random_games(b, 10)
    #test_minimax_games(b, 1)
    #print("FINAL \n",b)
    #test_board_loading(b)
    #c = b.clone()
    #b.play_at((1,1))
    #print(b)
    #print(c)

    
main()


# TODO
# - change logic for draw game
    # 1 - check for win
    # 2 - check for board fill
    # if win -> win endgame
    # if board fill -> draw game

# - functions for sending board state and receiving move to/from minimax

# - montecarlo machine player (as seen in principles of computing 1, week 2or3)

# - minmax algo machine learning (as seen in principles of computing 2, week 2)

# - NN algo machine learning (from scratch? with module?)

# - check that a board state is valid

# - use property and remove all the getter

# - play a game from start to finish with a human -> human input

# - prompt to get a move from and index

# - redo get_coord_from_index : we dont want to make an index dic each time







