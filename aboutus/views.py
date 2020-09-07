from django.shortcuts import render
from .models import AbaoutUs, WhyChooseUs, Chef

# Create your views here.

def about_us_list(request):

    about_us_list = AbaoutUs.objects.all()
    why_choose_us_list = WhyChooseUs.objects.all()
    chefs = Chef.objects.all()

    context = {
        "about_us_list": about_us_list,
        "why_choose_us_list": why_choose_us_list,
        "chefs": chefs,
    }

    return render(request, "aboutus/about.html", context)