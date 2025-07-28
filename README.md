# 🧠 Django Flashcards Quiz App

Una aplicación web desarrollada con Django para practicar preguntas y respuestas estilo flashcards y quiz.

## 🚀 Requisitos

- Python 3.10 o superior
- pip
- Git (opcional, pero recomendado)
- Entorno virtual (recomendado)

## 📦 Instalación del proyecto (pasos para clonar en otra máquina)

1. **Clonar el repositorio**

```
git clone https://github.com/tu-usuario/flashcards-quiz.git
cd flashcards-quiz
```

Crear y activar el entorno virtual

En Linux/macOS:

```
python3 -m venv env
source env/bin/activate
```

En Windows:

```
python -m venv env
env\Scripts\activate
```

Instalar dependencias

```
pip install -r requirements.txt
```

Aplicar migraciones
```
python manage.py migrate
```

Crear superusuario (opcional, para usar el admin)

```
python manage.py createsuperuser
```

Ejecutar el servidor

```
python manage.py runserver
```

Abrí tu navegador en http://127.0.0.1:8000 para ver la aplicación funcionando.

## 🛠 Estructura del proyecto
flashcards/ → Contiene las apps del proyecto

templates/ → HTMLs (si los agregás)

requirements.txt → Lista de paquetes del proyecto

manage.py → Comando principal de Django

## ✅ Funcionalidades
Panel de administración para cargar preguntas y respuestas

Separación por temas o categorías

Posibilidad de implementar quizzes interactivos (en desarrollo)

## 🔐 Acceso al panel de admin
http://127.0.0.1:8000/admin/
Usá el superusuario creado previamente para ingresar.

📄 Licencia
Este proyecto es de uso libre para fines educativos o personales.




