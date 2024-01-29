from django.contrib import admin
from .models        import Item, ItemImage




class InlineStackImage(admin.TabularInline):
  
  model = ItemImage
  extra = 0

  verbose_name = "صورة"
  verbose_name_plural = "صور السلعة"



class ItemAdminStyle(admin.ModelAdmin):
  
  inlines = (
    InlineStackImage,
  )
  fieldsets = (
    (
      "العام", {
        "fields" : (
          "name_arabic",
          "description_arabic",
          "name_english",
          "description_english",
          "small_photo",
        )
      },
    ),
  )

  



admin.site.register(Item, ItemAdminStyle)
