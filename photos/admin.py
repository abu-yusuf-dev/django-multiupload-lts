from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
  list_display = ('file', 'uploaded_at')

admin.site.register(Photo, PhotoAdmin)