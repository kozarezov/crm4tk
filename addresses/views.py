from django.shortcuts import render, redirect
from .forms import AddressForm
from .models import Address
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .uploadings import UploadingFiles
from django.contrib import messages

class AddressesUpdateView(UpdateView):
    model = Address
    template_name = 'addresses/add_address.html'
    form_class = AddressForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class AddressesDetailView(DetailView):
    model = Address
    template_name = 'addresses/details-address.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

class AddressesDeleteView(DeleteView):
    model = Address
    success_url = '/addresses'
    template_name = 'addresses/delete-address.html'
    context_object_name = 'addresses'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)


class Addresses(ListView):
    model = Address
    template_name = 'addresses/addresses.html'
    context_object_name = 'all_addresses'
    
    method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
        context = super(Addresses, self).get_context_data(**kwargs)
        return context

class AddAddress(CreateView):
    model = Address
    template_name = 'addresses/add_address.html'
    form_class = AddressForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)
   
def upload_addresses(request):
    if request.POST:
        file = request.FILES['file']
        uploadind_file = UploadingFiles({"file": file})
        
        if uploadind_file:
            return redirect('addresses')
        else:
            messages.error(request, "Ошибка при импорте!")
        
    return render(request, 'addresses/upload_addresses.html', locals())