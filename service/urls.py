from django.urls import path
from service.apps import ServiceConfig
from service.views import OrderCreateView, OrderDeleteView, OrderUpdateView, OrderDetailView, OrderListView, \
    TableListView, index, contacts, about_us, feedback

app_name = ServiceConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('about_us/', about_us, name='about_us'),
    path('feedback/', feedback, name='feedback'),
    path('tables/list/', TableListView.as_view(), name='table_list'),
    path('order/list/', OrderListView.as_view(), name='order_list'),
    path('order/create/<int:pk>', OrderCreateView.as_view(), name='order_create'),
    path('order/update/<int:pk>', OrderUpdateView.as_view(), name='order_update'),
    path('order/detail/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('order/delete/<int:pk>', OrderDeleteView.as_view(), name='order_delete'),
]