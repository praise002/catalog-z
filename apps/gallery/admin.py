from django.contrib import admin
from .models import Photo, Video, Tag

class PhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "views", "downloads", "created_at", "created_by")
    list_filter = ("created_at", "tags")
    search_fields = ("title",)
    readonly_fields = ("slug",)
    date_hierarchy = 'created_at'
    ordering = ("created_at",)
    
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "views", "downloads", "created_at", "created_by")
    list_filter = ("created_at", "tags")
    search_fields = ("title",)
    readonly_fields = ("slug",)
    date_hierarchy = 'created_at'
    ordering = ("created_at",)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Tag, TagAdmin)