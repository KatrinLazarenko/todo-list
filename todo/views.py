from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    # context_object_name = "tag_list"
    # template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    # fields = "__all__"
    queryset = Tag.objects.all()
    success_url = reverse_lazy("todo:tag-list")
    form_class = TagForm


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    queryset = Tag.objects.all()
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    queryset = Tag.objects.all()
    success_url = reverse_lazy("todo:tag-list")


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    queryset = Task.objects.all()
    success_url = reverse_lazy("todo:task-list")


class ChangeStatusView(View):
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Task, pk=self.kwargs['pk'])

        obj.status = not obj.status
        obj.save()
        return redirect(reverse_lazy("todo:task-list"))
