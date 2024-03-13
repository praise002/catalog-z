from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from autoslug import AutoSlugField
from apps.common.models import BaseModel

class Photo(BaseModel):
    title = models.CharField(_("Title"), max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    description = models.TextField(default="Aliquam varius posuere nunc, nec imperdiet neque condimentum at. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Please support us by contributing a small donation via PayPal.")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")  
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="photos", on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)  
    downloads = models.PositiveIntegerField(default=0)  
    dimension = models.CharField(max_length=50)  
    format = models.CharField(_("Format"), max_length=20)  
    license = models.TextField(_("License"), 
                               default="Free for both personal and commercial use. No need to pay anything. No need to make any attribution.") 
    tags = models.ManyToManyField("Tag", related_name="photos")  

    def __str__(self):
        return self.title
    
class Video(BaseModel):
    title = models.CharField(_("Title"), max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    description = models.TextField(default="Aliquam varius posuere nunc, nec imperdiet neque condimentum at. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Please support us by contributing a small donation via PayPal.")
    video = models.FileField(upload_to="videos//%Y/%m/%d/")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="videos", on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)  
    downloads = models.PositiveIntegerField(default=0)  
    resolution = models.CharField(max_length=50)  
    format = models.CharField(_("Format"), max_length=20)  
    duration = models.DurationField()
    license = models.TextField(_("License"), 
                               default="Free for both personal and commercial use. No need to pay anything. No need to make any attribution.") 
    tags = models.ManyToManyField("Tag", related_name="videos")  
    
    def __str__(self):
        return self.title

class Tag(models.Model):  #TODO: Might split to a different app
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        return self.name