from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import debug_toolbar

from studycafe import views
from studycafe.views import CafeListView, CafeUploadView, CafeDetailView, CafeEditView, cafedelete, BusinessUserDetailView, ReservationView, personal_signup, business_signup


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # index home
    path('', views.index, name='index'),
    
    # auth
    path('personal_signup/', views.personal_signup, name='personal_signup'),
    path('business_signup/', views.business_signup, name='business_signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    # social login
    path('', include('allauth.urls')),

    # user profile pages
    path('BUprofile/<int:pk>', BusinessUserDetailView.as_view(), name='BUprofile'),
    
    # study cafe listings
    path('cafelist', CafeListView.as_view(), name='cafelist'),
    path('cafeupload/<int:pk>', CafeUploadView.as_view(), name='cafeupload'),
    path('cafedetail/<int:pk>', CafeDetailView.as_view(), name='cafedetail'),
    path('cafeedit/<int:pk>', CafeEditView.as_view(), name='cafeedit'),
    path('cafedelete/<int:cafe_pk>', views.cafedelete, name='cafedelete'),
    path('reserve<int:pk>',ReservationView.as_view(), name='reservation'),

    # django debugger tool
    path('__debug__/', include(debug_toolbar.urls)),

]