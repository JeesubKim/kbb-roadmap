from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, "roadmap/roadmap.html")



def new_roadmap(request):
    if request.method == "GET":

        context = {
            "roadmap_items": [
                {
                    "class":"roadmap_name",
                    "type":"text",
                    "label":"로드맵 이름",
                    "options":[],
                    
                },
                
            ]
        }
        
        return render(request, "roadmap/roadmap_create.html", context=context)
    elif request.method == "POST":
        pass
