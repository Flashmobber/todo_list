from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskCreateForm
from todo_list.models import Task, Tag


def index(request):
    task_list = Task.objects.all()

    context = {
        "task_list": task_list,
    }

    return render(request, "todo_list/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo_list:task_list")


class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"
