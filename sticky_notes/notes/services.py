from .models import Note

def get_user_notes(user):
    return Note.objects.filter(user=user).order_by('-created_at')


def create_note(user, data):
    return Note.objects.create(
        user=user,
        title=data['title'],
        content=data['content'],
        priority=data['priority'],
        category=data.get('category', 'O'),
        color=data.get('color', '#fef08a')
    )


def update_note(note, data):
    note.title = data['title']
    note.content = data['content']
    note.priority = data['priority']
    note.category = data.get('category', 'O')
    note.color = data.get('color', '#fef08a')
    note.save()
    return note


def delete_note(note):
    note.delete()


def toggle_note(note):
    note.toggle_status()
    return note