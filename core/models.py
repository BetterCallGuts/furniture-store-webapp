from django.db import models




class Item(models.Model):
  
  name_arabic        = models.CharField(max_length=255, verbose_name="العنوان بالعربي")
  description_arabic = models.TextField(verbose_name="التفاصيل بالعربي")
  name_english       = models.CharField(max_length=255,verbose_name="العنوان بالإنجليزي")
  description_english= models.TextField(verbose_name="التفاصيل بالإنجليزي")
  small_photo        = models.ImageField(upload_to="small_photos",verbose_name="الصورة المصغرة",null=True, blank=True)
  
  
  def __str__(self):
    return f"{self.name_arabic}"
  
  class Meta:
    verbose_name        = "سلعة"
    verbose_name_plural = "عناصر"



class ItemImage(models.Model):
  image = models.ImageField(upload_to="item_photos", verbose_name="صورة للسلعة")
  itemf = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="السلعة")
  def __str__(self) -> str:
    return f"{self.itemf.name_arabic}"
  
  class Meta:
    
    verbose_name        = "صورة السلعة"
    verbose_name_plural = "صور السلع"