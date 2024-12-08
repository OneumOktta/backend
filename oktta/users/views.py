from django.contrib.auth import get_user_model
from django.db.models.signals import Signal

from rest_framework import views, status, response

from oktta.permissions import IsAdministrator
from oktta.utils import generate_password
from order.models import Order


User = get_user_model()


class AdminCreateUserApiView(views.APIView):
    user_signal = Signal()

    def get_permissions(self):
        method = self.request.method

        if method == 'GET':
            return [IsAdministrator(), ]
        return []

    def get(self, request, *args, **kwargs):
        token_auth = request.GET.get('key')

        if not token_auth:
            return response.Response(data={'detail': 'token does\'t found'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.get(token_auth=token_auth, status=True)
        except Order.DoesNotExist:
            return response.Response(data={'detail': 'order bad token or user was created'}, status=status.HTTP_400_BAD_REQUEST)

        user_data = {
            'email': order.email,
            'name': order.full_name,
            'company_name': order.company_name,
            'phone': order.phone,
            'telegram': order.telegram,
            'password': generate_password()
        }

        try:
            user = User.objects.create_user(**user_data)

            order.status = False
            order.save()
        except Exception as e:
            return response.Response(data={'detail': f'user can\'t created ({str(e)})'}, status=status.HTTP_400_BAD_REQUEST)

        self.user_signal.send(sender='send_user_mail', user_data=user_data)

        return response.Response(data={'detail': f'{user.email} was created'}, status=status.HTTP_201_CREATED)
