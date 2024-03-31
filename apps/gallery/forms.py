from .models import Photo, Video
from django import forms

        
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("title", "description", "category", "dimension", "format",
                  "caption", "tags",  "photo")
        
    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        # Add bootstrap form control to field classes
        for key in self.fields:
            self.fields[key].widget.attrs["class"] = "form-control rounded-0"
            
        # Set placeholders for all fields
        self.fields["title"].widget.attrs["placeholder"] = "Enter a title"
        self.fields["description"].widget.attrs["placeholder"] = "Enter a description"
        self.fields["category"].widget.attrs["placeholder"] = "Select a Category" 
        self.fields["dimension"].widget.attrs["placeholder"] = "Enter the image dimension e.g 1920x1080"
        self.fields["format"].widget.attrs["placeholder"] = "Enter the image format e.g JPG"
        self.fields["caption"].widget.attrs["placeholder"] = "Enter a caption e.g CLOCKS"
        self.fields["tags"].widget.attrs["placeholder"] = "Choose tags"
        self.fields["photo"].widget.attrs["placeholder"] = "Upload image"
        
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("title", "description", "category", "resolution", "format",
                  "duration", "caption", "tags", "video")
        
    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        # Add bootstrap form control to field classes
        for key in self.fields:
            self.fields[key].widget.attrs["class"] = "form-control rounded-0"
            
        # Set placeholders for all fields
        self.fields["title"].widget.attrs["placeholder"] = "Enter a title"
        self.fields["description"].widget.attrs["placeholder"] = "Enter a description"
        self.fields["category"].widget.attrs["placeholder"] = "Select a Category"  
        self.fields["resolution"].widget.attrs["placeholder"] = "Enter the video resolution e.g 1920x1080"
        self.fields["format"].widget.attrs["placeholder"] = "Enter the video format e.g MP4"
        self.fields["duration"].widget.attrs["placeholder"] = "Enter the video duration e.g 00:00:20"
        self.fields["caption"].widget.attrs["placeholder"] = "Enter a caption e.g CLOCKS"
        self.fields["tags"].widget.attrs["placeholder"] = "Choose tags"
        self.fields["video"].widget.attrs["placeholder"] = "Upload video"
        
# TODO: SUPPORT MULTIPLE FILE UPLOADS, INLINE-FORMSET 

class SearchForm(forms.Form):
    query = forms.CharField()