from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
class Flashcard(models.Model):
  question = models.TextField()
  correct_answer = models.CharField(max_length=255)
  wrong_answer_1 = models.CharField(max_length=255)
  wrong_answer_2 = models.CharField(max_length=255)
  wrong_answer_3 = models.CharField(max_length=255)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.question


# Create your models here.
