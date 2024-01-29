from django.contrib import admin

# Register your models here.
from .models import Website

admin.site.index_title = "zix"
admin.site.site_header = "ZIX"
admin.site.site_title  = "ZIX"

class AdminModel(admin.ModelAdmin):
  pass



admin.register(Website,AdminModel)