from rest_framework import generics, permissions
from service.models import Table, TimeSection, Order
from service.serializers import TableSerializer, TimeSectionSerializer, OrderSerializer

class TableListAPI(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.AllowAny]

class TimeSectionListAPI(generics.ListAPIView):
    queryset = TimeSection.objects.all()
    serializer_class = TimeSectionSerializer
    permission_classes = [permissions.AllowAny]

class OrderListCreateAPI(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=user)