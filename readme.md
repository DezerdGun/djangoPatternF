1. pip install django
2. django-admin startproject myproject
3. cd myproject
4. python manage.py startapp myapp
5.myapp/views.py 
from django.http import HttpResponse

def text(request):
    return HttpResponse("Hello wolrd")
6. myapp/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('',views.text, name = 'text')
]

7. myproject/urls.py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("myapp.urls"))
]
8. python manage.py runserver
9. httpp -> copy trow at web url

connection with mysql 
1.pip install mysqlclient
2.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',  # Replace with your database name
        'USER': 'your_database_user',  # Replace with your MySQL username
        'PASSWORD': 'your_database_password',  # Replace with your MySQL password
        'HOST': 'localhost',  # Set to your MySQL server address
        'PORT': '3306',  # Default MySQL port
    }
}
3.python manage.py makemigrations -> ne vajno
python manage.py migrate
