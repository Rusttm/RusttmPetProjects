from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """ return render page index """
    # return HttpResponse("Hello, world. You're at the polls index.")
    documents = Document.objects.all()

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'webapp/index.html', context={'documents': documents})

def example_page(request):
    """ return render page index """
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {
        'num_books': 12345,
        'num_instances': 6666,
        'num_instances_available': 7777,
        'num_authors': 12,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'webapp/example.html', context=context)



# Create your views here.
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
import sys
sys.path.insert(0, '/Users/johnlennon/RusttmGDrive/Python/GeekBrains/web/GBsWEB/django/mysite/webapp/')
from myuploader import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'webapp/myform.html', {'form': form} )

import webapp
from webapp.models import Document
from webapp.forms import DocumentForm
# from django.core.urlresolvers import reverse
from django.urls import reverse


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    # return render_to_response(
    #     'webapp/list.html',
    #     {'documents': documents, 'form': form},
    #     context_instance=RequestContext(request)
    # )
    return render(request, 'webapp/list.html', context={'documents': documents, 'form': form})