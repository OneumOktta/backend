from django.contrib.auth import get_user_model

from rest_framework import views, permissions, response

from oktta.permissions import IsAdministrator
from .serializers import FeedbackSerializer
from .models import Feedback


User = get_user_model()


class FeedbackViews(views.APIView):
    def get_permissions(self):
        method = self.request.method

        if method == 'GET':
            return [IsAdministrator(), ]
        return [permissions.IsAuthenticated(), ]

    def get(self,request, *args, **kwargs):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return response.Response(data={'detail': serializer.data})