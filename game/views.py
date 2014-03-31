from django.shortcuts import render

#request.session variables
#1-8 grid board positions
#player 'x', 'y', ' '

def new_game(request):
	for i in range(1,8):
		request.session[i] = i
	request.session['newgame'] = True
	return render(request, 'new-game.html', request.session)

def select_player(request):
	errors = []
	print str(request.GET)
	if 'color' in request.GET:
		color = request.GET['color']
		print request.GET['color']
		request.session['color'] = color
		return render(request, 'home.html', request.session)
	else:
		errors.append('No colors selected.')

def home(request):
	return render(request, 'home.html', request.session)
