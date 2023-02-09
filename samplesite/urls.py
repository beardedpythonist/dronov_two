from django.contrib import admin
from django.urls import path, include
from bboard.views import index2



urlpatterns = [path('bboard/',
            include('bboard.urls')),
            path('', index2),
            path('admin/', admin.site.urls)]

