from django.urls import path
from .import views

app_name = 'gallery'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('photos/', views.PhotoListView.as_view(), name="photo_list"),
]
