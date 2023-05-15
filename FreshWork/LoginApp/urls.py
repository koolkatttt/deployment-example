from django.urls import path
from . import views

app_name = 'LoginApp'


urlpatterns = [

               path('register/', views.register, name='register'),
               path('Login/', views.Login, name='Login'),
]
