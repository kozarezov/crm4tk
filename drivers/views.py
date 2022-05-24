from distutils.command.upload import upload
from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .forms import DriverForm
from .models import Driver
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .uploadings import UploadingFiles
from django.contrib import messages

class DriversUpdateView(UpdateView):
    model = Driver
    template_name = 'drivers/add_driver.html'
    form_class = DriverForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class DriversDetailView(DetailView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    model = Driver
    template_name = 'drivers/details_driver.html'

class DriversDeleteView(DeleteView):
    model = Driver
    success_url = '/drivers'
    template_name = 'drivers/delete-driver.html'
    context_object_name = 'drivers'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class Drivers(ListView):
    model = Driver
    template_name = 'drivers/drivers.html'
    context_object_name = 'all_drivers'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
    
class AddDriver(CreateView):
    model = Driver
    template_name = 'drivers/add_driver.html'
    form_class = DriverForm
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
def upload_drivers(request):
    if request.POST:
        file = request.FILES['file']
        uploadind_file = UploadingFiles({"file": file})
        
        if uploadind_file:
            return redirect('drivers')
        else:
            messages.error(request, "Ошибка при импорте!")
        
    return render(request, 'drivers/upload_drivers.html', locals())