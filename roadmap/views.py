from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

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
        from allauth.socialaccount.models import SocialAccount
        roadmap = models.Roadmap.objects.filter(id=id)
        requesters = list(SocialAccount.objects.filter(user_id=roadmap[0].requester.pk))
        assignees = list(SocialAccount.objects.filter(user_id=roadmap[0].assignee.pk))

        requester = {"name":roadmap[0].requester.username, "picture":requesters[0].extra_data.get("picture")}
        assignee = {"name":roadmap[0].assignee.username, "picture":assignees[0].extra_data.get("picture")}
        
        registration_agrees = list(models.RoadmapRegistrationAgreement.objects.filter(roadmap=roadmap[0]))
        completion_agrees = list(models.RoadmapCompletionAgreement.objects.filter(roadmap=roadmap[0]))
        
        users = list(get_user_model().objects.filter(is_superuser=False))
        criteria = len(users)/2
        registration_agreed_list = [{"name": registration_agrees[0].user.username, "picture": user.extra_data.get("picture")}for user in list(SocialAccount.objects.filter(user_id=registration_agrees[0].user.pk))]  if len(registration_agrees) > 0 else []
        completion_agreed_list = [{"name": completion_agrees[0].user.username, "picture": user.extra_data.get("picture")}for user in list(SocialAccount.objects.filter(user_id=completion_agrees[0].user.pk))] if len(completion_agrees) > 0 else []
        regi_rate = len(registration_agreed_list) / criteria
        comp_rate = len(completion_agreed_list) / criteria
        roadmap_data = {
            "roadmap_id":id,
            "roadmap_name":roadmap[0].roadmap_name,
            "status":roadmap[0].status,
            "created_at":roadmap[0].created_at,
            "updated_at":roadmap[0].updated_at,
            "requester": requester,
            "assignee": assignee,
            "registration_agrees": {
                "criteria":criteria,
                "percentage": regi_rate * 100 if regi_rate <=1 else 100,
                "total":len(registration_agreed_list),
                "list":registration_agreed_list
            },
            "completion_agrees": {
                "criteria":criteria,
                "percentage": comp_rate * 100  if regi_rate <=1 else 100,
                "total":len(completion_agreed_list),
                "list":completion_agreed_list
            }
        }

        

        comments = models.RoadmapComment.objects.filter(roadmap=roadmap[0]) if len(roadmap) > 0 else None

        comments_list = []
        for comment in comments:
            likes = list(models.RoadmapCommentLikes.objects.filter(comment=comment))

            
            liked_user_list = []
            for like in likes:

                users = list(SocialAccount.objects.filter(user_id=like.user.pk))
                if len(users) > 0:
                    picture = users[0].extra_data.get("picture")
                    liked_user_list.append({"username":like.user.username, "picture":picture})

            comments_list.append({"comment":comment, "likes": liked_user_list})


        context = {
            "roadmap": roadmap_data,
            "comments":comments_list,
            "form": RoadmapCommentForm()
        }
        
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
            
            if len(item) == 0:
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
        
        
            
        
        
def likes(request, id):
    
    if not is_authenticated(request):
        return HttpResponseRedirect('/user/')
    
    if request.method == "GET":

        from allauth.socialaccount.models import SocialAccount

        
        
        
        comment = list(models.RoadmapComment.objects.filter(pk=id))
        likes = list(models.RoadmapCommentLikes.objects.filter(comment=comment[0]))

        result = []
        for like in likes:
            users = list(SocialAccount.objects.filter(user_id=like.user.pk))
            picture = users[0].extra_data.get("picture")

            result.append({
                "name":like.user.username,
                "picture": picture
            })
        
        return JsonResponse({"success":True, "result": result})
    

    elif request.method == "POST":
        user = get_object_or_404(get_user_model(), pk=request.user.id)
        comments = list(models.RoadmapComment.objects.filter(pk=id))

        likes = models.RoadmapCommentLikes.objects.filter(comment=comments[0], user=user)
        roadmap_id = comments[0].roadmap.pk
        
        if len(likes) == 0:
            new_likes = models.RoadmapCommentLikes.objects.create(
                user = user,
                comment = comments[0]
            )
            new_likes.save()

        else:
            item = likes.delete()
            
        return HttpResponseRedirect(reverse("roadmap:detail", args=[roadmap_id]))
    
def agree(request, id, type):
    if request.method == "POST":
        user = get_object_or_404(get_user_model(), pk=request.user.id)
        roadmap = models.Roadmap.objects.filter(pk=id)
        target = None
        if type == "registration":
            target = models.RoadmapRegistrationAgreement.objects
            

        elif type == "completion":
            target = models.RoadmapCompletionAgreement.objects

        agreements = target.filter(roadmap=roadmap[0], user=user)
        len_agreement = len(agreements)
        if len_agreement == 0:
            new_agreement = target.create(
                roadmap = roadmap[0],
                user = user
            )
            new_agreement.save()        
            len_agreement += 1
        else:
            agreements.delete()
            len_agreement -= 1
        

        users = get_user_model().objects.filter(is_superuser=False)
        criteria = len(users) / 2
        
        if len_agreement >= criteria:
            
            if type == "registration":
                roadmap.update(status="In Progress")
            elif type == "completion":
                roadmap.update(status="Done")
        else:
            if type == "registration":
                if roadmap[0].status == "In Progress":
                    roadmap.update(status="Pending")
                
            elif type == "completion":
                if roadmap[0].status == "Done":
                    roadmap.update(status="In Review")
        
        

        
        
        # regi_rate = len(registration_agreed_list) / criteria
        # comp_rate = len(completion_agreed_list) / criteria
        return HttpResponseRedirect(reverse("roadmap:detail", args=[id]))
def complete(request, id):
    if request.method == "POST":
        user = get_object_or_404(get_user_model(), pk=request.user.id)
        roadmap = models.Roadmap.objects.filter(pk=id)
        if user == list(roadmap)[0].assignee:
            roadmap.update(status="In Review")
        return HttpResponseRedirect(reverse("roadmap:detail", args=[id]))
"""
path('detail/</likes/<str:id>/', views.likes, name="likes")
'detail/<str:id>/agreement/<str:type>'
'detail/<str:id>/agreement/registration'
'detail/<str:id>/agreement/completion'
"""