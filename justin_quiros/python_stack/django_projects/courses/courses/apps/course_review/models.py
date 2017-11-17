from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return "id: " + str(self.id) + ", name: " + self.name + ", desc: " + self.desc