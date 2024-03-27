from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse
from autoslug import AutoSlugField
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video
from apps.common.models import BaseModel

class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)
    image = models.ImageField(default="fallback.jpg", upload_to="category/%Y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    # TODO: FIX ISSUE WITH DEFAULT IMAGE NOT WORKING
    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = "/static/media/fallback.jpg"
        return url  # TODO: NOT WORKING

    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Photo(BaseModel):
    title = models.CharField(_("Title"), max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    description = models.TextField(default="Aliquam varius posuere nunc, nec imperdiet neque condimentum at. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Please support us by contributing a small donation via PayPal.")
    photo = models.ImageField(default="fallback.jpg", upload_to="photos/%Y/%m/%d/")  
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="photos", on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)  
    downloads = models.PositiveIntegerField(default=0)  
    dimension = models.CharField(max_length=50)  
    format = models.CharField(_("Format"), max_length=20)  
    license = models.TextField(_("License"), 
                               default="Free for both personal and commercial use. No need to pay anything. No need to make any attribution.") 
    tags = models.ManyToManyField("Tag", related_name="photos")  
    caption = models.CharField(_("Caption"), max_length=10, default="Untitled")
    category = models.ForeignKey(Category, related_name="photos", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("gallery:photo_detail", args=[self.slug])
    
    
class Video(BaseModel):
    title = models.CharField(_("Title"), max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    description = models.TextField(default="Aliquam varius posuere nunc, nec imperdiet neque condimentum at. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Please support us by contributing a small donation via PayPal.")
    video = models.FileField(upload_to="videos/%Y/%m/%d/",
                             storage=VideoMediaCloudinaryStorage(),
                             validators=[validate_video])  
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="videos", on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)  
    downloads = models.PositiveIntegerField(default=0)  
    resolution = models.CharField(max_length=50)  
    format = models.CharField(_("Format"), max_length=20)  
    duration = models.CharField(default="00:00:20")
    license = models.TextField(_("License"), 
                               default="Free for both personal and commercial use. No need to pay anything. No need to make any attribution.") 
    tags = models.ManyToManyField("Tag", related_name="videos")  
    caption = models.CharField(_("Caption"), max_length=10, default="Untitled")
    category = models.ForeignKey(Category, related_name="videos", on_delete=models.CASCADE, blank=True, null=True)
    # thumbnail = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("gallery:video_detail", args=[self.slug])

class Tag(models.Model):  #TODO: Might split to a different app
    name = models.CharField(_("Name"), max_length=50)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)

    def __str__(self):
        return self.name