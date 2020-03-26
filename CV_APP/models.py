from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.


class Education(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    school = models.CharField(max_length=100)
    descipline = models.CharField(max_length=100)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)


class Work_experience(models.Model):
    start = models.DateField()
    end = models.DateField()
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    userid = models.ForeignKey(User, on_delete=models.CASCADE)


class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    userid = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    userid = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media', blank=True)
    img_name = state = models.CharField(max_length=1000, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    skills = models.TextField()
    hobbies = models.TextField(blank=True)
    references = models.TextField(blank=True)
