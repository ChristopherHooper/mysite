from django.forms import ModelForm
from django import forms
import get_Events
from .models import Category
'''
class RankForm(forms.ModelForm):
	rank = forms.IntegerField()
	class Meta:
		model = Category
		fields = ['cId', 'short_name','events']
'''