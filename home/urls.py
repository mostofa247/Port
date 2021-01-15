from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('',views.home, name="home"),
    path('about',views.about,name="about"),
    path('projects',views.projects,name="projects"),
    path('contact',views.contact,name="contact")
]

#django admin site customize
admin.site.site_header = "Developer Mostofa"
admin.site.site_title = "Welcome to Dashboard"
admin.site.index_title = "Welcome to portal"