from rest_framework import serializers
from service.models import Table, TimeSection, Order
from users.models import User

class TimeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSection
        fields = ['id', 'time_section']

class TableSerializer(serializers.ModelSerializer):
    times = TimeSectionSerializer(many=True, read_only=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Table
        fields = ['id', 'number', 'seats', 'times', 'image']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    table = TableSerializer(read_only=True)
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(), source='table', write_only=True
    )
    order_time = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=TimeSection.objects.all()
    )

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'table', 'table_id', 'order_time',
            'order_date', 'order_confirm', 'reservation_date'
        ]

    def validate(self, data):
        # Проверка на существующие заказы (конфликты бронирования)
        table = data.get('table')
        reservation_date = data.get('reservation_date')
        order_times = data.get('order_time')

        if self.instance:
            # При обновлении исключаем текущий заказ из проверки
            qs = Order.objects.exclude(pk=self.instance.pk)
        else:
            qs = Order.objects.all()

        if qs.filter(
            table=table,
            reservation_date=reservation_date,
            order_time__in=order_times
        ).exists():
            raise serializers.ValidationError(
                "Этот столик уже забронирован на указанное время в выбранный день."
            )
        return data

    def create(self, validated_data):
        order_times = validated_data.pop('order_time')
        order = Order.objects.create(
            user=self.context['request'].user,
            **validated_data
        )
        order.order_time.set(order_times)
        return order

    def update(self, instance, validated_data):
        order_times = validated_data.pop('order_time', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if order_times is not None:
            instance.order_time.set(order_times)
        return instance