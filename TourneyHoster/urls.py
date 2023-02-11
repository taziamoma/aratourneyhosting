from django.contrib import admin
from django.urls import path, include

import hoster

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hoster.urls')),
    path('', include('registration.urls')),
]
