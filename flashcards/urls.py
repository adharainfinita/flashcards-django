from django.urls import path
from .views import quiz_view, reset_quiz

urlpatterns = [
  path('', quiz_view, name='quiz'),
  path('reset/', reset_quiz, name='reset_quiz'),
]