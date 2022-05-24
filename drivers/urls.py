from django.urls import path
from . import views

urlpatterns = [
    path('', views.Drivers.as_view(), name='drivers'),
    path('add', views.AddDriver.as_view(), name='add_driver'),
    path('<int:pk>', views.DriversDetailView.as_view(), name="drivers-detail"),
    path('<int:pk>/update', views.DriversUpdateView.as_view(), name="drivers-update"),
    path('<int:pk>/delete', views.DriversDeleteView.as_view(), name="drivers-delete"),
    path('upload', views.upload_drivers, name="drivers-upload"),
]