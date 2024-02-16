#!/usr/bin/python3

# TTT

# Playing tic tac toe
# I did the minmax algo implementation during week 3 of principles of computing 2 on coursera 
# https://www.coursera.org/learn/principles-of-computing-2/supplement/qMWrV/tttboard-class
# this time I m trying to code the class taking care of the game and board state by myself as well

from random import shuffle

class Board:
	def __init__(self):
		# board size
		self._size = 3
		# boards state {(row,col) : "XO-"}
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
		# First player is X
		self._player = "X"
		# register played moves
		self._played_move = []
		# game finished flag (to disregard extra moves)
		self._is_finished = False 
		# some UI
		print("### Game starting now ###")
		# for random play against itself
		self._pos_left = list(self._state.keys())
		# storing game result for stat purpose
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
	
	def play_at(self, pos):
		if self._is_finished:
			return
		assert pos in self._state.keys(), "playing out of bounds"
		assert not pos in self._played_move, "{} move already played !".format(pos)
		self._state[pos] = self._player
		print(self)
		if self.has_win():
			self.end_game(self._player)
		elif self.is_draw_game():
			self.end_game("-")
		#do last
		self._played_move.append(pos)
		self.switch_player()

	def switch_player(self):
		if self._player == "X":
			self._player = "O"
		else:
			self._player = "X"

	def has_win(self):
		for line in self._winning_lines:
			content = ""
			for pos in line:
				content += self._state[pos]
			if content in ["XXX", "OOO"]:
				self._winner = self._player
				return True			
		return False

	def end_game(self, winner):
		assert winner in ["X", "O", "-"]
		if winner == "-":
			print("Draw Game")
		else:
			print("The winner is {}\n".format(winner))
		self._is_finished = True
		
	def is_draw_game(self):
		if not "-" in self._state.values():
			self._winner = "-"
			return True
		return False

	def random_play(self):
		shuffle(self._pos_left)
		while self._pos_left != []:
			pos = self._pos_left.pop()
			self.play_at(pos)

	def get_winner(self):
		return self._winner

def display_stats(results):
	assert results != [], "No results"
	print("\n~~~~~~~~~~~~~~~\n- TTT RESULTS -\n~~~~~~~~~~~~~~~\n- number of runs : {}\n".format(len(results)))	
	print("X win : {}".format("#"*results.count("X")))
	print("O win : {}".format("#"*results.count("O")))
	print("Draw  : {}".format("#"*results.count("-")))
def main():
	results = []
	for i in range(100):
		b = Board()
		b.random_play()
		results.append(b.get_winner())
	display_stats(results)
	

def test():
	Xwin = [(1,1), (0,1), (0,2), (1,2), (2,2), (1,0),(2,0)]
	Owin = [(1,1), (0,1), (1,0), (0,0), (2,1), (0,2)]
	draw = [(1,1), (0,1), (2,0),(0,2), (1,2), (2,2), (0,0),(1,0),(2,1)]
	b = Board()
	for move in Xwin:
		b.play_at(move)
	b = Board()
	for move in Owin:
		b.play_at(move)
	b = Board()
	for move in draw:
		b.play_at(move)
		
	
main()


# TODO
# - change logic for draw game
	# 1 - check for win
	# 2 - check for board fill
	# if win -> win endgame
	# if board fill -> draw game

# - minmax algo machine learning

# - NN algo machine learning (from scratcyh)












