from django import views
from django.contrib import admin
from django.urls import URLPattern, path,include
from . import views

urlpatterns = [
    path('',views.livefe, name="index")
    # path('admin/', admin.site.urls),
]
