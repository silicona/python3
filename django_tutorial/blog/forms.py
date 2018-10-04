from django import forms

# Documentacion: https://docs.djangoproject.com/en/2.1/topics/forms/

from .models import *

class FormPublicar(forms.ModelForm):

	class Meta:

		model = Post
		fields = ('titulo', 'texto')


class FormComentar( forms.ModelForm ):

	class Meta:

		model = Comentario
		fields = ('texto',)