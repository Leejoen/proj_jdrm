from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'audits/audits.html')

def audit(request):
    return render(request, 'audits/audit.html')
