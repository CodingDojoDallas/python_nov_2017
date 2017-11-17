from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):

	def course_validation(self, form_data):
		errors = {}


		if len(form_data['name']) == 0:
			errors['name'] = "Course name is required."

		if len(form_data['name']) < 5:
			errors['name'] = "Course name must be atleast 5 characters."

		if len(form_data['desc']) < 15:
			errors['desc'] = "Course description must be atleast 15 characters."


		# if len(form_data['name']) == 0:
		# 	errors.append('Course name is required.')

		# if len(form_data['name']) < 5:
		# 	errors.append('Course name must be atleast 5 characters.')

		# if len(form_data['desc']) < 15:
		# 	errors.append('Course description must be atleast 15 characters.')

		return errors



class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = CourseManager()

	def __unicode__(self):
		return "id: " + str(self.id) + ", name: " + self.name + ", desc: " + self.desc