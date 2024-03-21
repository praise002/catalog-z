from django.shortcuts import render, get_object_or_404
from django.views import View
# from apps.accounts.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Photo, Video, Tag, Category

class HomeView(View):
    def get(self, request):
        # Display categories
        categories = Category.objects.all()
        
        # Display Trending Photos 
        trending_photos = Photo.objects.filter(views__gte=1000, downloads__gte=500)
        
        # Display latest photos
        latest_photos = Photo.objects.all().order_by("-created_at")
        
        context = {
            "categories": categories,
            "trending_photos": trending_photos,
            "latest_photos": latest_photos,
        }
        return render(request, 'gallery/home.html', context)

class CategoryDetailView(View):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, slug=kwargs["slug"])
        photos = category.photos.all().order_by("-created_at") # retrieve all photos associated with d categ
        context = {
            "category": category,
            "photos": photos
        }
        return render(request, "gallery/category/category_detail.html", context)
        

class PhotoListView(View):
    def get(self, request):
        photos = Photo.objects.all().order_by("-created_at")
        paginator = Paginator(photos, 16)  # num of photos per page
        page = request.GET.get("page")
        
        try:
            photo_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page
            photo_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results
            photo_list = paginator.page(paginator.num_pages)
        
        context = {
            "photos": photos,
            "photo_list": photo_list
        }    
        return render(request, "gallery/photos/photo_list.html", context)

class PhotoDetailView(View):
    pass

class VideoListView(View):
    pass
     
class VideoDetailView(View):
    pass