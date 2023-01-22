from .models import Mahasiswa
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class mahasiswaList(ListView):
    model = Mahasiswa


class createMahasiswa(CreateView):
    model = Mahasiswa
    fields = ['mahasiswaName', 'mahasiswaAge', 'mahasiswaSkill']
    success_url = reverse_lazy('listMahasiswa')


class updateMahasiswa(UpdateView):
    model = Mahasiswa
    fields = ['mahasiswaName', 'mahasiswaAge', 'mahasiswaSkill']
    success_url = reverse_lazy('listMahasiswa')


class deleteMahasiswa(DeleteView):
    model = Mahasiswa
    success_url = reverse_lazy('listMahasiswa')
