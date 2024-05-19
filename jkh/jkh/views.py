from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "main.html"


class AdviceView(TemplateView):
    template_name = "advice.html"
