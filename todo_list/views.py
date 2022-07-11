from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskCreateForm, TagCreateForm
from todo_list.models import Task, Tag


def index(request):
    task_list = Task.objects.all()

    context = {
        "task_list": task_list,
    }

    return render(request, "todo_list/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ("content", "deadline", "done", "tag")
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:index")
    template_name = "todo_list/task_confirm_delete.html"


class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagCreateForm
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name", )
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
    template_name = "todo_list/tag_confirm_delete.html"


def complete_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.done:
        task.done = False
    else:
        task.done = True

    task.save()

    return HttpResponseRedirect(reverse_lazy("todo_list:index"))
