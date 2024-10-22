from django.db import models
from django.utils import timezone


class Customer(models.Model):
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=75)
    lastname = models.CharField(max_length=75)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return f"{self.full_name}: {self.username} {self.email}"


class Post(models.Model):
    text = models.TextField(max_length=200)
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.author}: {self.text}"
