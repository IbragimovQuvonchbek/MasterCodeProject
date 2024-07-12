from django.db import models
from client.models import Client
from questions.models import Question


class ResultQuestions(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_solved = models.BooleanField(default=False)
    is_correct = models.BooleanField(default=False)
    solution = models.TextField(default=None)

    def __str__(self):
        return self.client.__str__()
