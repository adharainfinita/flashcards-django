from django.shortcuts import render, redirect
from .models import Flashcard
from django.views.decorators.http import require_POST
import random

def quiz_view(request):
    # Inicializar la sesión
    if 'answered' not in request.session:
        request.session['answered'] = 0
        request.session['correct'] = 0
        request.session['seen_ids'] = []

    if request.method == 'POST':
        selected_option = request.POST.get('option')
        correct_answer = request.POST.get('correct_answer')

        request.session['answered'] += 1
        is_correct = selected_option == correct_answer
        if is_correct:
            request.session['correct'] += 1

        request.session.modified = True

        # Mostrar página de resultado
        return render(request, 'flashcards/result.html', {
            'is_correct': is_correct,
            'correct_answer': correct_answer,
        })

    # Obtener tarjetas no vistas
    seen_ids = request.session.get('seen_ids', [])
    cards = Flashcard.objects.exclude(id__in=seen_ids)

    if not cards.exists():
        return render(request, 'flashcards/quiz.html', {
            'card': None,
            'answered': request.session['answered'],
            'correct': request.session['correct'],
        })

    # Elegir una aleatoria
    card = random.choice(cards)
    options = [
        card.correct_answer,
        card.wrong_answer_1,
        card.wrong_answer_2,
        card.wrong_answer_3,
    ]
    random.shuffle(options)

    # Registrar como mostrada
    request.session['seen_ids'].append(card.id)
    request.session.modified = True

    return render(request, 'flashcards/quiz.html', {
        'card': card,
        'options': options,
        'answered': request.session['answered'],
        'correct': request.session['correct'],
    })

def reset_quiz(request):
    request.session.flush()  # Borra el progreso
    
    return redirect('quiz') 