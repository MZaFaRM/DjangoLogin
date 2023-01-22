from django.urls import path
from .views import LoginViewSet

urlpatterns = [
    path("", LoginViewSet.as_view({'get': 'login', 'post': 'login'}), name="Login")
]
