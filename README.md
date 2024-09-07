CBN Creche Management System (CCMS)
CBN Creche Management System is a web-based application built using Django, aimed at helping manage a creche, including child registration, staff management, user roles, attendance, and more.

Features
User Management:

Role-based access control (Admin, Teacher, Student)
Registration and authentication
Manage users (view, add, edit, delete, reset password)
Child Management:

Register and view all children
Track attendance and progress reports
Staff Management:

Register and view all staff
Assign tasks and manage attendance
Dashboard:

A responsive dashboard with an intuitive user interface
Sidebar with collapsible menu
Search bar for quick navigation
User profile with logout dropdown
Custom Styling:

Fully customized CSS with Bootstrap integration
Box-shadow and custom background for dashboard content
Transparent sidebar with dark background image
Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap, JavaScript
Database: SQLite (or any other DB supported by Django)
Version Control: Git

Installation
1. Clone the repository:
git clone https://github.com/embee430/SchoolManagementSystem.git
cd school-management-system

2. Create and activate a virtual environment:
python3 -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

3. Install the dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Run the development server:
python manage.py runserver

6. Access the application:
Open a browser and go to http://127.0.0.1:8000/

Username: user1
Password: cBn12345
