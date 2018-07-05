from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

	def register_validation(self, form_data):
		errors = []

		if len(form_data['name']) == 0:
			errors.append( "Name is required.") 
		if len(form_data['alias']) == 0:
			errors.append("Alias is required")
		if len(form_data['email']) == 0 or not EMAIL_REGEX.match(form_data['email']):
			errors.append("Email is invalid.")
		if len(form_data['password']) < 8:
			errors.append("Email must be atleast 8 characters.")
		if form_data['password'] != form_data['conf_password']:
			errors.append("Passwords did not match.")
		
		duplicate = User.objects.filter(email = form_data['email'])
		if len(duplicate) == 1:
			errors.append("This email is already registered.")

		return errors



	def register(self, form_data):
		pw = str(form_data['password'])
		hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())

		user = User.objects.create(
			name = form_data['name'],
			alias = form_data['alias'],
			email = form_data['email'],
			password = hashed_pw
		)
		return user

	def login_validation(self, form_data):
		errors = []
		user = User.objects.filter(email=form_data['email']).first()
		print user
		if user:
			pw = str(form_data['password'])
			user_password = str(user.password)
			if not bcrypt.checkpw(pw.encode(), user_password.encode()):
				errors.append("Invalid password.")
		else:
			errors.append("Invalid email.")
		return errors


	def login(self, form_data):
		user = User.objects.filter(email=form_data['email']).first()
		return user






class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()


class Author(models.Model):
	name = models.CharField(max_length=255)

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(Author, related_name="books")







class ReviewManager(models.Manager):
	def review_validation(self, form_data):
		errors = []

		if len(form_data['title']) < 1 or len(form_data['review']) < 1:
			errors.append('Title/Review fields are required')
		if not "author" in form_data and len(form_data['new_author']) < 3:
			errors.append('Author names must be atleast 3 letters.')

		if "author" in form_data and len(form_data['new_author']) > 0 and len(form_data['new_author']) < 3:
			errors.append('Author names must be atleast 3 letters.')
		if not int(form_data['rating']) > 0 or not int(form_data['rating']) <= 5:
			errors.append('invalid rating')
		return errors

	def create_review(self, form_data, user_id):

        # retrive or create author
		the_author = None
		if len(form_data['new_author']) < 1:
			the_author = Author.objects.get(id=int(form_data['author']))
		else:
			the_author = Author.objects.create(name=form_data['new_author'])

        # retirive or create book
		the_book = None
		if not Book.objects.filter(title=form_data['title']):
			the_book = Book.objects.create(
		    title=form_data['title'], author=the_author
		)
		else:
 			the_book = Book.objects.get(title=form_data['title'])

        # returns a Review object
		return self.create(
		review = form_data['review'],
		rating = form_data['rating'],
		book = the_book,
		reviewer = User.objects.get(id=user_id)
		)

	def recent_and_not(self):

        # returns a tuple with the zeroeth index containing query for 3 most recent reviews, and the first index
        # containing the rest

		return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])

class Review(models.Model):
	review = models.TextField()
	rating = models.IntegerField()
	book = models.ForeignKey(Book, related_name="reviews")
	reviewer = models.ForeignKey(User, related_name="reviews_left")
	created_at = models.DateTimeField(auto_now_add=True)
	objects = ReviewManager()
	def __str__(self):
		return "Book: {}".format(self.book.title)