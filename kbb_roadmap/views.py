from django.http import HttpResponseRedirect

def is_authenticated(request):
    
    if not request.user.is_authenticated:
        return False
    
    return True
    

    
        
