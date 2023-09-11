from django.db import models

# Create your models here.

class Lesson(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTION_TYPES = (
        ('single', 'Single Answer'),
        ('multi', 'Multi Answer'),
    )
    text = models.TextField()
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text