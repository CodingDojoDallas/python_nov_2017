from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return "id: " + str(self.id) + ", first_name: " + self.first_name + ", last_name " + self.last_name + ", email " + self.email