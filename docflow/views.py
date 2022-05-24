from .forms import DocFlowForm, OrderDetailForm
from .models import DocFlow
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.shortcuts import render

class DocFlowList(ListView):
    model = DocFlow
    queryset = DocFlow.objects.filter(order__status='Выполнена').filter(~Q(status='Оплачен клиентом'))
    template_name = 'docflow/documents.html'
    context_object_name = 'all_orders'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
class DocFlowUpdate(UpdateView):
    model = DocFlow
    template_name = 'docflow/update_documents.html'
    form_class = DocFlowForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
class DocArchiveFlowList(ListView):
    model = DocFlow
    queryset = DocFlow.objects.filter(Q(status='Оплачен клиентом'))
    template_name = 'docflow/documents.html'
    context_object_name = 'all_orders'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
class OrdersDetailView(UpdateView):
    model = DocFlow
    template_name = 'docflow/details_order.html'
    form_class = OrderDetailForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
def delete_bd(request):
    DocFlow().delete_everything()
    DocFlow().drop_table()
    
    return render(request, "Удалено")
