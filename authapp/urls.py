from django.urls import path
from authapp import views

app_name='authapp'

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.user_login,name='user_login'),
]