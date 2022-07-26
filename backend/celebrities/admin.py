from django.contrib import admin

from .models import Celebrity, Photo, Rating


@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "num_of_photos", "created_by"]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "celebrity", "photo", "ratings"]


admin.site.register(Rating)
