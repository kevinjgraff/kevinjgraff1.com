from django.shortcuts import render
from django import forms
from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	message = forms.CharField(required=True)


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		#if not extension == "edu":
			#raise forms.ValidationError("Please use a valid .EDU email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

