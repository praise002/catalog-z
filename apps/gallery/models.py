from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Photo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(default="Aliquam varius posuere nunc, nec imperdiet neque condimentum at. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Please support us by contributing a small donation via PayPal.")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")  
    created_at = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)  
    downloads = models.PositiveIntegerField(default=0)  
    dimension = models.CharField(max_length=50)  
    format = models.CharField(_("Format"), max_length=20)  
    license = models.TextField(_("License"), 
                               default="Free for both personal and commercial use. No need to pay anything. No need to make any attribution.") 
    tags = models.ManyToManyField("Tag", related_name="photos")  

    def __str__(self):
        return self.title
    
class Video(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(default="Aliquam varius posuere nunc, nec imperdiet neque condimentum at. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Please support us by contributing a small donation via PayPal.")
    video = models.FileField(upload_to="videos//%Y/%m/%d/")
    created_at = models.DateField(auto_now_add=True)
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

class Tag(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self):
        return self.name