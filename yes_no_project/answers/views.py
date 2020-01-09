import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from answers.models import Answer


# Create your views here.
def answer_views(requests):
    answers = Answer.objects.all()
    answer = random.choice(answers)

    return render(requests, 'answer.html', context={'answer': answer})


def create_answer_views(request):
    if request.method == 'GET':
        return render(request, 'create_answer.html')

    if request.method == 'POST':
        if request.POST['text'] and request.POST['image']:
            Answer.objects.create(
                text=request.POST['text'],
                image=request.POST['image']
            )
        return redirect('answer_views_url')


class CreateAnswerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'create_answer.html')

    def post(self, request, *args, **kwargs):
        if request.POST['text'] and request.POST['image']:
            Answer.objects.create(
                text=request.POST['text'],
                image=request.POST['image']
            )
            return redirect('answer_views_url')
