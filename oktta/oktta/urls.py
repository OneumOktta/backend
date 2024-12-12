from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

from users.views import CustomTokenObtainPairView, CustomTokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('order.urls')),
    path('api/', include('users.urls')),
    path('api/swagger/', TemplateView.as_view(template_name='swagger_ui.html')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh')
]
