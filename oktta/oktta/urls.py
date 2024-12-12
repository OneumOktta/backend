from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('order.urls')),
    path('api/', include('users.urls')),
    path('api/swagger/', TemplateView.as_view(template_name='swagger_ui.html')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
