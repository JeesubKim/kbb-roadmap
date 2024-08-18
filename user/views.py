from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse, QueryDict,JsonResponse
import json
# from rest_framework import permissions, viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from serializer import UserSerializer
# Create your views here.

def main(request):
    return render(request, 'user/main.html')



def login(request):
    return render(request, 'user/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def get_user_by_name(request):
    queries = QueryDict(request.META.get("QUERY_STRING", None))
    user_name = queries.get("name", None)
    
    users = get_user_model().objects.filter(username__contains=user_name)
    users_list = list(users)
    
    """
    Cannot resolve keyword 'name' into field. 
    Choices are: 
    comment_likes, date_joined, email, emailaddress, first_name, groups, id, is_active, is_staff, 
    is_superuser, last_login, last_name, logentry, notificationstatus, password, roadmap_assignee, 
    roadmap_comment_author, roadmap_requester, roadmapagreement, roadmapcomplete, socialaccount, 
    user, user_permissions, username
    """
    # 
    # return HttpResponse(json.dumps({"user_name":user_name}))
    return JsonResponse({"users":[{"id":u.id, "name":u.username} for u in users_list]})





# def google_login(request):
#     scope = GOOGLE_SCOPE_USERINFO + GOOGLE_SCOPE_DRIVE
#     client_id = CLIENT_ID
#     return redirect(f"{GOOGLE_REDIRECT}?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")