
from django.contrib import admin
from django.urls import path
from . import views


admin.site.site_header = "Prajwal Sapaliya Editz"
admin.site.site_title = "Prajwal Sapaliya title"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('base',views.base,name="base"),
    path('pricing',views.pricing,name="pricing"),
    path('testimonial',views.testimonial,name="testimonial"),
    path('contact',views.contactme,name="contactme"),
    path('aboutme',views.aboutme,name="aboutme")
    
]
