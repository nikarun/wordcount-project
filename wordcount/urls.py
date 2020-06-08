

from django.urls import path
from django.contrib import admin
from count.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home,name="home"),
path('countwords/',count,name="count"),
    path('mywebpage',arun_bio,name="Arun_Bio")

]
