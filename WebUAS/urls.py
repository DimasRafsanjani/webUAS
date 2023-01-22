from django.contrib import admin
from django.urls import path, include

from CrudMahasiswa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('CrudMahasiswa.urls')),
]