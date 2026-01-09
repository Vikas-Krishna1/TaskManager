📝 TaskManager — Django Task Management App

A simple and secure task management web application built with Django, HTML templates, and SQLite. The app supports full user authentication and CRUD operations for managing personal tasks.

🚀 Features

🔐 User Authentication

Sign up, log in, and log out

Secure session-based authentication using Django’s built-in auth system

✅ Task Management (CRUD)

Create new tasks

View current and completed tasks

Update existing tasks

Delete tasks

Mark tasks as completed

👤 User-Specific Data

Each user can only see and manage their own tasks

🗄️ SQLite Database

Lightweight, file-based database

No external setup required

🖥️ Server-Side Rendered UI

Django templates with HTML

CSRF-protected forms

🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, Django Templates

Database: SQLite

Authentication: Django Auth System

📂 Project Structure
TaskManager/
├── TaskManager/        # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── todo/               # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── todo/
│           ├── base.html
│           ├── home.html
│           ├── loginuser.html
│           ├── signupuser.html
│           ├── currenttodos.html
│           ├── completedtodos.html
│           └── viewtodo.html
│
├── db.sqlite3
├── manage.py
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/taskmanager.git
cd taskmanager

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install django

4️⃣ Apply migrations
python manage.py migrate

5️⃣ Run the development server
python manage.py runserver


Visit:

http://127.0.0.1:8000/

🔐 Authentication Flow

New users can sign up

Existing users can log in

Only authenticated users can:

Create tasks

View tasks

Update tasks

Delete tasks

Mark tasks as completed

📸 Screens & UI

Home page

Login & signup forms

Current tasks list

Completed tasks list

Task detail & update view

(Screenshots can be added here)

🧪 Database

Uses SQLite (db.sqlite3)

Automatically created when migrations are applied

Ideal for development and small-scale apps

🔒 Security

CSRF protection enabled

User ownership enforced on all tasks

Session-based authentication

📈 Future Improvements

Task due dates & priorities

Task search & filters

Pagination

REST API support

Frontend styling with Bootstrap/Tailwind

Deployment (Docker / Railway / Render)

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss improvements.

📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Vikas Krishna
Computer Science Student
Stony Brook University
