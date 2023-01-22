from django.db import models
from django.urls import reverse


class Mahasiswa(models.Model):
    mahasiswaName = models.CharField(max_length=150)
    mahasiswaAge = models.CharField(max_length=200)
    mahasiswaSkill = models.CharField(max_length=150)

    def __str__(self):
        return self.mahasiswaAge

    def get_absolute_url(self):
        return reverse('updateMahasiswa', kwargs={'pk': self.pk})
