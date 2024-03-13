from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import SiteDetail, Address, Contact, Employee

class SiteDetailAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        obj, created = self.model.objects.get_or_create()
        return HttpResponseRedirect(
            reverse(
                f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change",
                args=(obj.id,),
            )  # app_label=general, model_name=SiteDetail
        )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    list_filter = ("created_at", "subject")
    date_hierarchy = "created_at"
    ordering = ("created_at",)

class AddressAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        obj, created = self.model.objects.get_or_create()
        return HttpResponseRedirect(
            reverse(
                f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change",
                args=(obj.id,),
            )  # app_label=general, model_name=Address
        )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class EmployeeAdmin(admin.ModelAdmin):  #TODO: 4 employees to be displayed
    list_display = ("name")

