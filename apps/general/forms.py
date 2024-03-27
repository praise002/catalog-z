from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message")
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # Add bootstrap form control to field classes
        for key in self.fields:
            print(key)
            self.fields[key].widget.attrs["class"] = "form-control rounded-0"
            
        # Set placeholders for all fields
        self.fields["name"].widget.attrs["placeholder"] = "Name"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["subject"].widget.attrs["placeholder"] = "Subject"
        self.fields["message"].widget.attrs["placeholder"] = "Message"
        
        # Set row for textarea
        self.fields["message"].widget.attrs["rows"] = "8"