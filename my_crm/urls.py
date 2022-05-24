from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('for_subclient.urls')),
    path('index', views.index, name='index'),
    path('file-storage', views.FileManager.as_view(), name='file-storage'),
    path('settings', views.update_profile, name='settings'),
    path('accounts/login/', views.LoginUser.as_view(), name="login"),
    path('accounts/logout/', views.LogoutUser, name="logout"),
    path('trucks/', include('trucks.urls')),
    path('drivers/', include('drivers.urls')),
    path('clients/', include('clients.urls')),
    path('addresses/', include('addresses.urls')),
    path('orders/', include('orders.urls')),
    path('documents/', include('docflow.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

handler404 = 'my_crm.views.error_404_view'
handler500 = 'my_crm.views.error_500_view'