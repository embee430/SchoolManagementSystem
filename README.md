CBN Creche Management System (CCMS)

CBN Creche Management System is a web-based application built using Django, aimed at helping manage a creche, including child registration, staff management, user roles, attendance, and more.

Features

1. User Management:
	a. Role-based access control (Admin, Teacher, Student).
	b. Registration and authentication
	c. Manage users (view, add, edit, delete, reset password)
   
2. Child Management:
   	a. Register and view all children
   	b. Track attendance and progress reports

3. Staff Management:
	a. Register and view all staff
	b. Assign tasks and manage attendance

4. Dashboard:
	a. A responsive dashboard with an intuitive user interface
	b. Sidebar menu
	c. Search bar for quick navigation
	d. User profile with logout dropdown

5. Custom Styling:
	a. Fully customized CSS with Bootstrap integration
	b. Box-shadow and custom background for dashboard content
	c. Transparent sidebar with dark background image

6. Technologies Used
	a. Backend: Django (Python)
	b. Frontend: HTML, CSS, Bootstrap, JavaScript
	c. Database: SQLite (or any other DB supported by Django)
	d. Version Control: Git

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
