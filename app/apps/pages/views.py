from django.contrib.auth.views import LoginView
from django.template.response import TemplateResponse
from django.views import generic

from ..data.core.models import Country
from .utils import get_data_count


def home_view(request):
    """View for start page of web page."""
    context = {"count": get_data_count(), "countries": Country.objects.all()}

    return TemplateResponse(request, "home/home.html", context)


class RobotsView(generic.TemplateView):
    template_name = "pages/robots.txt"
    content_type = "text/plain"


class UserLoginView(LoginView):
    template_name = "pages/login.html"
