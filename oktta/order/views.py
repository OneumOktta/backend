from rest_framework import views, status, response, exceptions, permissions

from .serializers import OrderSerializer, OrderUpdateSerializer
from .models import Order


class OrderApiView(views.APIView):
    """API для создания, получения и изменения заявок"""
    # TODO когда модель User будет готова, сделать permission, что бы только user с ролью администратора мог изменять
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk:
            try:
                order = Order.objects.get(pk=pk)
                serializer = OrderSerializer(order)
                return response.Response(data={'detail': serializer.data})
            except Order.DoesNotExist:
                return response.Response(data={'detail': 'data does not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            order = Order.objects.all()
            serializer = OrderSerializer(order, many=True)
            return response.Response(data={'detail': serializer.data})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk:
            raise exceptions.MethodNotAllowed(method='POST')

        serializer = OrderCreateSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            raise exceptions.ValidationError({'detail': 'data is bad'})

        serializer.save()

        return response.Response(data={'message': serializer.data}, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if not pk:
            raise exceptions.MethodNotAllowed(method='PATCH')

        order = Order.objects.get(pk=pk)
        serializer = OrderUpdateSerializer(order, data=request.data, partial=True)

        if not serializer.is_valid(raise_exception=True):
            raise exceptions.ValidationError({'detail': 'data is bad'})

        serializer.save()

        return response.Response(data={'message': serializer.data}, status=status.HTTP_201_CREATED)
