from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
def index(request):
	if request.session.get('word') == None:
		request.session['word'] = []

	return render(request, 'word_app/index.html')


def process(request):
	if request.POST.get('big') == None:
		class2 = ""
	else:
		class2 = request.POST['big']

	display = " - added on " + strftime("%I:%M %p, %b-%d-%Y", localtime())

	added_words = {
		"word": request.POST.get('word'),
		"class1": request.POST.get('color'),
		"class2": class2,
		"display": display
	}
	
	temp = request.session.get('word')
	temp.append(added_words)
	request.session['word'] = temp

	return redirect('/display')	


def display(request):
	return redirect('/')

def clear(request):
	del request.session['word']
	return redirect('/')







