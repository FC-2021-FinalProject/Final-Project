from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import debug_toolbar

from studycafe import views
from studycafe.views import CafeListView, CafeUploadView, CafeDetailView, CafeEditView
from studycafe.views import BusinessUserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #
    path('', views.index, name="index"),
    
    # auth
    path('login/', views.login, name="login"),
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

    # django debugger tool
    path('__debug__/', include(debug_toolbar.urls)),
]