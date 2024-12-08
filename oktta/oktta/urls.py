from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('order.urls')),
    path('api/', include('users.urls')),
    path('api/swagger/', TemplateView.as_view(template_name='swagger_ui.html'))
]
