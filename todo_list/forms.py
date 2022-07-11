from django import forms
import django.utils.timezone

from todo_list.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    deadline = django.utils.timezone.now

    class Meta:
        model = Task
        fields = ["content", "deadline", "done", "tag"]


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "done", "tag"]


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class TagUpdateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
