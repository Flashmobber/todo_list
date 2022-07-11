from django.urls import path

from .views import TagListView, index, TaskListView, TaskCreateView, \
    complete_task, TaskUpdateView, TaskDeleteView, TagUpdateView, \
    TagCreateView, TagDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(),
         name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(),
         name="tag-delete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(),
         name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(),
         name="task-delete"),
    path("tasks/<int:pk>/action/", complete_task, name="task-action")
]

app_name = "todo_list"
