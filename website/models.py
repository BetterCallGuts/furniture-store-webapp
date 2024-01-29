from django.db import models



class Website(models.Model):
  
  
  what_it_do        = models.CharField(max_length=255, )
  screenshottoit    = models.ImageField(upload_to="web_screen")
  arabic_transulate = models.TextField()
  english_trans     = models.TextField()
  pk_for_this_obj   = models.IntegerField(primary_key=True)

  

  def __str__(self):
    return f"{self.what_it_do}"
  
  class Meta:
    
    verbose_name        = "-"
    verbose_name_plural = "تعديل على الموقع"