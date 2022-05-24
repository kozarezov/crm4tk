from django.urls import path
from . import views

urlpatterns = [
    path('', views.DoneOrders.as_view(), name='orders'),
    path('actual', views.ActualOrders.as_view(), name='actual-orders'),
    path('add', views.AddOrder.as_view(), name='add_order'),
    path('actual/<int:pk>/update', views.ActualOrdersUpdateView.as_view(), name="actual-orders-update"),
    path('<int:pk>/update', views.OrdersUpdateView.as_view(), name="orders-update"),
    path('<int:pk>/delete', views.OrdersDeleteView.as_view(), name="orders-delete"),
    path('<int:pk>/document', views.SubclientDocument.as_view(), name="orders-document"),
    path('<int:pk>/bill-document', views.BillDocument.as_view(), name="bill-document"),
    path('<int:pk>/client-document', views.ClientDocument.as_view(), name="client-document"),
    path('<int:pk>/client-document1', views.ClientDocument1.as_view(), name="client-document1"),
    path('<int:pk>/ypd-document', views.YpdDocument.as_view(), name="ypd-document"),
    path('<int:pk>/ttn-document', views.TtnDocument.as_view(), name="ttn-document"),
    path('dispatcher', views.DispatcherView.as_view(), name="dispatcher"),
    path('dispatcher/<int:pk>', views.DispatcherUpdateView.as_view(), name="dispatcher-update"),
    path('reports_cloud', views.ReportsCloudView.as_view(), name='reports_cloud'),
    path('reports_sberfraht', views.ReportsFrahtView.as_view(), name='reports_sberfraht'),
    path('<int:pk>/clone', views.CloneOrder, name="orders-clone"),
]