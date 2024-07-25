from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from user.models import User as user_model
from . import models
from .forms import RoadmapNameForm
# Create your views here.


def main(request):
    is_authenticated(request)

    return render(request, 'roadmap/roadmap.html')



def new_roadmap(request):
    is_authenticated(request)
    print("new_roadmap", request.method)
    if request.method == "GET":

        context = {
            "form": RoadmapNameForm()
        }
        return render(request, "roadmap/roadmap_create.html", context=context)
    
    elif request.method == "POST":
        print("you came here")
        form = RoadmapNameForm(request.POST)

        if form.is_valid():
            print("form is valid")
            roadmap_name = form.cleaned_data["roadmap_name"]
            assignee = form.cleaned_data["assignee"]
            print(roadmap_name, assignee)
            user = get_object_or_404(user_model, pk=request.user.id)


            print(user)
            new_roadmap = models.Roadmap.objects.create(
                roadmap_name = roadmap_name,
                status = "Pending",
                requester = user,
                assignee = assignee,
            )
            new_roadmap.save()
        return render(request, 'roadmap/roadmap.html')
        
            
        
        
def is_authenticated(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/user/login')
    
        
