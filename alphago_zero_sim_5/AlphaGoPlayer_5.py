import numpy as np
from utils_5.constants import *
from utils_5.go import GoEnv as Board
import pandas as pd
from utils_5.mcts import MCTS
from sys import maxsize
import time 
from utils_5.agent import Player

class AlphaGoPlayer():
    def __init__(self, init_state, seed, player_color):
        self.board = Board("black", BOARD_SIZE)
        self.state = self.board.reset()
        self.player_color = player_color
        self.player = Player().to(DEVICE)
        self.player.load_state_dict(torch.load(BEST_PATH))
        self.player.eval()
        self.done = False
        self.mcts = MCTS()
        self.mcts.TuliSharmaOptimization(self.player, self.board, True)
        # self.mcts.runSims(self.board, self.player, 100, 3)

    def playOnce(self, other_pass):
        if other_pass and self.board.get_winner() + 1 == self.board.player_color:
            action = 169
        else: 
            action, action_scores = self.mcts.play(self.board, self.player, True, mcts_time=4.6)
        self.state, _, self.done = self.board.step(action)
        return action

    def get_action(self, cur_state, opponent_action):
        startTime = time.time()
        # print('--------------START--------------')
        if opponent_action != -1:
            # print("opponent_action ", opponent_action)
            self.mcts.advance(opponent_action)
            self.state, _, self.done = self.board.step(opponent_action)
            # self.board.render()
        if self.done:
            return 169 # pass
        action = self.playOnce(opponent_action == 169)
        # print("my action ", action)
        # self.board.render()
        print('-------------- END --------------', time.time() - startTime, action)
        return action
