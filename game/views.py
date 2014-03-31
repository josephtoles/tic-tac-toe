from django.shortcuts import render

def new_game(request):
	for i in range(1,10):
		if 'g'+str(i) in request.session:
			del request.session['g'+str(i)]
	request.session['newgame'] = True
	return render(request, 'new-game.html', request.session)

def select_player(request):
	errors = []
	if 'color' in request.GET:
		color = request.GET['color']
		request.session['color'] = color
		return render(request, 'home.html', request.session)
	else:
		errors.append('No colors selected.')

def move(request):
	if 'move' in request.GET:
		print 'move found'
		print str(request.GET)
		new_position = request.GET['move']
		request.session[new_position] = request.session['color']
		request.session[request.GET['move']] = request.session['color']
	else:
		print 'no move found'
	return render(request, 'home.html', request.session)

def home(request):
	return render(request, 'home.html', request.session)
