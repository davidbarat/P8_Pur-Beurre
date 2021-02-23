import os
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("index")


def index(request):
    template = loader.get_template("search/index.html")
    # return HttpResponse(message)
    return HttpResponse(template.render(request=request))

def password_reset_request(request):
	if os.environ['ENV'] == "DEV":
		domain = '127.0.0.1:8000/reset'

	else:
		domain = "167.99.212.10/reset"
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "search/password_reset_email.html"
					c = {
					"email":user.email,
					'domain': domain,
					'site_name': 'Purbeurre',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'contact@purbeurre.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(
        request=request, 
        template_name="search/password_reset_form.html", 
        context={"password_reset_form":password_reset_form})

def password_reset_done(request):
    template = loader.get_template("search/password_reset_complete.html")
    return HttpResponse(template.render(request=request))