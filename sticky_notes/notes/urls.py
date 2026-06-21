from django.urls import path
from .views import *

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('create/', NoteCreateView.as_view(), name='note_create'),
    path('update/<int:pk>/', NoteUpdateView.as_view(), name='note_update'),
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='note_delete'),
    path('toggle/<int:pk>/', NoteToggleView.as_view(), name='note_toggle'),
]