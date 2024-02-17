#!/usr/bin/python3

# Minimax simple implementation for tic-tac-toe game

# - takes a board instance state from a 2 player game (turn based)
# - return a move to be played, a tuple with a position (row, col)

# - board instance needs methods
#   - play_at((row, col))
#   - is_finished()
#   - get_winner()
#   - get_empty_cells()

def minimax_move(board):
	"""
	Takes a board object from TTT.py as input
	Return a tuple (row, col)
	"""
	return  "roger Roger"
	

def compute_moves(board):
	
	pass



# TODO
# - take symmetry into account. There are only 756 possibles boards
#   if rotation and symetry are taken into account.
# - tree pruning
# - during recursion cache the motifs already seen/computed (look at
#   that YT, mcoding I think, fibonnaci with cached values video)
