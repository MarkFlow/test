from django.shortcuts import render

# Create your views here.
def index(request):
    site = 'world!'
    return render(request, 'index.html', context={'words': site})