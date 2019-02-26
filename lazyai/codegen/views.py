from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def home(request):
    """
    Renders the home.html template.
    """
    template = loader.get_template('codegen/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def generate(request):
    """
    Renders the generate.html template.
    """
    template = loader.get_template('codegen/generate.html')
    context = {}
    return HttpResponse(template.render(context, request))

def output(request):
    """
    Renders the output.html template.
    """
    template = loader.get_template('codegen/output.html')
    context = {}
    return HttpResponse(template.render(context, request))
