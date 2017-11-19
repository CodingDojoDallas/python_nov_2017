from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
	request.session['status'] = ""
	if 'errors' not in request.session:
		request.session['errors'] = []
	context = {
	"errors": request.session['errors']
	}
	return render(request, 'review_app/index.html', context)

def register(request):
	if request.method == "POST":
		errors = User.objects.register_validation(request.POST)
		if len(errors) != 0:
			request.session['errors'] = errors
			print errors
			return redirect('/')
		else:
			user = User.objects.register(request.POST)
			request.session['user_id'] = user.id
			request.session['status'] = "registered."
			request.session['name'] = user.name
			return redirect('/books')

def login(request):
	errors = User.objects.login_validation(request.POST)
	if len(errors) != 0:
		request.session['errors'] = errors
		return redirect('/')
	else:
		user = User.objects.login(request.POST)
		request.session['name'] = user.name
		request.session['user_id'] = user.id
		request.session['status'] = "logged in."
		return redirect('/books')

def books(request):
	context = {
	'recent': Review.objects.recent_and_not()[0],
	'more': Review.objects.recent_and_not()[1]
	}
	return render(request, 'review_app/books.html', context)

def add(request):
	context = {
	"authors": Author.objects.all()
	}
	return render(request, 'review_app/add.html', context)

def add_review(request, book_id):
	book = Book.objects.get(id=book_id)
	new_review = {
	"title": book.title,
	"author": book.author.id,
	"rating": request.POST['rating'],
	"review": request.POST['review'],
	"new_author": ''
	}

	errors = Review.objects.review_validation(new_review)
	if errors:
		for e in errors:
			messages.error(request, e)
	else:
		Review.objects.create_review(new_review, request.session['user_id'])
	return redirect('/books/{}'.format(book_id))

def create(request):
	error = Review.objects.review_validation(request.POST)
	if error:
		for e in error:
			messages.error(request, e)
	else:
		book_id = Review.objects.create_review(request.POST, request.session['user_id']).book.id
	return redirect('/books/{}'.format(book_id))

def review(request, book_id):
	context = {
	"book": Book.objects.get(id=book_id)
	}
	return render(request, 'review_app/review.html', context)

def user(request, user_id):

	user = User.objects.get(id=user_id)
	print user
	unique_ids = user.reviews_left.all().values("book").distinct()
	unique_books = []
	for book in unique_ids:
		unique_books.append(Book.objects.get(id=book['book']))
	context = {
		'user': user,
		'unique_book_reviews': unique_books
	}
	return render(request, 'review_app/user.html', context)

def delete(request, review_id):
	book_id = Review.objects.get(id=review_id).book_id
	Review.objects.get(id=review_id).delete()
	return redirect('/books/{}'.format(book_id))

def logout(request):
	request.session.clear()
	return redirect('/')