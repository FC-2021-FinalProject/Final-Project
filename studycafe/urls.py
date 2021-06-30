from django.urls import path
from .views import CafeListView, CafeUploadView

app_name = 'studycafe'

urlpatterns = [
    path('cafelist', CafeListView.as_view(), name='cafelist'),
    path('cafeupload', CafeUploadView.as_view(), name='cafeupload'),
]