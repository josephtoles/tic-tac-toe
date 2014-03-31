#!/usr/bin/env python

# For this program I call X/O 'color' because players in
# board games are usually distinguished by colors.

import random

class Board:
	def __init__(self):
		#positions numbered [0,8]
		#positions contain None, 'X' or 'O'
		self.grid = [None]*9
		self.turn_index = 1
	
	#returns color of the character
	def current_player(self):
		if self.turn_index % 2 == 1:
			return 'X'
		return 'O'

	def opposing_player(self):
		if self.current_player() == 'X':
			return 'O'
		return 'X'

	#returns boolean representing success
	def place_at(self, loc):
		if self.game_over():
			return False
		if type(loc) != int:
			return False
		if loc < 0 or loc > 8:
			return False
		if self.grid[loc] != None:
			return False
		self.grid[loc] = self.current_player()
		self.turn_index += 1
		return True
	
	#returns winner, False otherwise
	def game_over(self):
		if self.turn_index >= 10:
			return 'draw'
		#columns
		for i in range(0,3):
			temp = self.grid[i]
			if temp != None and temp == self.grid[i+3] and temp == self.grid[i+6]:
				return temp
		#rows
		for i in range(0,3):
			temp = self.grid[i*3]
			if temp != None and temp == self.grid[i*3+1] and temp == self.grid[i*3+2]:
				return temp
		#diagonal
		temp = self.grid[0]
		if temp != None and temp == self.grid[4] and temp == self.grid[8]:
			return temp
		temp = self.grid[2]
		if temp != None and temp == self.grid[4] and temp == self.grid[6]:
			return temp

	#for testing purposes only
	def to_string(self):
		output = ''
		for i in range(0,9):
			if self.grid[i] == None:
				output += '_'
			else:
				output += self.grid[i]
			if i == 2 or i == 5:
				output = output+'\n'
		return output

	def move_random(self):
		if self.game_over():
			return False
		success = False
		while not success:
			index = random.randrange(9)
			success = self.place_at(index)

	def move_optimal(self):
		if self.game_over():
			return False
		#simple heuristic
		if self.turn_index == 2 or self.turn_index == 3:
			success = self.place_at(4)
			while not success:
				success = self.place_at(random.randrange(1)*2+random.randrange(1)*6)
			return
		options = []
		for i in range(0,9):
			b = self.copy()
			legal = b.place_at(i)
			if not legal:
				options.append('illegal')
			else:
				result = b.test()
				options.append(result)
				if result == self.current_player():
					self.place_at(i)
					return
		for i in range(0,9):
			if options[i] == 'draw':
				self.place_at(i)
				return
		self.move_random()

	def copy(self):
		copy = Board()
		copy.grid = []
		for i in range(0,9):
			copy.grid.append(self.grid[i])
		copy.turn_index = self.turn_index
		return copy

	#returns winner under perfect play
	def test(self):
		options = []
		for i in range(0,9):
			test = self.copy()
			legal = test.place_at(i)
			if not legal:
				options.append('illegal')
				continue
			winner = test.game_over()
			if winner:
				options.append(winner)
				continue
			options.append(test.test())
		if self.current_player() in options:
			return self.current_player()
		if 'draw' in options:
			return 'draw'
		return self.opposing_player()
		
