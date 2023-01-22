from .models import Developer
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class developerList(ListView):
    model = Developer


class createDeveloper(CreateView):
    model = Developer
    fields = ['developerName', 'developerAge', 'developerSkill', 'developerExpYear']
    success_url = reverse_lazy('listDeveloper')


class updateDeveloper(UpdateView):
    model = Developer
    fields = ['developerName', 'developerAge', 'developerSkill', 'developerExpYear']
    success_url = reverse_lazy('listDeveloper')


class deleteDeveloper(DeleteView):
    model = Developer
    success_url = reverse_lazy('listDeveloper')
