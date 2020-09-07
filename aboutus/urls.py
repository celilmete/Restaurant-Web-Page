from django.urls import path
from . import views

app_name = "aboutus"

urlpatterns = [
    path('',views.about_us_list, name="about_us_list")
]