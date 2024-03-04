#!/usr/bin/python3

# b is a Board instance from TTT.py
from minimax import cheated

def test_basic_fct(b):
    Xwin = [(1,1), (0,1), (0,2), (1,2), (2,2), (1,0),(2,0)]
    Owin = [(1,1), (0,1), (1,0), (0,0), (2,1), (0,2)]
    draw = [(1,1), (0,1), (2,0),(0,2), (1,2), (2,2), (0,0),(1,0),(2,1)]
    for move in Xwin:
        b.play_at(move)
    b.reset()

    for move in Owin:
        b.play_at(move)
    b.reset()
    
    for move in draw:
        b.play_at(move)
    b.reset()
    
def test_random_games(b, iter_num):
    results = []
    for i in range(iter_num):
        b.random_play()
        results.append(b.get_winner())
        b.reset()
    display_stats(results)

def test_minimax_games(b, iter_num):
    results = []
    for i in range(iter_num):
        while not b.game_is_over():
            mmmove = cheated(b)[0]
            print("###\n{} playing at {}".format(b.get_current_player(), mmmove))
            b.play_at(mmmove)
            print(b)
        results.append(b.get_winner())
        #b.reset()
    display_stats(results)

def test_monte_carlo_games(b,iter_num):
    results = []
    for i in range(iter_num):
        b.montecarlo_vs_montecarlo()
        results.append(b.get_winner())
        b.reset()
    display_stats(results)

def display_stats(results):
    assert results != [], "No results"
    print("\n~~~~~~~~~~~~~~~\n- TTT RESULTS -\n~~~~~~~~~~~~~~~\n- number of runs : {}\n".format(len(results)))	
    print("X win : {}".format("#"*results.count("X")))
    print("O win : {}".format("#"*results.count("O")))
    print("Draw  : {}".format("#"*results.count("-")))

def test_board_loading(b):
    states = ["--- -X- ---","X-- --- ---","XXO OOX ---","XX- OOO XOX"]
    for state in states:
        b.reset()
        b.load(state)
        print(b, "++++++\n")
