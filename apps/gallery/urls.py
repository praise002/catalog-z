from django.urls import path
from .import views

app_name = 'gallery'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    
    path('photos/', views.PhotoListView.as_view(), name="photo_list"),
    path('photos/tag/<slug:tag_slug>/', views.PhotoListByTagView.as_view(), name='photo_list_by_tag'),
    path('photo/<slug:slug>/', views.PhotoDetailView.as_view(), name="photo_detail"),
    
    path('videos/', views.VideoListView.as_view(), name="video_list"),
    path('videos/tag/<slug:tag_slug>/', views.VideoListByTagView.as_view(), name='video_list_by_tag'),
    path('video/<slug:slug>/', views.VideoDetailView.as_view(), name="video_detail"),
    
    path('submit/photo/', views.SubmitPhotoView.as_view(), name="submit_photo"),
    path('submit/video/', views.SubmitVideoView.as_view(), name="submit_video"),
    
    # path('search/', views.Search.as_view(), name="search"),
    path('search/', views.TrigramSearch.as_view(), name="search"),
    
    path('download/photo/<int:photo_id>/', views.download_photo, name="download_photo"),

]
