from django.shortcuts import render
from board import Board

def new_game(request):
	request.session['board'] = Board()
	return render(request, 'new-game.html', request.session)

def select_player(request):
	errors = []
	if 'color' in request.GET:
		color = request.GET['color']
		request.session['color'] = color
		if color == 'O':
			newboard = Board()
			newboard.move_random()
			request.session['board'] = newboard
		return render(request, 'home.html', request.session)

def move(request):
	if 'move' in request.GET:
		newboard = request.session['board']
		command = int(request.GET['move'])
		success = newboard.place_at(command-1)
		if success:
			newboard.move_optimal()
		request.session['board'] = newboard
	return render(request, 'home.html', request.session)

def home(request):
	return render(request, 'home.html', request.session)

