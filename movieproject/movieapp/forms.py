from django import forms
from movieapp.models import movie

class movieform(forms.ModelForm):
	"""docstring for movieform"""
	class Meta:
		model=movie
		fields='__all__'