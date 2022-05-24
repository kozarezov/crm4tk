from django.urls import path
from . import views

urlpatterns = [
    path('', views.Trucks.as_view(), name='trucks'),
    path('add', views.AddTruck.as_view(), name='add_truck'),
    path('<int:pk>', views.TrucksDetailView.as_view(), name="trucks-detail"),
    path('<int:pk>/update', views.TrucksUpdateView.as_view(), name="trucks-update"),
    path('<int:pk>/delete', views.TrucksDeleteView.as_view(), name="trucks-delete"),
    path('upload', views.upload_trucks, name="trucks-upload"),
]