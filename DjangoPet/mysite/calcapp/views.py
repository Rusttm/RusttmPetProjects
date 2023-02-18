from django.shortcuts import render

# Create your views here.
def index(request):
    """ return render page index """
    # return HttpResponse("Hello, world. You're at the mainapp index.")
    return render(request, 'calcapp/main.html', context={'name': 'Rusttm'})

from django.views.generic import TemplateView
class MainView(TemplateView):
    template_name = 'calcapp/main.html'