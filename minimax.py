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





def temp_minimax_move(board):
    """
    Takes a board object from TTT.py as input
    Return a tuple (row, col) and a score
    """
    score = 0
    pos = (0, 0)
#########################  WAS HERE ################################
    # while more than one move left : recursion
    while len(board.get_empty_cells()) > 1 and not board.game_is_over():
        for possible_move in board.get_empty_cells():
            possible_board = board.clone()
            playing = possible_board.get_current_player()
            possible_board.play_at(possible_move)
            # if game over no score to choose from
            if possible_board.game_is_over():
                    if playing == "X":    
                        return possible_move, 1
                    elif playing == "O":    
                        return possible_move, -1
                    elif playing == "-":    
                           return possible_move, 0
            # game is not over : we choose from several scores
            # if playing == "X":
                        # return
                    # elif playing == "O":
                        # return possible_move, -1
                    # elif playing == "-":
                           # return possible_move, 0
            # mm_move, score = minimax_move(possible_board)
            # return a score and a pos
            
#########################  WAS HERE ################################

    # Out of while without a game over so far meaning only one position 
    # left before P1win/P1loss/draw. Play it/update board and return info
    possible_board = board.clone()
    last_move = possible_board.get_empty_cells()
    playing = possible_board.get_current_player() 
    possible_board.play_at(last_move)
    if playing == "X":    
        return last_move, 1
    elif playing == "O":    
        return last_move, -1
    elif playing == "-":    
           return last_move, 0

def compute_moves(board):
    
    pass

def minimax_move(board):
    best_score = 0
    best_pos = board.get_empty_cells()[-1]
    # tmp_board = board.clone()

    if not board.game_is_over():
        for possible_move in board.get_empty_cells():
            tmp_board = board.clone()
            tmp_board.play_at(possible_move)

            print("b: \n",tmp_board)
            print("s: ",tmp_board.game_is_over())
            #print("w: ",tmp_board.get_winner()) 
            if tmp_board.game_is_over():
                if tmp_board.get_winner() == "X":
                    best_pos, best_score = possible_move, 1
                elif tmp_board.get_winner() == "O":
                    best_pos, best_score = possible_move, -1
                elif tmp_board.get_winner() == "-":
                    best_pos, best_score = possible_move, 0
            else:    
                pos, score = minimax_move(tmp_board)
                if score > best_score:
                    best_score = score
                    best_pos = pos
            return best_pos, best_score

def recurs_A(board):
    if board.game_is_over():
        print("got to leaf\n{}".format(board))
    else:
        for possible_move in board.get_empty_cells():
            print("InterNode\n{}".format(board))
            tmp_board = board.clone()
            tmp_board.play_at(possible_move)
            print("AfterPlay\n{}".format(tmp_board))
            recurs(tmp_board)

    return("yayay")     



def recurs(board):
    best_score = 0
    best_pos = board.get_empty_cells()[0]
    if not board.game_is_over():
        for possible_move in board.get_empty_cells():
            print("InterNode\n{}".format(board))
            tmp_board = board.clone()
            tmp_board.play_at(possible_move)
            print("AfterPlay\n{}".format(tmp_board))
            if tmp_board.game_is_over():
                print("got to leaf\n{}".format(tmp_board))
                return possible_move, SCORING[tmp_board.get_winner()]
            else:
                pos, score = recurs(tmp_board)
                if score > best_score:
                    best_score = score
                    best_pos = pos
    return best_pos, best_score
# 
def score(board):
    if board.get_winner == "X":
        return 1
    elif board.get_winner == "0":
        return -1
    else:
        return 0

# def minimax(board):
    # if board.get_current_player() == "X":
        # max_score_index = scores.index(max(scores))
        # return moves[max_score_index], scores[max_score_index]
    # if board.get_current_player() == "O":
        # min_score_index = scores.index(min(scores))
        # return moves[min_score_index], scores[min_score_index]


SCORING = {"X":1 , "O":-1, "-":0}
    
def cheated(board):
    if board.game_is_over():
        return board.get_latest_move(), SCORING[board.get_winner()]
    scores = []
    moves = []

    # populat score array
    for possible_move in board.get_empty_cells():
        tmp_board = board.clone()
        tmp_board.play_at(possible_move)
        scores.append(cheated(tmp_board)[1])
        moves.append(possible_move)    
    print(board)
    print(scores)
    print(moves)
    # MINIMAX Calculation
    #re moves[scores.index(max(scores))], scores.index(max(scores))
    if tmp_board.get_current_player() == "X":
        max_score_index = scores.index(max(scores))
        return moves[max_score_index], scores[max_score_index]
    if tmp_board.get_current_player() == "O":
        min_score_index = scores.index(min(scores))
        return moves[min_score_index], scores[min_score_index]

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
# - tree pruning
# - during recursion cache the motifs already seen/computed (look at
#   that YT, mcoding I think, fibonnaci with cached values video)
