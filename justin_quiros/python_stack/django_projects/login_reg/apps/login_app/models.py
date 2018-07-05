from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

	def register_validation(self, form_data):
		errors = []

		if len(form_data['first_name']) == 0:
			errors.append( "First name is required.") 
		if len(form_data['last_name']) == 0:
			errors.append("Last name is required")
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
			first_name = form_data['first_name'],
			last_name = form_data['last_name'],
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
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __unicode__(self):
		return "id: " + str(self.id) + ", first_name: " + self.first_name + ", last_name: " + self.last_name + ", email:" + self.email + ", password:" + self.password
