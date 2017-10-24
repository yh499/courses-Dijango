from __future__ import unicode_literals
from django.db import models


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Name should be more than 5 characters"
        if len(postData['des']) < 10:
            errors["des"] = "Description desc should be more than 10 characters"
        return errors

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    des = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    objects = CourseManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "object: name,{} des,{}, date,{}".format(self.name, self.des, self.created_at)