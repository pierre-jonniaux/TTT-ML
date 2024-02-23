#!/usr/bin/python3

# TTT

# Playing tic tac toe
# I did the minmax algo implementation during week 3 of principles of computing 2 on coursera 
# https://www.coursera.org/learn/principles-of-computing-2/supplement/qMWrV/tttboard-class
# this time I m trying to code the class taking care of the game and board state by myself as well

from random import choice
from minimax import minimax_move
from tests import test_basic_fct, test_random_games, test_board_loading
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
		# game finished flag (to disregard extra moves)
		self._is_finished = False 
		# storing game result either "X", "O" or "-" (Draw)
		self._winner = ""
		
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
		assert self._winner in ["X", "O", "-"]
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
			return
		if self.is_empty():
			print("### Game starting now ###")			
		assert pos in self.get_empty_cells(), "out of bound or already played"
		self._state[pos] = self._curr_player

		print("now playing is:", self._curr_player)
		print(self)
		
		if self.has_a_winner():
			self.prompt_end_game(self._curr_player)
		elif self.is_draw_game():
			self.prompt_end_game("-")
		else:
			self.switch_player()
		
	def prompt_end_game(self, winner):
		assert winner in ["X", "O", "-"]
		if winner == "-":
			print("Draw Game")
		else:
			print("The winner is {}\n".format(winner))
		self._is_finished = True
		

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
	#test_basic_fct(b)
	# test_random_games(b, 10)
	test_board_loading(b)
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

# - minmax algo machine learning

# - NN algo machine learning (from scratch)

# - check that a board state is valid

# - use property and remove all the getter











