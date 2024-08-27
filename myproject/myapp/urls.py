from django.urls import path
from . import views


urlpatterns = [
    path('',views.hello_view, name = 'hello'),
    path('about/', views.hello_view, name='about'),
    path('classes/', views.hello_view, name='classes'),
    path('blog/', views.hello_view, name='blog'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]