from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from kbb_roadmap.views import is_authenticated
from . import models

from .forms import CommentForm
# Create your views here.



def main(request):
    if request.method == "POST":

        form = CommentForm(request.POST)
        
        if form.is_valid():

            comment = form.cleaned_data["comment"]
            type = request.POST.get("type")
            id = request.POST.get("id")
            user = get_object_or_404(get_user_model(), pk=request.user.id)
            
            new_comment = models.Comment.objects.create(
                author = user,
                comment = comment
            )

            new_comment.save()
            print(type)
            if type == "roadmap":
                roadmap = list(models.Roadmap.objects.filter(id=id))
                
                new_roadmap_comment = models.RoadmapComment.objects.create(
                    roadmap=roadmap[0],
                    comment=new_comment
                )

                new_roadmap_comment.save()
                url = reverse("roadmap:detail", args=[id])
            elif type == "report":
                report = list(models.Report.objects.filter(id=id))
                new_report_comment = models.ReportComment.objects.create(
                    report=report[0],
                    comment=new_comment
                )
                new_report_comment.save()
                url = reverse("report:detail", args=[id])
            
            

            return HttpResponseRedirect(url)

    return render()




        
def likes(request, type, id):
    
    if not is_authenticated(request):
        return HttpResponseRedirect('/user/')
    
    if request.method == "GET":

        from allauth.socialaccount.models import SocialAccount

        
        comment = models.Comment.objects.filter(pk=id)
        # if type == "roadmap":
        #     comment = list(models.RoadmapComment.objects.filter(pk=id))
        # elif type == "report":
        #     comment = list(models.ReportComment.objects.filter(pk=id))
        
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
        comments = list(models.Comment.objects.filter(pk=id))

        likes = models.CommentLikes.objects.filter(comment=comments[0], user=user)
        url=""
        if type == "roadmap":
            link = list(models.RoadmapComment.objects.filter(comment=comments[0]))
            url = reverse("roadmap:detail", args=[link[0].roadmap.pk])
            

        elif type == "report":
            link = list(models.ReportComment.objects.filter(comment=comments[0]))
            url = reverse("report:detail", args=[link[0].report.pk])
            

        
        if len(likes) == 0:
            new_likes = models.CommentLikes.objects.create(
                user = user,
                comment = comments[0]
            )
            new_likes.save()

        else:
            item = likes.delete()
            
        return HttpResponseRedirect(url)
    


def get_comment_list(comments, user_id):
    from allauth.socialaccount.models import SocialAccount
    comments_list = []

    for comment in comments:
        # likes = list(models.RoadmapCommentLikes.objects.filter(comment=comment))
        likes = list(models.CommentLikes.objects.filter(comment=comment.comment))
        
        liked_user_list = []
        is_liked = False
        for like in likes:

            users = list(SocialAccount.objects.filter(user_id=like.user.pk))
            if len(users) > 0:
                picture = users[0].extra_data.get ("picture")
                liked_user_list.append({"username":like.user.username, "picture":picture})
                if like.user.pk == user_id:
                    is_liked=True

        comments_list.append({"comment":comment.comment, "likes": liked_user_list, "is_liked":is_liked})

    return comments_list
