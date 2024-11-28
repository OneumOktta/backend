from django.urls import path

from .views import OrderApiView


urlpatterns = [
    path('order/', OrderApiView.as_view(), name='order'),
    path('order/<int:pk>/', OrderApiView.as_view(), name='order_update')
]
