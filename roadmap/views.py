from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RoadmapNameForm
# Create your views here.


def main(request):
    return render(request, "roadmap/roadmap.html")



def new_roadmap(request):
    if request.method == "GET":

        # context = {
        #     "roadmap_items": [
        #         {
        #             "class":"roadmap_name",
        #             "type":"text",
        #             "label":"로드맵 이름",
        #             "options":[],
                    
        #         },
                
        #     ]
        # }
        
        
        # return render(request, "roadmap/roadmap_create.html", context=context)

        context = {
            "form": RoadmapNameForm()
        }
        return render(request, "roadmap/roadmap_create.html", context=context)
    elif request.method == "POST":
        form = RoadmapNameForm(request.POST)

        if form.is_valid():
            roadmap_name = form.cleaned_data["roadmap_name"]

            return HttpResponseRedirect("roadmap/")
        
