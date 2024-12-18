import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

# Import the Question model
from quiz.models import Question

def populate_questions():
    # Clear existing questions
    Question.objects.all().delete()

    # Create a list of questions
    questions = [
        Question(
            text="What is the capital of France?",
            option1="London", 
            option2="Berlin", 
            option3="Paris", 
            option4="Rome", 
            correct_option=3
        ),
        Question(
            text="What is 2 + 2?",
            option1="3", 
            option2="4", 
            option3="5", 
            option4="6", 
            correct_option=2
        ),
        Question(
            text="Which planet is known as the Red Planet?",
            option1="Venus", 
            option2="Jupiter", 
            option3="Mars", 
            option4="Saturn", 
            correct_option=3
        )
    ]

    # Save questions to the database
    for question in questions:
        question.save()

    print(f"{len(questions)} questions have been added to the database.")

if __name__ == '__main__':
    populate_questions()