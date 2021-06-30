from django.urls import path
from userinfo import views
from userinfo.views import BusinessUserDetailView

app_name = 'userinfo'

urlpatterns = [
    path('', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('BUprofile/<int:pk>', BusinessUserDetailView.as_view(), name='BUprofile'),
]

