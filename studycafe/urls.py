from django.urls import path
from .views import CafeListView, CafeUploadView, CafeDetailView

app_name = 'studycafe'

urlpatterns = [
    path('cafelist', CafeListView.as_view(), name='cafelist'),
    path('cafeupload<int:pk>', CafeUploadView.as_view(), name='cafeupload'),
    path('cafedetail<int:pk>', CafeDetailView.as_view(), name='cafedetail'),
]