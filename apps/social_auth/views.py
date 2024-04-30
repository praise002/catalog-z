from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from apps.accounts.mixins import LogoutRequiredMixin
from apps.accounts.models import User
from decouple import config
import sweetify

class SignUpView(LogoutRequiredMixin, View):
    def get(self, request):
        GITHUB_CLIENT_ID = config("GITHUB_CLIENT_ID")
        context = {
            "GITHUB_CLIENT_ID": GITHUB_CLIENT_ID,
        }
        return render(request, "login'html", context=context)

class GithubSignup(LogoutRequiredMixin, View):
    def get(self, request):
        GITHUB_CLIENT_ID = config("GITHUB_CLIENT_ID")
        GITHUB_CLIENT_SECRET = config("GITHUB_CLIENT_SECRET")
        code = request.GET.get("code") # retrieves authorization code
        url = "https://github.com/login/oauth/access_token"
        headers1 = {
            "Accept": "application/json"
        }
        body = {
            "client_id": GITHUB_CLIENT_ID,
            "client_secret": GITHUB_CLIENT_SECRET,
            "code": code,
            "accept": "json"
        }
        response = request.post(url, json=body, headers=headers1)
        status_code = response.status_code
        data = response.json()
        
        if status_code < 400:
            if "error" in data.keys():
                error = data["error_description"]
                # sweetify.error(self.request, error)
                return HttpResponse(error) 
            access_token = data["access_token"]
            headers1 = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}",
            }
            url = "https://api.github.com/user"
            data = response.json()
            
            email = data["email"]
            name = data["name"]
            first_name, last_name = name.split(' ', 1)
            photo_url = data["photo_url"]
            user = User.objects.create(
                username=email,
                defaults = {
                    "first_name": first_name,
                    "last_name": last_name
                }
            )
                