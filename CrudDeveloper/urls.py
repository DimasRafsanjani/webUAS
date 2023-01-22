from django.urls import path
from . import views

urlpatterns = [
    path('', views.developerList.as_view(), name="listDeveloper"),
    path('createDeveloper/', views.createDeveloper.as_view(), name="createDeveloper"),
    path('updateDeveloper/<int:pk>', views.updateDeveloper.as_view(), name="updateDeveloper"),
    path('deleteDeveloper/<int:pk>', views.deleteDeveloper.as_view(), name="deleteDeveloper")
]
