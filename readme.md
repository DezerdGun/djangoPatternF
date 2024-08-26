# Django Project Setup

## Installation and Project Setup

1. Install Django:
    ```bash
    pip install django
    ```

2. Start a new Django project:
    ```bash
    django-admin startproject myproject
    ```

3. Navigate to the project directory:
    ```bash
    cd myproject
    ```

4. Start a new Django app:
    ```bash
    python manage.py startapp myapp
    ```

## Creating Views and URL Configuration

5. In `myapp/views.py`, create a simple view:
    ```python
    from django.http import HttpResponse

    def text(request):
        return HttpResponse("Hello world")
    ```

6. In `myapp/urls.py`, configure the URL routing for the app:
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.text, name='text')
    ]
    ```

7. In `myproject/urls.py`, include the app's URL configurations:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include("myapp.urls"))
    ]
    ```

## Running the Server

8. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

9. Open your web browser and navigate to the server URL (e.g., `http://127.0.0.1:8000/`) to see the "Hello world" message.

## Connecting to MySQL

1. Install the MySQL client:
    ```bash
    pip install mysqlclient
    ```

2. Configure your database in `myproject/settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',  # Replace with your database name
            'USER': 'your_database_user',  # Replace with your MySQL username
            'PASSWORD': 'your_database_password',  # Replace with your MySQL password
            'HOST': 'localhost',  # Set to your MySQL server address
            'PORT': '3306',  # Default MySQL port
        }
    }
    ```

3. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

Your Django project is now set up and connected to MySQL!
