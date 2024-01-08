from django.db import models
from django.contrib.auth.models import User


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
