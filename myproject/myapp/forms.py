from django import forms
from .models import Datas

class Crudoperation(forms.ModelForm):
    class Meta:
        model = Datas
        fields = ['Name','Age','Address','Contact','Mail']


    def clean(self):
        super(Crudoperation,self).clean()


