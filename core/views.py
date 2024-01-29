from django.shortcuts  import redirect, render
from django.http       import HttpRequest, HttpResponse
from .models           import Item, ItemImage




def landing(req:HttpRequest, lang="EN") -> HttpResponse:

  chosen = "landing"
  vars_to_front_end = {
    "lang" : lang,
    "chosen" : chosen,
    "items"  : Item.objects.all()
  }
  
  return render(req, "pages/landing.html", vars_to_front_end)





def about_us(req:HttpRequest, lang="EN") -> HttpResponse:
  
  chosen = 'about us' 
  vars_to_front_end = {
    "lang" : lang,
    'chosen' : chosen
    
  }
  
  return render(req, "pages/landing.html", vars_to_front_end)







def services(req:HttpRequest, lang="EN") -> HttpResponse:
  
  
  vars_to_front_end = {
    "lang" : lang,
    'chosen': 'services'
  }
  
  return render(req, "pages/landing.html", vars_to_front_end)



def contact(req:HttpRequest, lang="EN") -> HttpResponse:
  
  
  vars_to_front_end = {
    "lang" : lang,
    "chosen" : "contact"
  }
  
  return render(req, "pages/landing.html", vars_to_front_end)




def item_detail(req, lang, item_pk):
  
  
  var  = {
    "lang" : lang
  }
  
  return render(req, "pages/item_detail.html", var )