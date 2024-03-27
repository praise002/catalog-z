from django.shortcuts import render, redirect
from django.views import View
from .models import SiteDetail, Address, Employee
from .forms import ContactForm

import sweetify

class AboutView(View):
    def get(self, request):
        sitedetail, created = SiteDetail.objects.get_or_create()
        context = {"sitedetail": sitedetail}
        return render(request, "general/about.html", context)

class ContactView(View):
    def get(self, request):
        form = ContactForm()
        address, created = Address.objects.get_or_create()
        employees = Employee.objects.all()[:4]
        sitedetail, created = SiteDetail.objects.get_or_create()
        context = {
            "form": form,
            "address": address,
            "employees": employees,
            "sitedetail": sitedetail
            }
        return render(request, "general/contact.html", context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 
                             title="Sent",
                             message = "Your message was sent successfully",
                             timer=3000,
                             )
            return redirect("general:contact")
            
        context = {"form": form}
        return render(request, "general/contact.html", context)