from django.urls import path
from . import views

urlpatterns = [
    path('', views.DocFlowList.as_view(), name='docflow'),
    path('archive', views.DocArchiveFlowList.as_view(), name='docflow-archive'),
    path('<int:pk>', views.OrdersDetailView.as_view(), name="orders-detail"),
    path('<int:pk>/update', views.DocFlowUpdate.as_view(), name='docflow-update'),
]