#!/usr/bin/python3

# Minimax simple implementation for tic-tac-toe game

# Algo :
# - A tree emerge from all possible moves from an initial board state root node.
# - We will choose a root->leaf path that get the best result (here for 1P for ex.).
# - The scoring method used to choose the path is called Minimax.
# - We choose the path recursively going from the leaves to the root.
# - Because we assume the opponent will play its best move, we do not score in
#   order to win but to not loose; in the tree we choose the safer path,
#   not the path which could lead to a win but requires a blunder from 2P.
# - At the final states (leaves) we can have 1Pwin/1Ploose/draw : 3 scores +1 -1 0
# - we go back from the leaves to the root and to node n we assign the score
#   from one of the n+1 node.
# - from next possibles states/nodes we choose either the max score or the 
#   minimum score depending on whose turn it is.  
# - so inbetween the leaves and the root we alternate between trying to
#   maximize or minmize the score
# - if we want 1P to win it means maximize the root node score 
#   (root node = playing first = 1P), minimize the second level and so on

# - takes a board instance state from a 2 player game (turn based)
# - return a move to be played, a tuple with a position (row, col)
# - board instance needs methods
#   - play_at((row, col))
#   - is_finished()
#   - get_winner()
#   - get_empty_cells()

SCORING = {"X":1 , "O":-1, "-":0}

def mm2(board):
    """Return a position and a score"""
    max_turn = board.get_current_player() == "X"
    
    if board.game_is_over():
        return board.get_latest_move(), SCORING[board.get_winner()]

    possible_moves = board.get_empty_cells()

    if max_turn:
        scores = []
        moves = []
        for move in possible_moves:
            clone = board.clone()
            clone.play_at(move)
            move, score = mm2(clone)
            moves.append(move)
            scores.append(score)
        return moves[scores.index(max(scores))], max(scores)
        # scores = [mm2(board.clone().play_at(move)) for move in possible_moves]
        # moves = [move for move in possible_moves]
        # return moves[scores.index(max(scores))], max(scores)
    else:
        scores = []
        moves = []
        for move in possible_moves:
            clone = board.clone()
            clone.play_at(move)
            move, score = mm2(clone)
            moves.append(move)
            scores.append(score)
        return moves[scores.index(min(scores))], min(scores)
        # scores = [mm2(board.clone().play_at(move)) for move in possible_moves]
        # moves = [move for move in possible_moves]
        # return moves[scores.index(min(scores))], min(scores)

def best_move(board):
    scores = []
    moves = []
    for possible_move in board.get_empty_cells():
        clone = board.clone()
        clone.play_at(possible_move)
        move, score = mm2(clone)
        moves.append(move)
        scores.append(score)
    return moves[scores.index(max(scores))], max(scores)
        

def mm(board):
    """Return a position and a score"""

    if board.game_is_over():
        return board.get_latest_move(), SCORING[board.get_winner()]

    scores = []
    moves = []
    for possible_move in board.get_empty_cells():
        clone = board.clone()
        clone.play_at(possible_move)
        move, score = mm(clone)
        moves.append(move)
        scores.append(score)
    # print(scores, moves)
    # here current player is the one that has played already
        if board.get_current_player() == "O":
            return moves[scores.index(max(scores))], max(scores)
        if board.get_current_player() == "X":
            return moves[scores.index(min(scores))], min(scores)


def nim_minimax(ns):
    
    if ns.is_game_over():
        return 1 if ns.get_winner() == 1 else -1



def monte_carlo(board, tries=100):
    """
    - Play random moves until game completion 
    - Record wins and losses
    - Assign weights to positions according to those records
    - Return the best position (max weigth)
    """
    weights = {}
    for pos in board.get_empty_cells():
        weights[pos] = 0
    
    for i in range(tries):
        # play random until board completion
        b = board.clone()
        b.random_play()
        
        if b.get_winner() == "X":
            for x_pos in b.get_X_cells():
                if x_pos in weights:
                    weights[x_pos] += 1
        elif b.get_winner() == "O":
            for o_pos in b.get_O_cells():
                if o_pos in weights:
                    weights[o_pos] += 1
    best_score = 0
    best_pos = ()
    for p in weights.keys():
        if weights[p] >= best_score:
            best_score = weights[p]
            best_pos = p
    return best_pos
  

            
# TODO
# - take symmetry into account. There are only 756 possibles boards
#   if rotation and symetry are taken into account.
# - tree pruning (alpha beta)
# - during recursion cache the motifs already seen/computed (look at
#   that YT, mcoding I think, fibonnaci with cached values video)


# 
# def mmpruning(board,alpha,beta):
    # """Return a position and a score"""
# 
    # if board.game_is_over():
        # return board.get_latest_move(), SCORING[board.get_winner()]
# 
    # scores = []
    # moves = []
    # for possible_move in board.get_empty_cells():
        # clone = board.clone()
        # clone.play_at(possible_move)
        # move, score = mm(clone, alpha, beta)
        # moves.append(move)
        # scores.append(score)
    # # print(scores, moves)
    # # here current player is the one that has played already
        # if board.get_current_player() == "O":
            # m, s = moves[scores.index(max(scores))], max(scores)
            # alpha = max(alpha, s)
            # if beta <= alpha:
                # break
            # return m, s
        # if board.get_current_player() == "X":
            # m, s = moves[scores.index(min(scores))], min(scores)
            # beta = min(beta, s)
            # if beta <= alpha:
                # break
            # return m, s

