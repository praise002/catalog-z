from django.urls import path
from .import views

app_name = 'gallery'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    
    path('photos/', views.PhotoListView.as_view(), name="photo_list"),
    path('photo/<slug:slug>/', views.PhotoDetailView.as_view(), name="photo_detail"),
    
    path('videos/', views.VideoListView.as_view(), name="video_list"),
    path('video/<slug:slug>/', views.VideoDetailView.as_view(), name="video_detail"),
]
