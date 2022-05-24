from django.shortcuts import render, redirect
from .forms import TruckForm
from .models import Truck
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .uploadings import UploadingFiles
from django.contrib import messages


class TrucksUpdateView(UpdateView):
    model = Truck
    template_name = 'trucks/add_truck.html'
    form_class = TruckForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class TrucksDetailView(DetailView):
    model = Truck
    template_name = 'trucks/details_truck.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class TrucksDeleteView(DeleteView):
    model = Truck
    success_url = '/trucks'
    template_name = 'trucks/delete-truck.html'
    context_object_name = 'trucks'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class Trucks(ListView):
    model = Truck
    template_name = 'trucks/trucks.html'
    context_object_name = 'all_trucks'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class AddTruck(CreateView):
    model = Truck
    template_name = 'trucks/add_truck.html'
    form_class = TruckForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
def upload_trucks(request):
    if request.POST:
        file = request.FILES['file']
        uploadind_file = UploadingFiles({"file": file})
        
        if uploadind_file:
            return redirect('trucks')
        else:
            messages.error(request, "Ошибка при импорте!")
        
    return render(request, 'trucks/upload_trucks.html', locals())