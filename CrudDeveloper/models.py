from django.db import models
from django.urls import reverse


class Developer(models.Model):
    developerName = models.CharField(max_length=150, null=False)
    developerAge = models.CharField(max_length=200, null=False)
    developerSkill = models.CharField(max_length=150, null=False)
    developerExpYear = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.developerName

    def get_absolute_url(self):
        return reverse('updateDeveloper', kwargs={'pk': self.pk})
