from django.urls import path

from todo.views import TagListView, TagCreateView, TagUpdateView, TagDeleteView, TaskListView, TaskCreateView, \
    TaskUpdateView, TaskDeleteView, ChangeStatusView


urlpatterns = [
    # path("", index, name="index"),
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path('task/<int:pk>/change', ChangeStatusView.as_view(), name="task-change"),
]

app_name = "todo"
