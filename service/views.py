from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.utils import timezone

from service.forms import OrderForm
from service.models import Order, Table


def index(request):
    return render(request,'service/index.html')


def about_us(request):
    return render(request,'service/about_us.html')


def contacts(request):
    return render(request,'service/contacts.html')


def feedback(request):
    return render(request,'service/feedback.html')

def table_gallery(request):
    tables = Table.objects.all()  # Получаем все столики
    return render(request, 'service/table_gallery.html', {'tables': tables})


class TableListView(ListView):
    model = Table
    template_name = 'service/reservation_blank.html'
    paginate_by = 4

    def get_queryset(self):
        date = self.request.GET.get('date', timezone.now().date())
        return Table.objects.exclude(id__in=Order.objects.filter(order_date=date).values_list('table', flat=True))


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('users:my_cabinet')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'table_pk': self.kwargs.get('pk')})
        return kwargs

    def form_valid(self, form):
        reservation_date = form.cleaned_data['reservation_date']
        order_times = form.cleaned_data['order_time']

        # Проверка на существующие заказы
        existing_orders = Order.objects.filter(
            table=self.kwargs.get('pk'),
            reservation_date=reservation_date,
            order_time__in=order_times
        )

        if existing_orders.exists():
            form.add_error(None, "Этот столик уже забронирован на указанное время в выбранный день.")
            return self.form_invalid(form)

        order = form.save(commit=False)
        order.user = self.request.user
        order.table = Table.objects.get(pk=self.kwargs.get('pk'))
        order.save()
        order.order_time.set(order_times)  # Сохраняем выбранное время
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('users:my_cabinet')

    def form_valid(self, form):
        order = self.get_object()
        times_used = order.order_time.all()
        used_table = order.table
        used_table.times.add(*times_used)
        return super().form_valid(form)


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['user', 'table', 'order_time']
    success_url = reverse_lazy('users:my_cabinet')


class OrderListView(ListView):
    model = Order
    paginate_by = 3
    template_name = 'users:my_cabinet'


class OrderDetailView(DetailView):
    model = Order
