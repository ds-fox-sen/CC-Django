from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Userside form for adding topics."""

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """Userside form for adding an entry to a topic."""

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
