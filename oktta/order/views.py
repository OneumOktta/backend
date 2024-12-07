from rest_framework import views, status, response, exceptions, permissions

from oktta.permissions import IsAdministrator

from .serializers import OrderSerializer, OrderUpdateSerializer
from .models import Order


class OrderApiView(views.APIView):
    """API для создания, получения и изменения заявок"""
    def get_permissions(self):
        """Доступ к API в зависимости от метода"""
        method = self.request.method

        if method == 'GET':
            permission_classes = [IsAdministrator, ]
        elif method == 'POST':
            permission_classes = []
        elif method == 'PATCH':
            permission_classes = [IsAdministrator, ]
        else:
            permission_classes = [permissions.IsAuthenticated, ]

        return [permission() for permission in permission_classes]

    def get(self, request, *args, **kwargs):
        """Получение заявки или список заявок. Доступно только для роли (administrator)"""
        pk = kwargs.get('pk')

        if pk:
            try:
                order = Order.objects.get(pk=pk)
                serializer = OrderSerializer(order)
                return response.Response(data={'detail': serializer.data})
            except Order.DoesNotExist:
                return response.Response(data={'detail': 'data does\'t found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return response.Response(data={'detail': serializer.data})

    def post(self, request, *args, **kwargs):
        """Создание заявки. Для всех ролей"""
        pk = kwargs.get('pk')

        if pk:
            raise exceptions.MethodNotAllowed(method='POST')

        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(data={'detail': serializer.data}, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        """Частичное изменение заявки (только поле status). Доступно только для роли (administrator)"""
        pk = kwargs.get('pk')

        if not pk:
            raise exceptions.MethodNotAllowed(method='PATCH')

        if not request.data:
            return response.Response(data={'detail': 'data does\'t found'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return response.Response(data={'detail': 'data does\'t found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderUpdateSerializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(data={'detail': serializer.data}, status=status.HTTP_201_CREATED)
