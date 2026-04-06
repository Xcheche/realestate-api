from django.contrib import admin
from . models import UserAccount
# Register your models here.


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("is_active", "email", "name", "is_realtor", "is_staff")
    list_display_links = ("email",)
    list_filter = ("is_realtor", "is_staff", "is_active")
    search_fields = ("email", "name")
    ordering = ("email",)
    list_editable = ("is_realtor", "is_staff", "is_active")



admin.site.register(UserAccount, UserAccountAdmin)
