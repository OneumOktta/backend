from django.urls import path

from .views import FeedbackViews

urlpatterns = [
    path('feedback/', FeedbackViews.as_view())
]