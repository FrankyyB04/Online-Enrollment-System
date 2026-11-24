# EnrollFlow — Student Profile & Class Enrollment Portal (Django)

A clean, soft-modern Django web application for registering students, viewing class rosters, and inspecting detailed student profiles (Personal Information, Educational & Family Background, and Enrollment Status) alongside full Django Admin integration.

## Quick Start

1. Create & activate a virtual environment:
   - Windows: `python -m venv venv` then `venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv venv` then `source venv/bin/activate`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Apply database migrations (or copy your existing `db.sqlite3` into this folder):
   - `python manage.py migrate`
4. Optional — load sample students into the database:
   - `python manage.py seed_students`
5. Create an admin account:
   - `python manage.py createsuperuser`
6. Run the server:
   - `python manage.py runserver`
7. Open:
   - `http://127.0.0.1:8000/` — Student Profile & Class Roster Portal
   - `http://127.0.0.1:8000/register/` — Front-End Student Registration Form
   - `http://127.0.0.1:8000/admin/` — Django Admin Panel
