from decouple import config

def social_auth(request):
    GITHUB_CLIENT_ID = config("GITHUB_CLIENT_ID")
    return {"GITHUB_CLIENT_ID": GITHUB_CLIENT_ID}
