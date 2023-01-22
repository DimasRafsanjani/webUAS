from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

from .models import Mahasiswa


class Mahasiswamaster(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['mahasiswaName', 'mahasiswaAge', 'mahasiswaSkill']