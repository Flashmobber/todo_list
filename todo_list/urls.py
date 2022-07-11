from django.urls import path

from .views import TagListView, index, TaskListView, TaskCreateView

urlpatterns = [
    path("", index, name="index"),
    path("tag/", TagListView.as_view(), name="tag_list"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "todo_list"