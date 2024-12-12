from django.contrib.auth import get_user_model
from django.db.models.signals import Signal

from rest_framework import views, status, response, exceptions

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from oktta.permissions import IsAdministrator
from oktta.utils import generate_password
from order.models import Order
from .serializers import UserRegistrationSerializer
from .models import UserRegister


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


class UserRegistrationApiView(views.APIView):
    def get_permissions(self):
        method = self.request.method

        if method == 'GET':
            return []
        elif method == 'POST':
            return []
        return []

    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')

        if not token:
            raise exceptions.ValidationError(detail={'error': 'token does\'t found'}, code=status.HTTP_400_BAD_REQUEST)

        try:
            user_data = UserRegister.objects.get(register_token=token)
            data_serializer = UserRegistrationSerializer(user_data)
        except UserRegister.DoesNotExist:
            raise exceptions.ValidationError(detail={'error': 'user does\'t found'}, code=status.HTTP_400_BAD_REQUEST)

        serializer = UserRegistrationSerializer(data=data_serializer.data)
        serializer.is_view = True
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data.delete()

        return response.Response(data={'success': 'User was created'}, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data={'success': 'Check mail'}, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        token_response = super().post(request, *args, **kwargs)

        if not token_response.status_code == 200:
            raise exceptions.AuthenticationFailed(detail='cant authenticate', code=status.HTTP_400_BAD_REQUEST)

        token_response.headers['X-Access-Token'] = token_response.data['access']
        token_response.headers['X-Refresh-Token'] = token_response.data['refresh']

        token_response.data = {'success': 'user authorization'}

        return token_response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        token_response = super().post(request, *args, **kwargs)

        if not token_response.status_code == 200:
            raise exceptions.AuthenticationFailed(detail='cant refreshing', code=status.HTTP_400_BAD_REQUEST)

        token_response.headers['X-Access-Token'] = token_response.data['access']

        token_response.data = {'success': 'token was refreshing'}

        return token_response
