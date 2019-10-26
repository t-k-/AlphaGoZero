import time
import os
import pandas as pd
from tqdm import tqdm

from game import Game
from agent import Player
from constants import *
from train import *
from sys import platform
if platform == 'linux'
	from evaluator import *
# from data import *

print(DEVICE)

alphazero = Player()
simulator = Game(alphazero, mctsEnable=True)

dataset = pd.DataFrame({
			"States": [],
			"Actions": [],
			"ActionScores": [],
			"Rewards": [],
			"Done": []})

for i in tqdm(range(GAMES)):
	df = simulator.play()

	dataset = dataset.append(df)

# print(evaluate(alphazero, alphazero))

dataset.to_pickle('dataset.pkl')
dataset.to_csv('dataset.csv')
# train_data = dataset[:train_percentage*len(dataset)]
# data_loader = torch.utils.data.DataLoader(train_data, ...)
# train(data_loader, alphazero)