from django.shortcuts import render
from django.views import View
# from apps.accounts.mixins import LoginRequiredMixin

class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, 'gallery/home.html', context)
        # TODO: return latest photos and use pagination
