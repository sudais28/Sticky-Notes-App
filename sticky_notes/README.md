# Sticky Note Board | Virtual Organization System

Sticky Note Board is a creative personal organization tool that mimics a real-world physical pinboard. Capture your ideas on colorful virtual sticky notes and organize them with ease.

## 🚀 Features

- **Classic Sticky Aesthetic**: Notes look like real paper with slight rotations, pins, and handwritten-style fonts.
- **Customizable Colors**: Choose different pastel shades for your notes.
- **Categorization**: Group notes into Work, Personal, Idea, Task, or Other.
- **Pinboard View**: A natural grid layout that feels like a physical board.
- **Quick Toggle**: Mark tasks as "Done" with a visual checkmark.

## 📋 Quick Start

1. **Install Dependencies**: `pip install -r requirements.txt`
2. **Setup Database**: 
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. **Run Server**: `python manage.py runserver`

## 👤 User Management

- **Create a New User**: Run `python manage.py createsuperuser` in the terminal to create an admin account.
- **Login/Logout**: Use the "Leave Board" link to sign out and switch accounts.
- **Admin Panel**: Access `http://127.0.0.1:8000/admin/` to manage all board users and notes.

## 💡 Advanced Tips

- **Resetting/Deleting a User**: If you need to delete a user to start over, run:
  ```powershell
  python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='YOUR_USERNAME').delete()"
  ```
- **Password Reset**: Run `python manage.py changepassword YOUR_USERNAME`.

---
*Sticky Note Board - Pin your thoughts.*
