from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.

def main(request):
    return render(request, 'user/main.html')



def login(request):
    return render(request, 'user/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


# def google_login(request):
#     scope = GOOGLE_SCOPE_USERINFO + GOOGLE_SCOPE_DRIVE
#     client_id = CLIENT_ID
#     return redirect(f"{GOOGLE_REDIRECT}?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")