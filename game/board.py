#!/usr/bin/env python

# For this program I call X/O 'color' because players in
# board games are usually distinguished by colors.

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
			return
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
