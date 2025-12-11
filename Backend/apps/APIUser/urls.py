from django.urls import path
from .views import RegisterTokenView

urlpatterns = [
    path('register/', RegisterTokenView.as_view(), name='register'),
]