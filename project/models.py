from django.db import models
from django.db.models.base import Model

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name


class Resume(models.Model):
    # Fields for Resume model
    pass

class Project(models.Model):
    # Fields for Project model
    pass

