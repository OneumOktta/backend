from django.urls import path

from .views import AdminCreateUserApiView


urlpatterns = [
    path('admin_create_user/', AdminCreateUserApiView.as_view(), name='admin_create_user')
]
