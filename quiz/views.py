from django.shortcuts import render, redirect
from django.views import View
from .models import Question
import random

class QuizView(View):
    def get(self, request):
        # Start a new quiz session
        request.session['total_questions'] = 0
        request.session['correct_answers'] = 0
        request.session['incorrect_answers'] = 0
        
        # Get a random question
        question = Question.objects.order_by('?').first()
        return render(request, 'quiz/quiz.html', {
            'question': question
        })

    def post(self, request):
        # Get the selected question and user's answer
        question_id = request.POST.get('question_id')
        selected_option = request.POST.get('selected_option')
        
        # Retrieve the question
        question = Question.objects.get(id=question_id)
        
        # Update session statistics
        request.session['total_questions'] = request.session.get('total_questions', 0) + 1
        
        # Check if the answer is correct
        is_correct = int(selected_option) == question.correct_option
        
        if is_correct:
            request.session['correct_answers'] = request.session.get('correct_answers', 0) + 1
        else:
            request.session['incorrect_answers'] = request.session.get('incorrect_answers', 0) + 1
        
        # Get a new random question
        next_question = Question.objects.order_by('?').first()
        
        return render(request, 'quiz/quiz.html', {
            'question': next_question,
            'is_correct': is_correct,
            'total_questions': request.session['total_questions'],
            'correct_answers': request.session['correct_answers'],
            'incorrect_answers': request.session['incorrect_answers']
        })