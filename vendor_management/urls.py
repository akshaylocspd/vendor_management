from django.contrib import admin
from django.urls import path, include
from django.conf import *
from django.conf.urls.static import static
from accounts.views import *  # Import your view
from django.urls import re_path, path

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('api/', include('accounts.urls')),
    path('api/', include('purchase_Orders.urls')),
]

