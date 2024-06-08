from django.shortcuts import render
from django.template.defaulttags import register
from django.http import HttpResponse

@register.filter
def get_name_url(path):
    return path.replace('/', '')

def main(request):
    return render(request, 'main/main.html')
