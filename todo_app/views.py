from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def index(request):
    form = TaskForm()
    tasks = [task for task in Task.objects.all()]

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'form': form, 'tasks': tasks}
    return render(request, 'todo_app/index.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'todo_app/update_task.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {'task': task}
    return render(request, 'todo_app/delete_task.html', context)
