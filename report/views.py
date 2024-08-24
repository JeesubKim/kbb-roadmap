from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .forms import ReportForm
from comments.forms import CommentForm
from comments.models import ReportComment, CommentLikes
# Create your views here.
from kbb_roadmap.views import is_authenticated

from . import models
def main(request):
    if not is_authenticated(request):
        return HttpResponseRedirect('/user/')

    if request.method == "GET":
        reports = models.Report.objects.all()
        
        context = {
            "reports":reports
        }
    return render(request, 'report/report.html', context=context)

def new_report(request):
    if not is_authenticated(request):
        return HttpResponseRedirect('/user/')

    if request.method == "GET":
        context = {
            "form": ReportForm()
        }
        return render(request, 'report/report_create.html', context=context)
    elif request.method == "POST":

        form = ReportForm(request.POST, request.FILES)
        
        if form.is_valid():
            print("is_valid")
            report_subject = form.cleaned_data["report_subject"]
            report_content = form.cleaned_data["report_content"]
            report_image = form.cleaned_data["report_image"]

            user = get_object_or_404(get_user_model(), pk=request.user.id)
            
            new_report = models.Report.objects.create(
                report_subject = report_subject,
                report_content = report_content,
                report_image = report_image,
                reporter =user
            )

            new_report.save()
        
    return HttpResponseRedirect(reverse("report:main"))

def detail(request, id):
    if request.method == "GET":
        
        report = list(models.Report.objects.filter(pk=id))

        from allauth.socialaccount.models import SocialAccount
        users = list(SocialAccount.objects.filter(user_id=report[0].reporter.pk))
        reporter = {"name":report[0].reporter.username, "picture":users[0].extra_data.get("picture")}
        report_data = {
            "report_id":id,
            "report_subject":report[0].report_subject,
            "report_content":report[0].report_content,
            "report_image":report[0].report_image,
            "reporter":reporter,
            "created_at":report[0].created_at,
        }
        

        comments = ReportComment.objects.filter(report=report[0])
        
        comments_list = []

        for comment in comments:
            # likes = list(models.RoadmapCommentLikes.objects.filter(comment=comment))
            likes = list(CommentLikes.objects.filter(comment=comment.comment))
            
            liked_user_list = []
            for like in likes:

                users = list(SocialAccount.objects.filter(user_id=like.user.pk))
                if len(users) > 0:
                    picture = users[0].extra_data.get ("picture")
                    liked_user_list.append({"username":like.user.username, "picture":picture})

            comments_list.append({"comment":comment.comment, "likes": liked_user_list})

        context = {
            "report": report_data,
            "comments":comments_list,
            "form": CommentForm()
        }
        return render(request, 'report/report_detail.html', context=context)
    
