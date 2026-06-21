from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'priority', 'category', 'color']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-3 border-b-2 border-slate-200 focus:border-yellow-500 focus:outline-none transition-all bg-transparent font-bold text-lg',
                'placeholder': 'Note Title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-3 border-none focus:ring-0 transition-all bg-yellow-50/50 rounded-xl font-medium',
                'rows': 5,
                'placeholder': 'What is on your mind?'
            }),
            'priority': forms.Select(attrs={
                'class': 'w-full p-2 border-2 border-slate-100 rounded-xl focus:border-yellow-500 transition-all'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-2 border-2 border-slate-100 rounded-xl focus:border-yellow-500 transition-all'
            }),
            'color': forms.TextInput(attrs={
                'type': 'color',
                'class': 'h-10 w-full p-1 border-2 border-slate-100 rounded-xl cursor-pointer'
            }),
        }