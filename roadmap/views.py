from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.urls import reverse
from user.models import User as user_model
from .models import Roadmap as roadmap_model
from django.contrib.auth import get_user_model
from . import models
from .forms import RoadmapNameForm, RoadmapCommentForm
from kbb_roadmap.views import is_authenticated
from notification.views import create_notification
# Create your views here.


def main(request):
    if not is_authenticated(request):
        return HttpResponseRedirect('/user/')

    if request.method == "GET":
        
        roadmaps = models.Roadmap.objects.all().order_by("status", "-created_at")
        
        context = {
            "roadmaps" : roadmaps
        } 
        
        return render(request, 'roadmap/roadmap.html', context=context)

def detail(request, id):
    if not is_authenticated(request):
        return HttpResponseRedirect('/user/')
    
    if request.method == "GET":

        roadmap = models.Roadmap.objects.filter(id=id)
        

        comments = models.RoadmapComment.objects.filter(roadmap=roadmap[0]) if len(roadmap) > 0 else None

        

        context = {
            "roadmap": roadmap[0] if len(roadmap) > 0 else None,
            "comments":comments,
            "form": RoadmapCommentForm()
        }
        # print(request.GET.get("id", None))
        # print(QueryDict(request.META["QUERY_STRING"]))
        return render(request, 'roadmap/roadmap_detail.html', context=context)
    
    elif request.method == "POST":


        form = RoadmapCommentForm(request.POST)

        if form.is_valid():

            comment = form.cleaned_data["comment"]
            user = get_object_or_404(get_user_model(), pk=request.user.id)
            roadmap = models.Roadmap.objects.filter(id=id)
            new_comment = models.RoadmapComment.objects.create(
                author = user,
                roadmap = roadmap[0] if len(roadmap) > 0 else None,
                comment = comment,
                child = None
            )

            new_comment.save()

            return HttpResponseRedirect(f'/roadmap/detail/{id}')


def new_roadmap(request):
    if not is_authenticated(request):
        return HttpResponseRedirect('/user/')
    
    if request.method == "GET":

        context = {
            "form": RoadmapNameForm()
        }
        return render(request, "roadmap/roadmap_create.html", context=context)
    
    elif request.method == "POST":
        
        form = RoadmapNameForm(request.POST)

        if form.is_valid():
        
            roadmap_name = form.cleaned_data["roadmap_name"]
            assignee_id = form.cleaned_data["assignee"]
        
            item = models.Roadmap.objects.filter(roadmap_name=roadmap_name)
            print(item)
            if len(item) == 0:
            #user = get_object_or_404(user_model, pk=request.user.id)
                user = get_object_or_404(get_user_model(), pk=request.user.id)
                assignee_user = get_object_or_404(get_user_model(), pk=assignee_id)

            
                new_roadmap = models.Roadmap.objects.create(
                    roadmap_name = roadmap_name,
                    status = "Pending",
                    requester = user,
                    assignee = assignee_user,
                )
                new_roadmap.save()

                # need to create notification
                create_notification({
                    "name" : "액션 요청",
                    "content" : f"{user.username}님이 새로운 로드맵을 등록하고 {assignee_user.username}님에게 할당하였습니다.",
                    "type" : "로드맵",
                    "link" : f"/roadmap/detail/{new_roadmap.pk}"
                })
                
        return HttpResponseRedirect(reverse("roadmap:main"))
        
        
            
        
        
