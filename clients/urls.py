from django.urls import path
from . import views

urlpatterns = [
    path('', views.Clients.as_view(), name='clients'),
    path('add', views.AddClient.as_view(), name='add_client'),
    path('<int:pk>', views.ClientsDetailView.as_view(), name="clients-detail"),
    path('<int:pk>/update', views.ClientsUpdateView.as_view(), name="clients-update"),
    path('<int:pk>/delete', views.ClientsDeleteView.as_view(), name="clients-delete"),
    path('upload', views.upload_clients, name="clients-upload"),
]