from django.shortcuts import render
from django.views import generic

# Create your views here.
def index(request):

    """
    view function returns the landing page
    """
    return render(request,'all-projects/index.html')
