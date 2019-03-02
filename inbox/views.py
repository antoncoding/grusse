from django.shortcuts import render
from django.template import loader

# for testing
from django.http import HttpResponse

# Create your views here.

def inbox(request):
    return render(request, 'inbox.html')

def compose(request):
    return render(request, 'compose.html')

# render Template page
# def template(request):  
#     context = {'name': 'qq'}
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render(context, request))