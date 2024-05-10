from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login
import requests
from apps.accounts.mixins import LogoutRequiredMixin
from apps.accounts.models import User
from apps.accounts.senders import SendEmail
from decouple import config
# import sweetify

# class SignUpView(LogoutRequiredMixin, View):
#     def get(self, request):
#         GITHUB_CLIENT_ID = config("GITHUB_CLIENT_ID")
#         context = {
#             "GITHUB_CLIENT_ID": GITHUB_CLIENT_ID,
#         }
#         return render(request, "login.html", context=context)

# class GithubSignup(LogoutRequiredMixin, View):
#     def get(self, request):
#         GITHUB_CLIENT_ID = config("GITHUB_CLIENT_ID")
#         GITHUB_CLIENT_SECRET = config("GITHUB_CLIENT_SECRET")
#         code = request.GET.get("code") # retrieves authorization code
#         url = "https://github.com/login/oauth/access_token"
#         headers1 = {
#             "Accept": "application/json"
#         }
#         body = {
#             "client_id": GITHUB_CLIENT_ID,
#             "client_secret": GITHUB_CLIENT_SECRET,
#             "code": code,
#             "accept": "json"
#         }
#         response = requests.post(url, json=body, headers=headers1)
#         status_code = response.status_code
#         data = response.json()
        
#         if status_code == 200:
#             if "error" in data.keys():
#                 error = data["error_description"]
#                 # sweetify.error(self.request, error)
#                 return HttpResponse(error) 
#             access_token = data["access_token"]
#             headers2 = {
#                 "Accept": "application/json",
#                 "Authorization": f"Bearer {access_token}",
#             }
#             url = "https://api.github.com/user"
#             response = requests.get(url, headers=headers2)
#             user_data = response.json()
            
#             email = user_data["email"]
#             name = user_data["name"]
#             first_name, last_name = name.split(' ', 1)
#             photo_url = user_data["avatar_url"]
#             user, created = User.objects.get_or_create(
#                 email=email,
#                 defaults = {
#                     "first_name": first_name,
#                     "last_name": last_name
#                 }
#             )
#             if created:
#                 user.photo = photo_url
#                 user.is_email_verified = True  
#                 user.save()
#                 SendEmail.welcome(request, user)
#             login(request, user)
#             return redirect('/')
        
#         else:
#             error = data["error_description"]
#             return HttpResponse(error)

# GITHUB_CLIENT_ID = config("GITHUB_CLIENT_ID")
# print("GITHUB_CLIENT_ID:", GITHUB_CLIENT_ID)          
# def signup_view(request):
#     # get request
#     GITHUB_CLIENT_ID = config("GITHUB_CLIENT_ID")
#     print("GITHUB_CLIENT_ID:", GITHUB_CLIENT_ID)
#     return render(request, "accounts/login.html", 
#                   {"GITHUB_CLIENT_ID": GITHUB_CLIENT_ID})

# configuring the redirect url
def github_signup(request):
    # 1. Request a users github identity
    # https://github.com/login/oauth/authorize?scope=user,user:email&client_id={{ GITHUB_CLIENT_ID }}
    # 2. Users are redirected back to your site by github
    GITHUB_CLIENT_ID = config("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET = config("GITHUB_CLIENT_SECRET")
    code = request.GET.get("code")
    # post request
    url = 'https://github.com/login/oauth/access_token'
    # response in json
    headers1 = {        
        'Accept': 'application/json'
    }
    body = {"client_id": GITHUB_CLIENT_ID, "client_secret": GITHUB_CLIENT_SECRET, "code":code, "accept":"json"}
    resp = requests.post(url, json=body, headers=headers1)  
    status_code = resp.status_code
    data = resp.json()
    if status_code < 400:       
        if 'error' in data.keys():            
            error = data['error_description']
            return HttpResponse(error) 
        # 3. Use the access token to access the API
        access_token = data['access_token']        
        headers1 = {        
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}',
        } 
        # makes request to the API on behalf of the user: get request
        url = 'https://api.github.com/user'        
        resp = requests.get(url,headers=headers1) 
        data = resp.json()
        
        email = data['email']
        print(email)
        name = data['name']
        print("Name", name)
        firstname, lastname = name.split(' ', 1)
        print(f"FirstName: {firstname} LastName: {lastname}")
        avatar_url = data['avatar_url']  
        print("Avatar url", avatar_url) 
        user, created = User.objects.get_or_create(email=email, defaults={'first_name': firstname, 'last_name': lastname})      
        print(f"User: {user} Created: {created}")
        login(request, user)     
        return redirect("/")     
    else:
        error = data['error_description']
        return HttpResponse(error)   
