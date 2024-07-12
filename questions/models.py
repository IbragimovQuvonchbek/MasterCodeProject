from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.category


class Question(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    questions = models.TextField(blank=False)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
