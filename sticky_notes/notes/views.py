from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note
from .forms import NoteForm
from . import services
from rest_framework import viewsets, permissions
from .serializers import NoteSerializer


class NoteListView(LoginRequiredMixin, View):
    def get(self, request):
        notes = services.get_user_notes(request.user)
        return render(request, "notes/note_list.html", {"notes": notes})


class NoteCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = NoteForm()
        return render(request, "notes/note_form.html", {"form": form})

    def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            services.create_note(request.user, form.cleaned_data)
            return redirect("note_list")
        return render(request, "notes/note_form.html", {"form": form})


class NoteUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        form = NoteForm(instance=note)
        return render(request, "notes/note_form.html", {"form": form})

    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            services.update_note(note, form.cleaned_data)
            return redirect("note_list")
        return render(request, "notes/note_form.html", {"form": form})


class NoteDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        services.delete_note(note)
        return redirect("note_list")


class NoteToggleView(LoginRequiredMixin, View):
    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        services.toggle_note(note)
        return redirect("note_list")


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)