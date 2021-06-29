from django.urls import path
from userinfo import views

app_name = 'userinfo'

urlpatterns = [
    path('', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
]

