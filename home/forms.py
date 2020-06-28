from django.forms import ModelForm
from .models import *


class Create(ModelForm):
	class Meta:
		model = client
		fields = '__all__'
