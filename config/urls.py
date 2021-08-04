from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import debug_toolbar

from studycafe import views
from studycafe.views import BusinessUserEditView, CafeListView, CafeUploadView, cafedetailview, CafeEditView, cafedelete, PersonalUserDetailView, BusinessUserDetailView, BusinessUserEditView ,ReservationView, personal_signup, business_signup, personal_profile_edit, personal_password_edit, ReviewView, login, kakao_logout, IdPwSearch, IdSearch, PwSearch, bookmark


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # index home
    path('', views.index, name='index'),
    
    # auth
    path('personal_signup/', views.personal_signup, name='personal_signup'),
    path('business_signup/', views.business_signup, name='business_signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    # Id Pw Searching
    path('IdPwSearch/', views.IdPwSearch, name='IdPwSearch'),
    path('IdSearch/', views.IdSearch, name='IdSearch'),
    path('PwSearch/', views.PwSearch, name='PwSearch'),

    #social login
    path('kakao/login/', views.kakao_login, name='kakao_login'),
    path('kakao/login/callback/', views.kakao_callback, name='kakao_callback'),
    path('kakao/logout/', views.kakao_logout, name='kakao_logout'),
    path('', include('allauth.urls')),

    # user profile pages
    path('PUprofile/<slug:username>', PersonalUserDetailView.as_view(), name='PUprofile'),
    path('PUprofileedit/<slug:username>', views.personal_profile_edit, name='personal_profile_edit'),
    path('PUpasswordedit/<slug:username>', views.personal_password_edit, name='personal_password_edit'),
    path('BUprofile/<int:pk>', BusinessUserDetailView.as_view(), name='BUprofile'),
    path('BUprofileedit/<int:pk>', BusinessUserEditView.as_view(), name='BUedit'),

    # study cafe listings
    path('cafelist', CafeListView.as_view(), name='cafelist'),
    path('cafeupload/<int:pk>', CafeUploadView.as_view(), name='cafeupload'),
    path('cafedetail/<int:pk>', views.cafedetailview, name='cafedetail'),
    # path('cafedetail/<int:pk>', CafeDetailView.as_view(), name='cafedetail'),
    path('cafeedit/<int:pk>', CafeEditView.as_view(), name='cafeedit'),
    path('cafedelete/<int:cafe_pk>', views.cafedelete, name='cafedelete'),
    path('reserve/<int:pk>',ReservationView.as_view(), name='reservation'),
    path('review/<int:pk>', ReviewView.as_view(), name='review'),

    # features
    path('bookmarkcafe/<int:cafe_pk>', views.bookmark, name='bookmark'),

    # django debugger tool
    path('__debug__/', include(debug_toolbar.urls)),

]