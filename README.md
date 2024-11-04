Employee-Management-System-Django-REST-API

    This is a Django REST Framework project for managing employee records, including CRUD operations, JWT authentication, validation, filtering, pagination, and testing.

Features
    Create, Retrieve, Update, and Delete Employees
    JWT Authentication for secure access
    Field Validations:
    Unique and valid email.
    Non-empty name field.

Error Handling with appropriate HTTP status codes:
    201 Created for successful creation.
    404 Not Found for invalid employee IDs.
    400 Bad Request for validation errors.
    204 No Content for successful deletion.

Filtering employees by department and role.
    Pagination with a limit of 10 employees per page.
    Unit Tests for endpoints and edge cases.

Setup Instructions
    Prerequisites
    Python 3.6+
    Django 4.x
    Django REST Framework
    MySQL (or your preferred database)


Install Dependencies

pip install -r requirements.txt
Database Setup

Update the DATABASES section in settings.py to configure your MySQL database:
=
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Apply Migrations

    python manage.py makemigrations
    python manage.py migrate

Create a Superuser

    python manage.py createsuperuser

Run the Development Server
    python manage.py runserver

Authentication and Authorization
    n a JWT token by making a POST request to /api/token/ with a valid username and password.

Use the token in the Authorization header for protected endpoints:

    Authorization: Bearer <your_token>
    API Endpoints

Employee Endpoints
    Method	Endpoint	Description
    POST	/api/employees/	Create a new employee
    GET	/api/employees/	List employees
    GET	/api/employees/{id}/	Retrieve an employee by ID
    PUT	/api/employees/{id}/	Update an employee by ID
    DELETE	/api/employees/{id}/	Delete an employee by ID

Filtering and Pagination
    Filtering: /api/employees/?department=HR&role=Developer
    Pagination: /api/employees/?page=2

Running Tests
Run all tests:

python manage.py test
Expected Tests:

    Valid creation of employees.
    Fetching employees by ID.
    Updating an employee.
    Deleting an employee.
    Validation for unique email.
    Status Codes
    201 Created: Employee successfully created.
    404 Not Found: Invalid employee ID.
    400 Bad Request: Validation errors.
    204 No Content: Successful deletion.
    Example Requests with Postman

Create Employee (POST /api/employees/)

json
{
    "name": "komal patil",
    "email": "komal@gmail.com",
    "department": "Engineering",
    "role": "Developer"
}
Update Employee (PUT /api/employees/{id}/)

json
{
    "name": "komal patil",
    "email": "komal@gmail.com",
    "department": "HR",
    "role": "Manager"
}
Delete Employee (DELETE /api/employees/{id}/)
