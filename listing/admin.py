from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ("is_published", "title", "price", "city", "date_created", "is_deleted")
    list_display_links = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("is_published", "city", "state", "is_deleted", "date_created")
    search_fields = ("title", "description")
    ordering = ("-date_created",)
    list_editable = ("is_published", "price", "is_deleted")


    actions = ('restore_selected', 'soft_delete_selected', 'hard_delete_selected')

    def get_queryset(self, request):
        # Show both active and soft-deleted rows in admin.
        return self.model.all_objects.all()

    @admin.action(description='Restore selected listings')
    def restore_selected(self, request, queryset):
        queryset.restore()

    @admin.action(description='Soft delete selected listings')
    def soft_delete_selected(self, request, queryset):
        queryset.delete()

    @admin.action(description='Hard delete selected listings permanently')
    def hard_delete_selected(self, request, queryset):
        queryset.hard_delete()

    def delete_model(self, request, obj):
        # Admin single-object delete should use soft delete by default.
        obj.delete()

    def delete_queryset(self, request, queryset):
        # Admin bulk delete should use soft delete by default.
        queryset.delete()
    




admin.site.register(Listing, ListingAdmin)

# Register your models here.
