from django.urls import path
from .           import views


app_name = "core"

urlpatterns = [
  path('', views.landing, name='landing'),
path('<str:lang>', views.landing, name='landing'),
path('about-us/<str:lang>/', views.about_us, name='about us'),
path("services/<str:lang>/", views.services, name="services"),
path("contact/<str:lang>/", views.contact, name="contact"),
path("item-detail/<str:lang>/<int:item_pk>/", views.item_detail, name="item-detail")

]

  