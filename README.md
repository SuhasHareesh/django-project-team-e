# Django Hotel Management System

This project is a web-based Hotel Management System developed using Django. It facilitates the management of hotel operations, including room bookings, customer information, and billing.

## Features

- **Room Management**: Add, update, and delete room details.
- **Booking System**: Manage room bookings and track availability.
- **Customer Management**: Store and manage customer information.
- **Billing**: Generate invoices for customers.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SuhasHareesh/django-project-team-e.git

2. **Navigate to the project directory**:
   ```bash
   cd django-project-team-e

3. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv env
   
4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt

5. **Apply migrations**:
   ```bash
   python manage.py migrate

6. **Create a superuser (to access the admin panel)**:
   ```bash
   python manage.py createsuperuser

7. **Start the development server**:
   ```bash
   python manage.py runserver

 ## Usage

- Access the application at http://127.0.0.1:8000/.
- Use the admin panel at http://127.0.0.1:8000/admin/ to manage rooms, bookings, and customers.
