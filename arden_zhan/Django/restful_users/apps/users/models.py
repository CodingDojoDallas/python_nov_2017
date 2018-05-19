# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name needs to be 2 or more characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name needs to be 2 or more characters'

        #checks email format and if dupe
        if not 'email' in errors and not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email!'
        else:
            if len(self.filter(email = postData['email'])) > 1:
                errors['email'] = 'Email already in use!'

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()


