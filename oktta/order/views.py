from rest_framework import views, status, response, exceptions, permissions

from .serializers import OrderSerializer, OrderUpdateSerializer
from .models import Order


class OrderApiView(views.APIView):
    """API для создания, получения и изменения заявок"""
    # TODO когда модель User будет готова, сделать permission, что бы только user с ролью администратора мог изменять
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Только для роли (administrator)"""
        pk = kwargs.get('pk')

        if pk:
            try:
                order = Order.objects.get(pk=pk)
                serializer = OrderSerializer(order)
                return response.Response(data={'detail': serializer.data})
            except Order.DoesNotExist:
                return response.Response(data={'detail': 'data does\'t found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            order = Order.objects.all()
            serializer = OrderSerializer(order, many=True)
            return response.Response(data={'detail': serializer.data})

    def post(self, request, *args, **kwargs):
        """Для всех"""
        pk = kwargs.get('pk')

        if pk:
            raise exceptions.MethodNotAllowed(method='POST')

        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(data={'detail': serializer.data}, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        """Только для роли (administrator)"""
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
