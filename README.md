# Django CRUD Project with Bootstrap

This Django project is a simple web application that performs CRUD (Create, Read, Update, Delete) operations using Django and incorporates Bootstrap for the user interface.

## Prerequisites

- Python (3.6 or higher)
- Django (3.x or higher)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/manishgk9/basic_crud_django.git
    cd basic_crud_django
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser and navigate to [http://localhost:8000](http://localhost:8000) to access the application.

8. Admin panel can be accessed at [http://localhost:8000/admin](http://localhost:8000/admin) using the superuser credentials.

## Features

- CRUD operations for managing data.
- Bootstrap for a responsive and user-friendly UI.

## Project Structure
django-crud-bootstrap/
│
├── core/
│ ├── migrations/
│ ├── templates/
│ │ └── base.html/
│ │ └── home.html/
│ │ └── add_employee.html/
│ │ └── delete_employee.html/
| | └── update_employee.html/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── basic_crud/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.pyl
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt

