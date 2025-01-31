
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('api/', include('faq.urls')),  # API endpoints
    path('', include('faq.urls')),  
]