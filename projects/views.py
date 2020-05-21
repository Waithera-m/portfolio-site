from django.shortcuts import render
from django.views import generic
import datetime
from .models import Repo

# Create your views here.
def index(request):

    """
    view function returns the landing page
    """
    return render(request,'all-projects/index.html')

def projects(request):

    """
    view function returns template that displays all repos
    """
    projects = Repo.objects.all()

    return render(request,'repos.html',{'projects':projects})

class DetailView(generic.DetailView):

    """
    view function returns template that displays information on a single project
    """
    model = Repo
    template_name = 'all-projects/detail.html'
    context_object_name = 'project'