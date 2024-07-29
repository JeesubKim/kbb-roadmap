from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from user.models import User as user_model
from .models import Roadmap as roadmap_model
from django.contrib.auth import get_user_model
from . import models
from .forms import RoadmapNameForm
# Create your views here.


def main(request):
    is_authenticated(request)

    if request.method == "GET":
        
        roadmaps = models.Roadmap.objects.all()
        
        context = {
            "roadmaps" : roadmaps
        }
        
        return render(request, 'roadmap/roadmap.html', context=context)



def new_roadmap(request):
    is_authenticated(request)
    
    if request.method == "GET":

        context = {
            "form": RoadmapNameForm()
        }
        return render(request, "roadmap/roadmap_create.html", context=context)
    
    elif request.method == "POST":
        
        form = RoadmapNameForm(request.POST)

        if form.is_valid():
        
            roadmap_name = form.cleaned_data["roadmap_name"]
            assignee = form.cleaned_data["assignee"]
        
            #user = get_object_or_404(user_model, pk=request.user.id)
            user = get_object_or_404(get_user_model(), pk=request.user.id)
        

        
            new_roadmap = models.Roadmap.objects.create(
                roadmap_name = roadmap_name,
                status = "Pending",
                requester = user,
                assignee = user,
            )
            new_roadmap.save()
        return HttpResponseRedirect(reverse("roadmap:main"))
        
        
            
        
        
def is_authenticated(request):
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/user/login')
    
        
