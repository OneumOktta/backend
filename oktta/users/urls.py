from django.urls import path

from .views import AdminCreateUserApiView, UserApiView


urlpatterns = [
    path('admin_create_user/', AdminCreateUserApiView.as_view(), name='admin_create_user'),
    path('user/', UserApiView.as_view(), name='user')
]
