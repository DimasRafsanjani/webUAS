from django.urls import path
from . import views

urlpatterns = [
    path('', views.mahasiswaList.as_view(), name="listMahasiswa"),
    path('createMahasiswa/', views.createMahasiswa.as_view(), name="createMahasiswa"    ),
    path('updateMahasiswa/<int:pk>', views.updateMahasiswa.as_view(), name="updateMahasiswa"),
    path('deleteMahasiswa/<int:pk>', views.deleteMahasiswa.as_view(), name="deleteMahasiswa")
]
