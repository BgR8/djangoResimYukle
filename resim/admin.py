from django.contrib import admin
from .models import Resim

# Register your models here.
class ResimAdmin(admin.ModelAdmin):
    list_display = ['title', 'image',]
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Resim, ResimAdmin)