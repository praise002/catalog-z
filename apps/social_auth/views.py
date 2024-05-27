import secrets, hashlib, base64
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login
from django.urls import reverse
import requests
from apps.accounts.mixins import LogoutRequiredMixin
from apps.accounts.models import User
from apps.accounts.senders import SendEmail
from decouple import config
import sweetify

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
        if email is None: # if not email
            sweetify.error(request, 'Public Email Confirmation')
            # use js to display what is similar to what i screenshot
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

# TODO: SWITCH to class-based views later
def facebook_signup(request):
    code = request.GET.get("code")  # authorization code
    app_id = config("FACEBOOK_APP_ID")
    app_secret = config("FACEBOOK_SECRET")
    redirect_uri = config("FACEBOOK_REDIRECT_URL")
    http_headers = {
        "Content-Type": "application/json",
    }
    # Exchanging Code for an Access Token
    url = f"https://graph.facebook.com/v19.0/oauth/access_token?client_id={app_id}&redirect_uri={redirect_uri}&client_secret={app_secret}&code={code}"
    response = requests.get(url, headers=http_headers)
    data = response.json()
    access_token = data["access_token"]
    
    # get user.id with access token
    url = f"https://graph.facebook.com/{id}?fields=id,name,email,picture&access_token={access_token}"
    response = requests.get(url, headers=http_headers)
    data = response.json()
    
    id = data["id"]
    name = data["name"]
    first_name, last_name = name.split(' ', 1)
    email = data["email"]
    picture = data["picture"]["data"]["url"]
    user, created = User.objects.get_or_create(email=email, 
                                               defaults={
                                                   "first_name": first_name,
                                                   "last_name": last_name
                                               })
    if created:
        user.photo = picture
        user.is_email_verified = True  
        user.save()
        SendEmail.welcome(request, user)
    login(request, user)
    return redirect("/")

def google_signin(request):
    access_token = request.GET.get("access_token")
    if access_token:
        headers1 = {
            "Content-Type": "application/json",
            "Connection": "Keep-Alive",
            "Authorization": f"Bearer {access_token}",
        }
        url = "https://people.googleapis.com/v1/people/me?personFields=emailAddresses,names,photos"
        response = requests.get(url, headers=headers1)
        data = response.json()
        status_code = response.status_code
        if status_code == 200:
            family_name = data["names"][0]["family_name"]
            given_name = data["names"][0]["given_name"]
            email = data["email_addresses"][0]["value"]
            photo = data["photos"][0]["url"]
            user, created = User.objects.get_or_create(email=email, defaults={
                "first_name": family_name,
                "last_name": given_name,
            })
            if created:
                user.photo = photo
                user.is_email_verified = True  
                user.save()
                SendEmail.welcome(request, user)
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("error")
        
    return render(request, "accounts/login.html")

def linkedin_signup(request):
    code = request.GET.get("code")  # auth token
    headers1 = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "Keep-Alive"
    }
    LINKEDIN_CLIENT_ID = config("LINKEDIN_CLIENT_ID")
    LINKEDIN_CLIENT_SECRET = config("LINKEDIN_CLIENT_SECRET")
    LINKEDIN_REDIRECT_URL = config("LINKEDIN_REDIRECT_URL")  
    # get access token
    body = {
        "grant_type": "authorization_code",
        "client_secret": LINKEDIN_CLIENT_SECRET, 
        "client_id": LINKEDIN_CLIENT_ID, 
        "code": code, 
        "redirect_uri": LINKEDIN_REDIRECT_URL
    }
    response = requests.post("https://www.linkedin.com/oauth/v2/accessToken", 
                             data=body, headers=headers1)
    data = response.json()
    status_code = response.status_code
    
    if status_code == 200:
        # get user info
        token = data["access_token"]
        headers1 = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "Keep-Alive",
        "Authorization": f"Bearer {token}",
        }   
            
        resp = requests.get("https://api.linkedin.com/v2/userinfo",headers=headers1) 
        data = resp.json()
        status_code = resp.status_code
        if status_code == 200:
            name = data["name"]
            given_name = data["given_name"]
            family_name = data["family_name"]
            email = data["email"]
            picture = data["picture"]
            user, created = User.objects.get_or_create(email=email, defaults={
                "first_name": family_name,
                "last_name": given_name
            })
            if created:
                user.photo = picture
                user.is_email_verified = True  
                user.save()
                SendEmail.welcome(request, user)
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("error")
    
    else:
        return HttpResponse("error")
    
def generate_state():
    return secrets.token_urlsafe(16)

def generate_code_verifier():
    return base64.urlsafe_b64encode(secrets.token_bytes(32))\
        .rstrip(b"=").decode("utf-8")
        
def generate_code_challenge(code_verifier):
    code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(code_challenge)\
        .rstrip("b=").decode("utf-8")
        
def twitter_signup(request):
    state = generate_state()
    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge()
    
    # Store the state and code_verifier in the session for later use
    request.session["oauth_state"] = state
    request.session["code_verifier"] = code_verifier
    
    client_id = config("TWITTER_CLIENT_ID")
    redirect_uri = config("TWITTER_REDIRECT_URL")
    scope = "users.read offline.access"
    
    auth_url = (
        f"https://twitter.com/i/oauth2/authorize"
        f"?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
        f"&scope={scope}&state={state}&code_challenge={code_challenge}&code_challenge_method=S256"
    )
    print(auth_url)
    return redirect(auth_url)

def twitter_callback(request):
    # request.GEt is a dict but doesn't raise a keyError if the key doesn not exist
    # using .get() returns None by default and you can even specify a
    # second argument as default value
    state = request.GET.get("state")
    code = request.GET.get("code")
    
    if state != request.session.pop("oauth_state", None):
        sweetify.error(request, "State mismatch. Possible CSRF attack.")
        return redirect("accounts:login")
    
    code_verifier = request.session.pop("code_verifier", None)
    token_url = "https://api.twitter.com/2/oauth2/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": config("TWITTER_CLIENT_ID"),
        "client_secret": config("TWITTER_CLIENT_SECRET"),
        "code": code,
        "redirect_uri": request.build_absolute_uri(reverse('twitter_callback')),
        "code_verifier": code_verifier,
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(token_url, data=data, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        name = user_data.get("name", "")
        first_name, last_name = name.split(" ", 1)
        email = user_data.get("email", "")
        picture = user_data.get("profile_image_url", "")
        user, created = User.objects.get_or_create(email=email, defaults={
                "first_name": first_name,
                "last_name": last_name
            })
        if created:
            user.photo = picture
            user.is_email_verified = True  
            user.save()
            SendEmail.welcome(request, user)
        login(request, user)
        return redirect("/")
       
    else:
        sweetify.error(request, "Failed to obtain access token.")
        return redirect("accounts:login")