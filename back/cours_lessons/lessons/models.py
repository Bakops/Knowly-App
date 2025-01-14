# lessons/models.py
from django.db import models
from ..cours.models import Course

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
