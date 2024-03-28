# from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from apps.accounts.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Photo, Video, Tag, Category
from .forms import PhotoForm, VideoForm
import sweetify

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
    def get(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, slug=kwargs["slug"])
        
        # Get related photos based on shared tags
        related_photos = Photo.objects.filter(tags__in=photo.tags.all())\
            .exclude(id=photo.id).distinct()
        
            
        context = {
            "photo": photo,
            "related_photos": related_photos
        }
        return render(request, "gallery/photos/photo_detail.html", context)

class VideoListView(View):
    def get(self, request):
        videos = Video.objects.all().order_by("-created_at")
        paginator = Paginator(videos, 16)  # num of photos per page
        page = request.GET.get("page")
        
        try:
            video_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page
            video_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results
            video_list = paginator.page(paginator.num_pages)
        
        context = {
            "videos": videos,
            "video_list": video_list
        }    
        return render(request, "gallery/videos/video_list.html", context)
     
class VideoDetailView(View):
    def get(self, request, *args, **kwargs):
        video = get_object_or_404(Video, slug=kwargs["slug"])
        
         # Get related photos based on shared tags
        related_videos = Video.objects.filter(tags__in=video.tags.all())\
            .exclude(id=video.id).distinct()
            
        context = {
            "video": video,
            "related_videos": related_videos
        }
        return render(request, "gallery/videos/video_detail.html", context)
    

class PhotoListByTagView(View):
    def get(self, request, *args, **kwargs):
        # tag_slug = kwargs.get("tag_slug")
        tag_slug = kwargs["tag_slug"]
        print(tag_slug)
        tag = get_object_or_404(Tag, slug=tag_slug)
        print(tag)
        photos = Photo.objects.filter(tags__slug=tag_slug)
        print(photos)
        
        context = {
            "tag": tag,
            "photos": photos
        }
        return render(request, "gallery/photos/photo_list.html", context)

class VideoListByTagView(View):
    def get(self, request, *args, **kwargs):
        # tag_slug = kwargs.get("tag_slug")
        tag_slug = kwargs["tag_slug"]
        print(tag_slug)
        tag = get_object_or_404(Tag, slug=tag_slug)
        print(tag)
        videos = Video.objects.filter(tags__slug=tag_slug)
        print(videos)
        
        context = {
            "tag": tag,
            "videos": videos
        }
        return render(request, "gallery/videos/video_list.html", context)

class SubmitPhotoView(LoginRequiredMixin, View):
    def get(self, request):
        form = PhotoForm()
        context = {"form": form}
        return render(request, "gallery/photos/submit_photo.html", context)
    
    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.created_by = request.user  
            photo.save()
                
            sweetify.success(request, 
                             title="Submitted",
                             message = "Submitted")
            return redirect("gallery:home")
        
        context = {"photo": photo}
        return render(request, "gallery/photos/submit_photo.html", context)
    
class SubmitVideoView(LoginRequiredMixin, View):
    def get(self, request):
        form = VideoForm()
        context = {"form": form}
        return render(request, "gallery/videos/submit_video.html", context)
    
    def post(self, request):
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.created_by = request.user
            video.save()
            sweetify.success(request, 
                             title="Submitted",
                             message = "Submitted")
            return redirect("gallery:home")
        
        context = {"form": form}
        return render(request, "gallery/videos/submit_video.html", context)