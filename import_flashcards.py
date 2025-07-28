# scripts/import_flashcards.py
import json
import os
import django

# Configurar entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from flashcards.models import Category, Flashcard  # Asegurate de importar correctamente

with open('flashcards_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    category_name = item['category']
    category, _ = Category.objects.get_or_create(name=category_name)

    Flashcard.objects.create(
        question=item['question'],
        correct_answer=item['correct_answer'],
        wrong_answer_1=item['wrong_answer_1'],
        wrong_answer_2=item['wrong_answer_2'],
        wrong_answer_3=item['wrong_answer_3'],
        category=category
    )

print("¡Importación completa!")
