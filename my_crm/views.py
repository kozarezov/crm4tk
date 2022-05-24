from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .forms import LoginUserForm, FileStorageForm, ProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView
from .models import FileStorage
from django.db import transaction
from .dashboard_utils import Utils
import json


@login_required
def index(request):
    util = Utils()
    day_margin, day_gross, day_count_done, day_count_not_done = util.day_indicators()
    month_margin, month_gross, month_count_done, month_count_not_done = util.month_indicators()
    day_margin_percent, day_gross_percent, day_count_done_percent, day_count_not_percent = util.percent_of_day_indicators()
    clients_array, total_orders = util.client_indicators()
    if (day_count_done + day_count_not_done) <= 0:
        conversion = 100
    else:
        conversion = round(day_count_done / (day_count_done + day_count_not_done) * 100)
    data_count = util.all_orders_in_month()
    data_count_month = util.all_orders_in_year()
    data_count_weekday = util.all_orders_in_weekday()
    
    context = {
        'day_margin': day_margin, 
        'month_margin': month_margin,
        'day_margin_percent': day_margin_percent,
        'day_gross': day_gross, 
        'month_gross': month_gross,
        'day_gross_percent': day_gross_percent,
        'day_count_done': day_count_done, 
        'month_count_done': month_count_done,
        'day_count_done_percent': day_count_done_percent,
        'day_count_not_done': day_count_not_done, 
        'month_count_not_done': month_count_not_done,
        'day_count_not_percent': day_count_not_percent,
        'conversion': conversion,
        'data_count' : json.dumps(data_count),
        'data_count_month' : json.dumps(data_count_month),
        'data_count_weekday' : json.dumps(data_count_weekday),
        'clients_array': json.dumps(clients_array),
        'total_orders': json.dumps(total_orders),
        
    }
    return render(request, 'my_crm/index.html', context={'data': context})

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'my_crm/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('index')

def LogoutUser(request):
    logout(request)
    return redirect('login')

def error_404_view(request, exception):
    return render(request, 'my_crm/error404.html')

def error_500_view(request):
    return render(request, 'my_crm/error500.html')

class FileManager(ListView):
    model = FileStorage
    template_name = 'my_crm/file-storage.html'
    form_class = FileStorageForm
    context_object_name = 'all_documents'
    
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('settings')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'my_crm/settings.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    
