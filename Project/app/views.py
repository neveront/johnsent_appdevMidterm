from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/home.html'

    # def get(self, request, *args, **kwargs):
    #     return HttpResponse("<h1>Hello World from view!</h1>")
