from django.shortcuts import render
from .models import Flashcard
import random

def quiz_view(request):
    if request.method == 'POST':
        selected_option = request.POST.get('option')
        correct_answer = request.POST.get('correct_answer')
        is_correct = selected_option == correct_answer
        return render(request, 'flashcards/result.html', {
            'selected_option': selected_option,
            'correct_answer': correct_answer,
            'is_correct': is_correct,
        })

    flashcards = list(Flashcard.objects.all())
    if flashcards:
        card = random.choice(flashcards)
        options = [
            card.correct_answer,
            card.wrong_answer_1,
            card.wrong_answer_2,
            card.wrong_answer_3,
        ]
        random.shuffle(options)
        return render(request, 'flashcards/quiz.html', {
            'card': card,
            'options': options
        })

    return render(request, 'flashcards/quiz.html', {'card': None})
