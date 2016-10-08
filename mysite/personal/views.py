from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, SignUpForm


def index(request):
	return render(request, 'personal/home.html')

def basic(request):
	title='Welcome'
	form = SignUpForm(request.POST or None)

	context = {
		"title": title,
		"form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name

		instance.save()
		context = {
			"title": "Thank you"
		}

	return render(request,"basic.html",context)

def about(request):
	return render(request, 'personal/about.html')

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#for key in form.cleaned_data.iteritems():
		#	print key, value
			#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		#print email, message, full_name
		subject = 'Site Contact Form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "%s: %s via %s"%(
				form_full_name, 
				form_message, 
				form_email)

		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				fail_silently=False)

		return HttpResponseRedirect('/thank-you/')
	context = {
		"form": form,
	}
	return render(request, "personal/forms.html", context)

def thankyou(request):
	return render(request, 'personal/thankyou.html')