from django.urls import path

from .views import AdminCreateUserApiView, UserRegistrationApiView, UserApiView


urlpatterns = [
    path('admin_create_user/', AdminCreateUserApiView.as_view(), name='admin_create_user'),
    path('registration/', UserRegistrationApiView.as_view(), name='user-registration'),
    path('get-user/', UserApiView.as_view(), name='get-user'),
]
