# Django URL Shortener

A web-based URL shortening application built using Django and Django REST Framework.

This project allows users to create short URLs from long URLs and redirect users to the original links. It includes user authentication and a responsive user interface.

---

## Features

### User Authentication
- User registration and login
- Secure authentication system
- Custom validation messages
- Password validation rules
- User-friendly login and registration interface

### URL Shortening
- Convert long URLs into short URLs
- Redirect short URLs to original URLs
- Generate unique short links
- Manage URL shortening functionality

### API Support
- REST API implementation using Django REST Framework
- API endpoints for authentication and URL operations

### User Interface
- Responsive design using Bootstrap 5
- Modern authentication pages
- Toast notifications for user feedback
- Improved form validation experience

---

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework

### Frontend
- HTML
- CSS
- Bootstrap 5
- JavaScript

### Database
- SQLite

---

## Project Structure
Django-URL-Shortener
│
├── accounts
│ └── User authentication
│
├── urlshortener
│ └── URL shortening functionality
│
├── core
│ └── Project configuration
│
├── templates
│ └── HTML templates
│
└── manage.py


---

## Installation and Setup

1. Clone the repository:
git clone https://github.com/CHAN-dhana/Django-URL-Shortener.git

2. Navigate to the Project Directory
cd Django-URL-Shortener

3. Create a Virtual Environment
python -m venv venv

4. Activate Virtual Environment
For Windows:
venv\Scripts\activate

5. Install Dependencies
pip install -r requirements.txt
Database Setup
Apply Database Migrations
python manage.py makemigrations
python manage.py migrate
Create Admin User
python manage.py createsuperuser

Enter the required details to create your admin account.

Run Application

Start the Django development server:
python manage.py runserver

Open the application in your browser:
http://127.0.0.1:8000/


