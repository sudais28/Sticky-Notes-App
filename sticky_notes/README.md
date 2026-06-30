# 📝 Sticky Note Board

A modern virtual sticky note application inspired by physical pinboards. Organize ideas, tasks, reminders, and projects with colorful notes in a clean, intuitive interface.

## ✨ Features

- 🎨 Realistic sticky note design with subtle rotations and paper styling
- 🌈 Multiple pastel note colors
- 📂 Categories: Work, Personal, Ideas, Tasks, and Other
- ✅ Mark notes as completed with a single click
- 📌 Pinboard-style layout for an organized workspace
- 👤 User authentication with individual boards
- 🔒 Django admin panel for managing users and notes

## 🛠️ Tech Stack

- Python
- Django
- HTML, CSS, JavaScript
- SQLite (default)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd sticky-note-board
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create an administrator (optional)

```bash
python manage.py createsuperuser
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## 👥 User Management

### Create an Admin
```bash
python manage.py createsuperuser
```

### Change a Password
```bash
python manage.py changepassword <username>
```

### Delete a User
```bash
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='<username>').delete()"
```

## 📁 Project Structure

```
sticky-note-board/
├── manage.py
├── requirements.txt
├── app/
├── templates/
├── static/
└── db.sqlite3
```

## 📸 Screenshots

Add screenshots or GIFs here to showcase the application.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

## 📄 License

This project is intended for educational and personal use. Add your preferred license if you plan to distribute it.

---

Built with ❤️ using Django.
