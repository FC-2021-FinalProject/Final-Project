from os import name
from django.urls import path
from .views import CafeListView, CafeUploadView, CafeDetailView, CafeEditView

app_name = 'studycafe'

urlpatterns = [
    path('cafelist', CafeListView.as_view(), name='cafelist'),
    path('cafeupload/<int:pk>', CafeUploadView.as_view(), name='cafeupload'),
    path('cafedetail/<int:pk>', CafeDetailView.as_view(), name='cafedetail'),
    path('cafeedit/<int:pk>', CafeEditView.as_view(), name='cafeedit'),
]