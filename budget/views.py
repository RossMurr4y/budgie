from django.shortcuts import render

# Create your views here
def index(request):
    """The home page for Budgie Budget"""
    return render(request, 'index.html')
