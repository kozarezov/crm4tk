from django.db.models import fields
from django.shortcuts import render, redirect
from .forms import ClientForm
from .models import Client
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .uploadings import UploadingFiles
from django.contrib import messages


class ClientsUpdateView(UpdateView):
    model = Client
    template_name = 'clients/add_client.html'
    form_class = ClientForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class ClientsDetailView(DetailView):
    model = Client
    template_name = 'clients/details_client.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class ClientsDeleteView(DeleteView):
    model = Client
    success_url = '/clients'
    template_name = 'clients/delete-client.html'
    context_object_name = 'clients'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class Clients(ListView):
    model = Client
    template_name = 'clients/clients.html'
    context_object_name = 'all_clients'
    
    method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class AddClient(CreateView):
    model = Client
    template_name = 'clients/add_client.html'
    form_class = ClientForm
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
def upload_clients(request):
    if request.POST:
        file = request.FILES['file']
        uploadind_file = UploadingFiles({"file": file})
        
        if uploadind_file:
            return redirect('clients')
        else:
            messages.error(request, "Ошибка при импорте!")
        
    return render(request, 'clients/upload_clients.html', locals())