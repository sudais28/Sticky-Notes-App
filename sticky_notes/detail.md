# Project Architecture & File Documentation

This document provides a detailed breakdown of every file in the **Sticky Note Board** project to help you understand how the system works.

---

## 📂 Core Project Folder (`sticky_notes_v2/`)

### 1. `settings.py`
The "brain" of the project. It contains all configurations, including:
- **INSTALLED_APPS**: List of active modules (including `jazzmin` for the admin theme).
- **DATABASES**: Connection settings for the SQLite database.
- **JAZZMIN_SETTINGS**: Custom configuration for the professional admin dashboard UI.
- **AUTH_PASSWORD_VALIDATORS**: Security rules for user passwords.

### 2. `urls.py` (Main)
The main traffic controller. It routes requests to the correct app.
- `/admin/` goes to the administration panel.
- `/accounts/` handles login/logout.
- `/` (root) is passed to the `notes` app.

### 3. `wsgi.py` & `asgi.py`
These are web server gateway interfaces. You don't usually edit these; they allow the project to communicate with web servers like Gunicorn or Daphne when you deploy it online.

---

## 📂 Application Folder (`notes/`)

### 1. `models.py`
Defines the **Note** model. This is where the database structure lives. It stores the title, content, priority, category, and custom color for every sticky note.

### 2. `views.py`
The "Logic" layer. It contains Class-Based Views (CBVs) like `NoteListView` and `NoteCreateView`. These handle what happens when a user clicks a button or visits a page.

### 3. `services.py`
A custom layer I added to keep the code clean. Instead of putting heavy database logic in `views.py`, we use "Service functions" like `create_note()` or `toggle_note()` here. This makes the project much easier to maintain.

### 4. `forms.py`
Handles the **Sticky Note Creation Form**. It uses Tailwind CSS classes to style the input fields so they look integrated into the "sticky note" theme.

### 5. `urls.py` (App-specific)
Defines the internal routes for the notes app, such as `/create/`, `/update/`, and `/delete/`.

### 6. `admin.py`
Customizes the Django Admin interface. It registers the Note model so you can manage it from the dashboard and sets up the custom headers and filters.

### 7. `serializers.py`
Used by the Django Rest Framework (DRF). It converts database objects into JSON format so that other apps or JavaScript could potentially read the data.

---

## 📂 Templates Folder (`templates/`)

### 1. `base.html`
The master layout. It contains the `<head>`, CSS links, and the overall "Board" background. All other pages "plug into" this file so you don't have to repeat code.

### 2. `notes/note_list.html`
The "Wall" view. This file generates the grid of sticky notes you see on the main page. It uses a `{% cycle %}` tag to randomly rotate the notes for a natural look.

### 3. `notes/note_form.html`
The "Composition" view. It displays the large sticky note where you type your thoughts.

---

## 📄 Root Files

### 1. `manage.py`
The command-line utility. You use this to run the server, create users, and apply database migrations.

### 2. `requirements.txt`
A list of all Python libraries needed to run the project (Django, Jazzmin, etc.).

### 3. `README.md`
The user manual. It explains how to install and use the project.
