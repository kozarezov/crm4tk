from django.urls import path
from . import views

urlpatterns = [
    path('', views.Addresses.as_view(), name='addresses'),
    path('add', views.AddAddress.as_view(), name='add_address'),
    path('<int:pk>', views.AddressesDetailView.as_view(), name="addresses-detail"),
    path('<int:pk>/update', views.AddressesUpdateView.as_view(), name="addresses-update"),
    path('<int:pk>/delete', views.AddressesDeleteView.as_view(), name="addresses-delete"),
     path('upload', views.upload_addresses, name="addresses-upload"),
]