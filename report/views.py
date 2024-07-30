from django.shortcuts import render
from .forms import ReportForm
# Create your views here.

def main(request):

    return render(request, 'report/report.html')

def new_report(request):


    if request.method == "GET":
        context = {
            "form": ReportForm()
        }
        return render(request, 'report/report_create.html', context=context)
    elif request.method == "POST":
        pass
    return render(request, 'report/report.html')

