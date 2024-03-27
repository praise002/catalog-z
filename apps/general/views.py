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
        context = {"form": form}
        return render(request, "general/about.html", context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 
                             title="Sent",
                             message = "Your message was sent successfully",
                             timer=3000,
                             )
            return redirect("gallery:contact")
            
        context = {"form": form}
        return render(request, "general/about.html", context)

class AddressView(View):
    def get(self, request):
        address, created = Address.objects.get_or_create()
        context = {"address": address}
        return render(request, "general/contact.html", context)
    
class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all()[:4]
        context = {"employees": employees}
        return render(request, "general/employees.html", context)