from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .utils import get_plot, get_func

def index(request):
    """ return render page index """
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'matplotapp/base.html', context={'name': 'Rusttm'})

def main_view(request):
    x = [i for i in range(-5,6)]
    y = [x_value**2 for x_value in x]
    chart = get_plot(x, y)
    return render(request, 'matplotapp/main.html', context={'chart': chart})

from .forms import UploadFunction
def func_view(request):

    if request.method == 'POST':
        form = UploadFunction(request.POST)
        function_string = request.POST.get('your_function')
        range_left = int(request.POST.get('left_edge'))
        range_right = int(request.POST.get('right_edge'))
        accuracy = int(request.POST.get('accuracy'))
        if range_left > range_right:
            range_left, range_right = range_right, range_left
        context = {
            'function_string': function_string,
            'range_left': range_left,
            'range_right': range_right,
            'accuracy': accuracy,
        }
        print(f'function_string is {function_string}')
        chart = get_func(function_string=function_string, range=(range_left, range_right), accuracy=accuracy)
        return render(request, 'matplotapp/main.html', {'chart': chart, 'form': form, 'context': context})

        # if form.is_valid():
        #     handle_uploaded_file(request.FILES['file'])
        #     return HttpResponseRedirect('/success/url/')

    else:
        form = UploadFunction()
        return render(request, 'matplotapp/main.html', {'form': form} )
