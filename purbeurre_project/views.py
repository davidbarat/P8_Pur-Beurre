from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("index")


def index(request):
    template = loader.get_template("search/index.html")
    # return HttpResponse(message)
    return HttpResponse(template.render(request=request))
