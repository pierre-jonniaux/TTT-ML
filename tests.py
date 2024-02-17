#!/usr/bin/python3

# b is a Board instance from TTT.py

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

def display_stats(results):
	assert results != [], "No results"
	print("\n~~~~~~~~~~~~~~~\n- TTT RESULTS -\n~~~~~~~~~~~~~~~\n- number of runs : {}\n".format(len(results)))	
	print("X win : {}".format("#"*results.count("X")))
	print("O win : {}".format("#"*results.count("O")))
	print("Draw  : {}".format("#"*results.count("-")))
