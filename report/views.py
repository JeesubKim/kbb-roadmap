from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .forms import ReportForm
# Create your views here.
from kbb_roadmap.views import is_authenticated
from .forms import ReportForm
from . import models
def main(request):
    is_authenticated(request)

    if request.method == "GET":
        reports = models.Report.objects.all()
        print("디버깅>>>>>>>>>>>>>>>>>>>>",reports)
        context = {
            "reports":reports
        }
    return render(request, 'report/report.html', context=context)

def new_report(request):
    is_authenticated(request)

    if request.method == "GET":
        context = {
            "form": ReportForm()
        }
        return render(request, 'report/report_create.html', context=context)
    elif request.method == "POST":

        form = ReportForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            print("is_valid")
            report_subject = form.cleaned_data["report_subject"]
            report_content = form.cleaned_data["report_content"]
            report_image = form.cleaned_data["report_image"]

            user = get_object_or_404(get_user_model(), pk=request.user.id)
            
            print(user)
            new_report = models.Report.objects.create(
                report_subject = report_subject,
                report_content = report_content,
                report_image = report_image,
                reporter =user
            )

            new_report.save()
        
    return HttpResponseRedirect(reverse("report:main"))

