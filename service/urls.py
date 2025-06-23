from django.urls import path

from service.api_views import TableListAPI, TimeSectionListAPI, OrderListCreateAPI, OrderRetrieveUpdateDestroyAPI
from service.views import OrderCreateView, OrderDeleteView, OrderUpdateView, OrderDetailView, OrderListView, \
    TableListView, index, contacts, about_us, feedback, table_gallery

app_name = 'service'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('about_us/', about_us, name='about_us'),
    path('tables/gallery/', table_gallery, name='table_gallery'),
    path('feedback/', feedback, name='feedback'),
    path('tables/list/', TableListView.as_view(), name='table_list'),
    path('order/list/', OrderListView.as_view(), name='order_list'),
    path('order/create/<int:pk>', OrderCreateView.as_view(), name='order_create'),
    path('order/update/<int:pk>', OrderUpdateView.as_view(), name='order_update'),
    path('order/detail/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('order/delete/<int:pk>', OrderDeleteView.as_view(), name='order_delete'),

    # API маршруты
    path('api/tables/', TableListAPI.as_view(), name='api_table_list'),
    path('api/timesections/', TimeSectionListAPI.as_view(), name='api_timesection_list'),
    path('api/orders/', OrderListCreateAPI.as_view(), name='api_order_list_create'),
    path('api/orders/<int:pk>/', OrderRetrieveUpdateDestroyAPI.as_view(), name='api_order_detail'),
]