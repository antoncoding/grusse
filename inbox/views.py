from django.shortcuts import render
from django.template import loader

# for testing
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("inbox.index .")

# render Template page
def template(request):  
    context = {'name': 'qq'}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))