##### Belt Exam - Home App
##### Mason Brewer
##### November 19th, 2018

from __future__ import unicode_literals
from django.db import models
# import re, bcrypt
    
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class JobManager(models.Manager):
    def jobValidator(self, postData, allCats):
        errors = {}
        if len(postData["title"]) < 3:
            errors["title"] = "Title should be at least 3 characters."
        if len(postData["description"]) < 3:
            errors["description"] = "Description should be at least 3 characters."
        if len(postData["location"]) < 3:
            errors["location"] = "Location should be at least 3 characters."
        if len(allCats) < 3:
            errors["categories"] = "Must enter a valid category."
        return errors

class Job(models.Model):
    title = models.CharField(max_length = 255)
    decription = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)
    catergories = models.CharField(max_length = 255)
    poster = models.ForeignKey("loginApp.User", related_name="poster")
    volunteer = models.ForeignKey("loginApp.User", related_name="volunteer", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()
