from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task


# inheriting from above import ListView


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = 'base/task_detail.html'


class TaskCreate(CreateView):
    model = Task
    # creates model form, takes all fields from model - class Task(
    # models.Model)
    fields = '__all__'
    success_url = reverse_lazy('tasks')
