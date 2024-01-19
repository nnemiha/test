from django.contrib import admin
from .models import Car, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Car, PostAdmin)