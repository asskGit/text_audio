from django.urls import path
from .views import CustomAPIView

urlpatterns = [
    path('text/', CustomAPIView.as_view(), name='text'),


]