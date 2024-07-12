from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=False, unique=True)
    username = models.CharField(max_length=32, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.username
