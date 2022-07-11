from django import forms
import django.utils.timezone

from todo_list.models import Task


class TaskCreateForm(forms.ModelForm):
    deadline = django.utils.timezone.timedelta(14)

    class Meta:
        model = Task
        fields = ["content", "deadline", "done", "tag"]
