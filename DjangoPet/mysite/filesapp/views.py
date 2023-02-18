from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from .models import FileUploaded

def index(request):
    """ return render page index """
    # return HttpResponse("Hello, world. You're at the polls index.")
    documents = FileUploaded.objects.all()
    return render(request, 'filesapp/main.html', context={'name': 'Rusttm', 'documents': documents})

class MainView(TemplateView):
    template_name = 'filesapp/main.html'

def file_upload_view(request):
    print(request.FILES)

    if request.method == 'POST':
        my_file = request.FILES.get('file')
        FileUploaded.objects.create(upload=my_file)
        documents = FileUploaded.objects.all()
        # return HttpResponse()
        return render(request, 'filesapp/main.html', context={'documents': documents})
    return JsonResponse({'post':'false'})

