from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.


class Education(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    school = models.CharField(max_length=100)
    descipline = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Work_experience(models.Model):
    start = models.DateField()
    end = models.DateField()
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    image = CloudinaryField()
    nationality = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    skills = models.TextField()
    hobbles = models.TextField()
    references = models.TextField()
