from .forms import OrderDispatcherForm, OrderForm, OrderUpdateForm
from .models import Order
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django_xhtml2pdf.views import PdfMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy

def delete_bd(request):
    Order().delete_everything
    Order().drop_table
    
    return render(request, "Удалено")

class ActualOrdersUpdateView(UpdateView):
    model = Order
    template_name = 'orders/add_actual_order.html'
    form_class = OrderForm
    success_url = '/orders/actual'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
class OrdersUpdateView(UpdateView):
    model = Order
    success_url = '/orders/dispatcher'
    template_name = 'orders/update_order.html'
    form_class = OrderUpdateForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class OrdersDeleteView(DeleteView):
    model = Order
    success_url = '/orders/actual'
    template_name = 'orders/delete-order.html'
    context_object_name = 'orders'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class DoneOrders(ListView):
    model = Order
    queryset = Order.objects.filter(status='Выполнена')
    template_name = 'orders/orders.html'
    context_object_name = 'all_orders'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
class ActualOrders(ListView):
    model = Order
    queryset = Order.objects.filter((Q(status='Актуальная') | Q(status='Бронь')))
    template_name = 'orders/actual_orders.html'
    context_object_name = 'all_orders'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class AddOrder(CreateView):
    model = Order
    template_name = 'orders/add_actual_order.html'
    form_class = OrderForm
    success_url = '/orders/actual'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

def derive(obj):
    import copy
    from django.contrib.admin.utils import NestedObjects
    from django.db import DEFAULT_DB_ALIAS
    from django.db.models.fields.related import ForeignKey
    """
        Derive a new model instance from previous one,
        and duplicate all related fields to point to the new instance
    """
    obj2 = copy.copy(obj)
    obj2.pk = None
    obj2.status = 'Актуальная'
    obj2.subclient = None
    obj2.truck = None
    obj2.driver = None
    obj2.subclient_cost = 0
    obj2.logist = None
    obj2.date_on_fact = None
    obj2.date_off_fact = None
    obj2.comment = None
    obj2.status_dispatcher = None
    obj2.problem_bool = False
    obj2.save()
    collector = NestedObjects(using=DEFAULT_DB_ALIAS)
    collector.collect([obj])
    collector.sort()
    related_models = collector.data.keys()
    data_snapshot = {}

    for key in collector.data.keys():
        data_snapshot.update({
            key: dict(
                zip(
                    [item.pk for item in collector.data[key]],
                    [item for item in collector.data[key]]
                )
            )
        })

    # Денис запомни этот кусок я изменил для исключения дубля DocFlow
    duplicate_order = related_models

    for model in duplicate_order:
        # Find all FKs on model that point to a related_model.
        fks = []
        for f in model._meta.fields:
            if isinstance(f, ForeignKey) and f.remote_field.model in related_models:
                fks.append(f)
        # Replace each `sub_obj` with a duplicate.
        if model not in collector.data:
            continue
        sub_objects = collector.data[model]
        for obj in sub_objects:
            for fk in fks:
                dupe_obj = copy.copy(obj)
                setattr(dupe_obj, fk.name, obj2)
                dupe_obj.pk = None
                dupe_obj.save()
        break
    return obj2

def CloneOrder(request, **kwargs):
    all_orders = Order.objects.all()
    obj = Order.objects.get(pk=kwargs['pk'])
    obj2 = derive(obj)

    return render(request, 'orders/clone-order.html', {'id': obj2.pk, 'id_old': obj.pk, 'all_orders': all_orders})

class DispatcherUpdateView(UpdateView):
    model = Order
    template_name = 'orders/dispatcher_update.html'
    form_class = OrderDispatcherForm
    success_url = '/orders/dispatcher'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class DispatcherView(ListView):
    model = Order
    queryset = Order.objects.filter(status='ТС назначен')
    template_name = 'orders/dispatcher.html'
    context_object_name = 'all_orders'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
class ReportsCloudView(ListView):
    model = Order
    queryset = Order.objects.filter((Q(status='ТС назначен') | Q(status='Выполнена')))
    
    template_name = 'orders/reports_cloud.html'
    context_object_name = 'all_orders'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
class ReportsFrahtView(ListView):
    model = Order
    queryset = Order.objects.all()
    
    template_name = 'orders/reports_sberfraht.html'
    context_object_name = 'all_orders'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
class SubclientDocument(PdfMixin, DetailView):
    model = Order
    template_name = 'orders/to_pdf/subclient_document.html'
    context_object_name = 'orders'

class ClientDocument1(PdfMixin, DetailView):
    model = Order
    template_name = 'orders/to_pdf/client_document1.html'
    context_object_name = 'orders'
    
class ClientDocument(DetailView):
    
    model = Order
    template_name = 'orders/to_pdf/client_document.html'
    context_object_name = 'orders'
    
class BillDocument(PdfMixin, DetailView):
    model = Order
    template_name = 'orders/to_pdf/bill.html'
    context_object_name = 'orders'
    
class YpdDocument(PdfMixin, DetailView):
    model = Order
    template_name = 'orders/to_pdf/ypd.html'
    context_object_name = 'orders'
    
class TtnDocument(DetailView):
    model = Order
    template_name = 'orders/to_pdf/ttn.html'
    context_object_name = 'orders'
    
    