#! /usr/bin/python3

from random import choice
from minimax import nim_minimax

class Nim():
    """
    Plays game of Nim 
    stack : the number of counter
    human_player : the number of human players, if 0 play against itself
    algo : random, montecarlo, minimax
    """
    
    def __init__(self, stack = 6, algo = "random"):
        self._stack = stack
        self._algo = algo
        self._playing = 1
        self._max_remove = 3
        # needed for minimax
        self._winner = -1
        self._maximising = True


    def __str__(self):
        msg  = "\nRemaining : {}".format(self._stack)
        msg += "{}".format("|" * self._stack)
        msg += "\n\nNow playing is player {}".format(self._playing)
        return msg

    def get_choices(self):
        if self._stack >= self._max_remove:
            return list(range(1, self._max_remove+1))
        elif self._stack < self._max_remove:
            return list(range(1, self._stack+1))
        
    def switch_player(self):
        assert self._playing in [1,2], "Invalid player"
        self._playing = 2 if self._playing == 1 else 1
        self._maximising = False if self._maximising == True else True

    def remove_from_stack(self, n):
        assert n > 0 and n <= self.get_choices()[-1], "Can't remove that much {}".format(n)
        self._stack -= n
        print("{} counters were removed".format(n))
        self.switch_player()        
        if self.is_game_over():
            self._winner = self._playing
        else:
            print(self)

    def is_game_over(self):
        if self._stack == 0:
            return True

    def get_winner(self):
        return self._winner
    
    def player_maximising(self):
        return self._maximising
    
    def prompt(self, player):
        if player == "hum":
            n = input("Please choose a number between 1 and {}\n".format(self.get_choices()[-1]))
            n = int(n.rstrip())
            self.remove_from_stack(n)
        elif player == "ai":
            if self._algo == "random":
                self.remove_from_stack(choice(self.get_choices()))

    def prompt_game_over(self):
        print("\nGame Over : the winner is P{}".format(self._winner))

    def play_a_game(self, h_player):
        # human vs human
        if h_player == 2:
            while not self.is_game_over():
                self.prompt("hum")
        # cpu vs cpu
        elif h_player == 0:
            while not self.is_game_over():
                self.prompt("ai")
        # human vs cpu
        elif h_player == 1:
            while True:
                if self.is_game_over():
                    break
                self.prompt("hum")
                if self.is_game_over():
                    break
                self.prompt("ai")
        self.prompt_game_over()


if __name__ == "__main__":
    n = Nim()
    n.play_a_game(1)

# todo 
# dans play_a_game bien passer le player en arg et check qui joue qui prompter






















