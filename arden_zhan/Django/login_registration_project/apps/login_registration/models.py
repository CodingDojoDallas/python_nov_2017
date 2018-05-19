# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validateReg(self, postData):
        errors = {}
        
        #first/last name at least 2 characters, letters only
        if len(postData['first_name']) < 2 or postData['first_name'].isalpha() == False:
            errors['first_name'] = 'First name needs to be at least 2 characters, letters only'
        if len(postData['last_name']) < 2 or postData['last_name'].isalpha() == False:
            errors['last_name'] = 'Last name needs to be at least 2 characters, letters only'

        #checks email format and if dupe
        if not 'email' in errors and not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email!'
        else:
            if len(self.filter(email = postData['email'])) > 0:
                errors['email'] = 'Email already in use!'

        #password at least 8 characters, matches confirm
        if len(postData['password']) < 8 or postData['password_confirm'] != postData['password']:
            errors['password'] = "Password needs to be at least 8 characters; matches confirmed password"

        #NO ERRORS -> MAKE NEW USER and HASHED PW
        if not errors:
            hashed = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt())
            new_user = self.create(
                first_name = postData['first_name'],
                last_name = postData['last_name'],
                email = postData['email'],
                password = hashed,
            )
            return new_user

        return errors

    def validateLogin(self, postData):
        errors = {}
        
        #checks if email exists
        if len(self.filter(email = postData['email'])) != 0:
            user = self.filter(email = postData['email'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "invalid email/password"

        else: #list is len 0 so email doesn't exist
            errors['email'] = "invalid email/password"
        
        if not errors:
            return user
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()


