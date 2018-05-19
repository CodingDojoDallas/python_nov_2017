# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['name']) <= 5:
            errors['name'] = 'Course name needs to be more than 5 characters'
        return errors

class DescManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['desc']) <= 15:
            errors['desc'] = 'Course description needs to be more than 15 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

class Desc(models.Model):
    content = models.TextField()
    course = models.OneToOneField(Course, related_name = 'desc')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = DescManager()