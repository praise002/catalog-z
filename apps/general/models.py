from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

class SiteDetail(models.Model):
    title = models.CharField(default="About Catalog-Z")
    description = models.TextField(default="Pellentesque urna odio, scelerisque eu mauris vitae, vestibulum sodales neque. Ut augue justo, tincidunt nec aliquet ac, cursus vel augue. Suspendisse vel quam imperdiet, sodales tellus sed, ullamcorper lorem. Suspendisse id consequat risus. Aliquam varius posuere nunc, nec imperdiet neque condimentum at. Aenean porta eleifend venenatis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.")
    maps_url = models.URLField(
        default="https://maps.google.com/maps?q=Av.+L%C3%BAcio+Costa,+Rio+de+Janeiro+-+RJ,+Brazil&t=&z=13&ie=UTF8&iwloc=&output=embed"
    )
    

    fb = models.URLField(verbose_name=_("Facebook"), default="https://www.facebook.com")
    ig = models.URLField(
        verbose_name=_("Instagram"), default="https://www.instagram.com/"
    )
    tw = models.URLField(verbose_name=_("Twitter"), default="https://www.twitter.com/")
    pinterest = models.URLField(
        verbose_name=_("Pinterest"), default="https://www.pinterest.com/"
    )
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self._state.adding and SiteDetail.objects.exists():
            raise ValidationError(_("Only one site detail object can be created."))
        return super(SiteDetail, self).save(*args, **kwargs)

    
class Contact(models.Model):
    class Subject(models.TextChoices):
        SALES_AND_MARKETING = "Sales and Marketing", "Sales and Marketing"
        CREATIVE_DESIGN = "Creative Design", "Creative Design"
        UI_UX = "UI/UX", "UI/UX"

    name = models.CharField(_("Name"), max_length=200)
    email = models.EmailField(_("Email"), max_length=200)
    subject = models.CharField(max_length=200, 
                               choices=Subject.choices,
                               default=Subject.UI_UX)
    message = models.TextField(_("Message"))
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-created_at"]
        
class Address(models.Model):
    description = models.TextField(default="Quisque eleifend mi et nisi eleifend pretium. Duis porttitor accumsan arcu id rhoncus. Praesent fermentum venenatis ipsum, eget vestibulum purus. Nulla ut scelerisque elit, in fermentum ante. Aliquam congue mattis erat, eget iaculis enim posuere nec. Quisque risus turpis, tempus in iaculis. 120-240 Fusce eleifend varius tempus Duis consectetur at ligula 10660")
    email = models.EmailField(default="info@comapany.com")
    tel = models.CharField(default="010-020-0340")
    url = models.URLField(default="www.comapany.com")
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self._state.adding and Address.objects.exists():
            raise ValidationError(_("Only one address object can be created."))
        return super(Address, self).save(*args, **kwargs)

ROLE_CHOICES = (
    ("CO-Founder", "CO-Founder"),
    ("General Manager", "General Manager"),
    ("Chief Executive Officer", "Chief Executive Officer"),
    ("Chief Marketing Officer", "Chief Marketing Officer"),
    ("Accounting Executive", "Accounting Executive"),
    ("Creative Art Director", "Creative Art Director"),
)
class Employee(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, choices=ROLE_CHOICES)
    description = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="team/")
    fb = models.URLField(verbose_name=_("Facebook"), default="https://www.facebook.com")
    tw = models.URLField(verbose_name=_("Twitter"), default="https://www.twitter.com/")
    ln = models.URLField(
        verbose_name=_("Linkedin"), default="https://www.linkedin.com/"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    @property
    def photo_url(self):
        try:
            url = self.avatar.url
        except:
            url = ""
        return url
    
