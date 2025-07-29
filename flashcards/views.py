from django.shortcuts import render, redirect
from .models import Flashcard
import random

def quiz_view(request):
    # Inicializar la sesión
    if 'answered' not in request.session:
        request.session['answered'] = 0
        request.session['correct'] = 0
        request.session['seen_ids'] = []

    total_questions = Flashcard.objects.count()

    if request.method == 'POST':
        selected_option = request.POST.get('option')
        correct_answer = request.POST.get('correct_answer')

        request.session['answered'] += 1
        is_correct = selected_option == correct_answer
        if is_correct:
            request.session['correct'] += 1

        request.session.modified = True

        correct = request.session['correct']
        percent = int((correct / total_questions) * 100) if total_questions > 0 else 0

        # Mostrar página de resultado con progreso
        return render(request, 'flashcards/result.html', {
            'is_correct': is_correct,
            'correct_answer': correct_answer,
            'answered': request.session['answered'],
            'correct': correct,
            'total_questions': total_questions,
            'progress_percent': percent,
        })

    # Obtener tarjetas no vistas
    seen_ids = request.session.get('seen_ids', [])
    cards = Flashcard.objects.exclude(id__in=seen_ids)

    if not cards.exists():
        # No quedan tarjetas por mostrar, mostrar resumen final
        return render(request, 'flashcards/quiz.html', {
            'card': None,
            'answered': request.session['answered'],
            'correct': request.session['correct'],
            'total_questions': total_questions,
            'progress_percent': 100,
        })

    # Elegir una tarjeta aleatoria
    card = random.choice(cards)
    options = [
        card.correct_answer,
        card.wrong_answer_1,
        card.wrong_answer_2,
        card.wrong_answer_3,
    ]
    random.shuffle(options)

    # Registrar como vista la tarjeta actual
    request.session['seen_ids'].append(card.id)
    request.session.modified = True

    correct = request.session['correct']
    percent = int((correct / total_questions) * 100) if total_questions > 0 else 0

    return render(request, 'flashcards/quiz.html', {
        'card': card,
        'options': options,
        'answered': request.session['answered'],
        'correct': correct,
        'total_questions': total_questions,
        'progress_percent': percent,
    })

def reset_quiz(request):
    # Reiniciar progreso borrando la sesión
    request.session.flush()
    return redirect('quiz')
