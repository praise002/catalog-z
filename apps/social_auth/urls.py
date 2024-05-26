from django.urls import path
from .import views

app_name = "social_auth"

urlpatterns = [
    # path("", views.signup_view, name="signup"),
    # path("", views.SignUpView.as_view(), name="signup"),
    # path("signup/github/", views.GithubSignup.as_view(), name="github_signup"),
    # path("github/", views.github_signup, name="github_signup"),
    path("facebook/", views.facebook_signup, name="facebook_signup"),
]