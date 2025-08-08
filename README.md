# 📚 Django Library Management System

A full-featured **Library Management System** built using **Django**.  
This project provides **role-based access control** for **Admins** and **Students**, enabling book management, borrowing, returning, fine calculation, and tracking borrow history.

---

## 🚀 Features

### 👤 User Management
- **Student & Admin Roles**
- User registration and authentication
- Profile management
- Role-based access control
- Secure login/logout

### 📖 Book Management
- Admin can add, edit, delete books
- Manage book stock & quantities
- Upload book images
- Auto-generate book slugs
- Search & filter books

### 📚 Book Borrowing & Returning
- Students can view available books
- Borrow a book with due date
- Auto decrease stock on borrow
- Track borrow history
- Prevent borrowing same book twice
- Admin can track who borrowed each book

### ⏳ Due Dates & Fines
- Due date set automatically on borrow
- Fine calculation for late returns
- Overdue book detection

### 📊 Dashboard
- **Admin Dashboard**
  - Total books, issued books, and overdue books
  - See all borrowed book details
- **Student Dashboard**
  - View borrowed books
  - Track due dates
  - Fine details

---

## 🛠 Tech Stack
- **Backend:** Django 5.x
- **Frontend:** HTML, Bootstrap 5, Crispy Forms
- **Database:** SQLite (default), PostgreSQL (optional)
- **Other:** Pillow (Image handling), python-dotenv


## 📂 Project Structure
<pre>

    library_project/
    │
    ├── .env
    ├── .gitignore
    ├── manage.py
    ├── requirements.txt
    │
    ├── library_project/ # Main Django project
    │ ├── init.py
    │ ├── settings.py
    │ ├── urls.py
    │ ├── wsgi.py
    │ └── asgi.py
    │
    ├── users/ # User management app
    │ ├── models.py
    │ ├── views.py
    │ ├── forms.py
    │ ├── urls.py
    │ ├── admin.py
    │ └── templates/users/
    │
    ├── books/ # Book management app
    │ ├── models.py
    │ ├── views.py
    │ ├── forms.py
    │ ├── urls.py
    │ ├── admin.py
    │ └── templates/books/
    │
    ├── dashboard/ # Dashboard app
    │ ├── views.py
    │ ├── urls.py
    │ └── templates/dashboard/
    │
    └── templates/ # Global templates
    ├── base.html
    └── navbar.html

</pre>

# ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
<pre>
git clone https://github.com/your-username/django-library-management.git
cd django-library-management
</pre>

2️⃣ Create & Activate Virtual Environment

<pre>
    python -m venv env
# Activate (Windows)
env\Scripts\activate
# Activate (Mac/Linux)
source env/bin/activate
</pre>

3️⃣ Install Dependencies

<pre>
    pip install -r requirements.txt
</pre>


4️⃣ Configure Environment Variables
Create a .env file in the root directory:
<pre>
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    ENGINE=db_type
    NAME=db_name
    USER=db_user
    PASSWORD=db_password
    HOST=db_host
    PORT=db_port
</pre>




5️⃣ Apply Migrations
<pre>
    python manage.py makemigrations
    python manage.py migrate
</pre>

6️⃣ Create Superuser
<pre>
    
python manage.py createsuperuser
</pre>


7️⃣ Run Server
<pre>
    python manage.py runserver
</pre>

