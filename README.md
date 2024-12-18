# Django Quiz App

## Project Overview
This is a simple Django-based quiz application that allows users to answer random multiple-choice questions and track their performance.

## Prerequisites
- Python 3.8+
- Django 3.2+
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Tanmaya04/quizapp.git
cd quizapp
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Populate Questions
```bash
python populate_questions.py
```

### 6. Run the Application
```bash
python manage.py runserver
```

## Project Structure
- `quiz/` - Main app directory
  - `models.py` - Database models for questions
  - `views.py` - Application logic
  - `templates/` - HTML templates
- `quiz_project/` - Project configuration
  - `settings.py` - Django project settings
  - `urls.py` - URL routing

## Notes
- Questions are predefined in the database
- No user authentication is implemented
- Questions are selected randomly
- Simple scoring mechanism tracks total, correct, and incorrect answers

## Future Improvements
- Add more questions
- Implement user authentication
- Add difficulty levels
- Improve UI/UX
- Add error handling
