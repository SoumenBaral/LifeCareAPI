from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Specialization(models.Model):
    name = models.CharField(max_length = 40)
    slug = models.SlugField(max_length = 40)




    def __str__(self) -> str:
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length = 40)
    slug = models.SlugField(max_length = 40)

    def __str__(self) -> str:
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length = 100)


    def __str__(self) -> str:
        return self.name

class Doctor (models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    image = models.ImageField(upload_to='doctor/images')
    specialization = models.ManyToManyField(Specialization)
    designation = models.ManyToManyField(Designation)
    availableTime = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length = 200)
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

