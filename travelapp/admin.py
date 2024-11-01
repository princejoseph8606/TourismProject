from django.contrib import admin
from .models import Profile, TravelPackage

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'vendor', 'tour_date', 'is_approved')
    actions = ['approve_packages']

    def approve_packages(self, request, queryset):
        queryset.update(is_approved=True)
    approve_packages.short_description = "Approve selected packages"
