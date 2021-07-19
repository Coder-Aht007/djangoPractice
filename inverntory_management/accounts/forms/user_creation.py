from accounts.models import my_user
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2100)))
	class Meta:
		model = my_user
		fields = ("username", "email", "password1", "password2", 'date_of_birth')

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.date_of_birth = self.cleaned_data['date_of_birth']
		if commit:
			user.save()
		return user