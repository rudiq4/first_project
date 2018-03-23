from django.contrib import admin
from .models import *


class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VehicleType._meta.fields]

    class Meta:
        model = VehicleType


admin.site.register(VehicleType, VehicleTypeAdmin)


class VehicleImageInline(admin.TabularInline):
    model = VehicleImage
    extra = 3


class VehicleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vehicle._meta.fields]
    list_display_links = ('marka',)  # Клік по полю для редагування
    inlines = [VehicleImageInline]

    class Meta:
        model = Vehicle


admin.site.register(Vehicle, VehicleAdmin)


class VehicleImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VehicleImage._meta.fields]

    class Meta:
        model = VehicleImage


admin.site.register(VehicleImage, VehicleImageAdmin)
