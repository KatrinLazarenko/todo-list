from django import forms

from todo.models import Task, Tag


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    date = forms.DateField(widget=DateInput)
    deadline = forms.DateField(widget=DateInput)

    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
