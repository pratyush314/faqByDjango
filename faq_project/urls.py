
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('faq.urls')),  
    path('api/', include('faq.urls')),  
    path('admin/', admin.site.urls),
]