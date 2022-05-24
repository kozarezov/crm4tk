from django.urls import path
from . import views

urlpatterns = [
    path('', views.ActualOrdersForSubclient.as_view(), name='for_subclient'),
    path('ttn', views.TtnCreate.as_view(), name='ttn'),
]