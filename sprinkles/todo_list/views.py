from django.shortcuts import render
from .models import Todo


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}

    return render(request, 'todo_list/index.html', content)
