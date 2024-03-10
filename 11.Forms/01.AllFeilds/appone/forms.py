from django.forms import ModelForm
from .models import Company

class CustomerForm(ModelForm):
	class Meta:
		model = Company
		fields = '__all__'