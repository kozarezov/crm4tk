from django.shortcuts import render
from django.views.generic import ListView, CreateView
from orders.models import Order
from django.contrib.auth.models import User
from .models import Ttn
from .forms import TtnForm

class ActualOrdersForSubclient(ListView):
    model = Order
    template_name = 'for_subclient/actual_orders_for_sublient.html'
    context_object_name = 'all'
    
    def get_queryset(self):
        queryset = {'all_orders': Order.objects.filter(status='Актуальная'), 
                    'all_user': User.objects.all(),}
        return queryset

class TtnCreate(CreateView):
    model = Ttn
    template_name = 'for_subclient/ttn-form.html'
    form_class = TtnForm

