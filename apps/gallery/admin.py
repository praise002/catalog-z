from typing import Any
from django.contrib import admin
from moviepy.editor import VideoFileClip
from io import BytesIO
from .models import Photo, Video, Tag, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("created_at",)
    readonly_fields = ("slug",)
    
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "views", "downloads", "created_at", "created_by")
    list_filter = ("created_at", "tags")
    search_fields = ("title",)
    readonly_fields = ("slug", "id")
    date_hierarchy = 'created_at'
    ordering = ("created_at",)
    
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "views", "downloads", "created_at", "created_by")
    list_filter = ("created_at", "tags")
    search_fields = ("title",)
    readonly_fields = ("slug",)
    date_hierarchy = 'created_at'
    ordering = ("created_at",)
    
    # def save_model(self, request, obj, form, change):
    #     # calculate video duration
    #     video_path = obj.video.url
    #     clip =  VideoFileClip(video_path)
    #     obj.duration = clip.duration
    #     clip.close()
            
    #     # save the model instance
    #     super().save_model(request, obj, form, change)
    # TODO: WORK ON THIS

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ("slug",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Tag, TagAdmin)
