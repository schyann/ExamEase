from django.contrib import admin
from django.urls import path,include
from APP.views import home

urlpatterns = [
    path("admin/", admin.site.urls),     
    path('',include('APP.urls')),
    # path("user/",include('django.contrib.auth.urls')),
    
]
