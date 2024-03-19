from django.shortcuts import render
from django.views import View
# from apps.accounts.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Photo, Video, Tag, Category

class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        
        context = {
            "categories": categories
        }
        return render(request, 'gallery/home.html', context)
    
        # TODO: return latest photos and use pagination
