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
        files = FileUploaded.objects.all()
        # return HttpResponse()
        return render(request, 'filesapp/main.html', context={'documents': files})
    return JsonResponse({'post': 'false'})

from .models import DocumentUploaded
from .forms import DocumentForm
from django.urls import reverse
from django.http import HttpResponseRedirect

def doc_upload_view(request):
    # Handle file upload
    print("doc_upload_view requested")
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = DocumentUploaded(upload=request.FILES['upload'])
            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('filesapp_upload2'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = DocumentUploaded.objects.all()

    # Render list page with the documents and the form
    # return render_to_response(
    #     'webapp/list.html',
    #     {'documents': documents, 'form': form},
    #     context_instance=RequestContext(request)
    # )
    return render(request, 'filesapp/main.html', context={'documents': documents, 'form': form})
