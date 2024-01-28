from django.shortcuts import render
from .models import Communicate, SlideImage, ServiceImage, ProjectImage, Testimonial, Logo, AboutText, WhyUs, FreeQuote
from django.http import HttpResponse
from django.http import HttpResponseNotFound

from urunler.models import Product, Category, CatFloor
from urunler.views import Category, Product
import folium
from folium.plugins import FastMarkerCluster

categories = Category.objects.all()
products = Product.objects.all()

# cat_floor = CatFloor.objects.all()
# floor = Floor.objects.all()


floor_categories = CatFloor.objects.all()
communication_info = Communicate.objects.first()
slide_images = SlideImage.objects.all()


# service_image = ServiceImage.objects.first()
def index(request):
    service_images = ServiceImage.objects.all()

    quote = FreeQuote.objects.get()
    project_images = ProjectImage.objects.all()
    testimonials = Testimonial.objects.all()
    logo_images = Logo.objects.all()
    about_text = AboutText.objects.first()
    wyh_us = WhyUs.objects.first()
    
    context = {
            'communication_info': communication_info,
            'slide_images': slide_images,
            'service_images': service_images,
            'project_images': project_images,
            'testimonials': testimonials,
            'logo_images': logo_images,
            'about_text': about_text,
            'why_us': wyh_us,
            'quote': quote,
            'categories': categories,
            'products': products,
            'floor_categories': floor_categories,
            # 'cat_floor': cat_floor,
            # 'floor': floor,                                     
        }
    
    return render(request, 'index.html', context)




def about(request):
    logo_images = Logo.objects.all()
    about_text = AboutText.objects.first()
    wyh_us = WhyUs.objects.get()
    
    context = {
            'communication_info': communication_info,
            'logo_images': logo_images,
            'about_text': about_text,
            'why_us': wyh_us,
            'categories': categories,
            'products': products,
            'floor_categories': floor_categories,
        }
    
    return render(request, "about.html", context)

def service(request):
    service_images = ServiceImage.objects.all()
    testimonials = Testimonial.objects.all()
    logo_images = Logo.objects.all()
    quote = FreeQuote.objects.get()
    
    context = {
            'communication_info': communication_info,
            'service_images': service_images,
            'testimonials': testimonials,
            'logo_images': logo_images,
            'quote': quote,
            'categories': categories,
            'products': products,
            'floor_categories': floor_categories,
        }
    
    return render(request, "service.html", context)

def project(request):
    project_images = ProjectImage.objects.all()
    logo_images = Logo.objects.all()
    
    context = {
            'communication_info': communication_info,
            'project_images': project_images,
            'logo_images': logo_images,
            'categories': categories,
            'products': products,
            'floor_categories': floor_categories,
        }
    
    return render(request, "project.html", context)

def feature(request):
    logo_images = Logo.objects.all()
    wyh_us = WhyUs.objects.get()
    
    context = {
            'communication_info': communication_info,
            'logo_images': logo_images,
            'why_us': wyh_us,
            'categories': categories,
            'products': products,
            'floor_categories': floor_categories,
        }
    
    return render(request, "feature.html", context)

def freequote(request):
    logo_images = Logo.objects.all()
    quote = FreeQuote.objects.get()
    
    context = {
            'communication_info': communication_info,
            'logo_images': logo_images,
            'quote': quote,
            'categories': categories,
            'products': products,
            'floor_categories': floor_categories,
        }
    
    return render(request, "freequote.html", context)



def testimonial(request):
    testimonials = Testimonial.objects.all()
    logo_images = Logo.objects.all()
    
    context = {
            'communication_info': communication_info,
            'testimonials': testimonials,
            'logo_images': logo_images,
            'categories': categories,
            'products': products,
            'floor_categories': floor_categories,
        }
    
    return render(request, "testimonial.html", context)


def contact(request):
    logo_images = Logo.objects.all()
    
    context = {
            'communication_info': communication_info,
            'logo_images': logo_images,
            'categories': categories,
            'products': products,
            'floor_categories': floor_categories,   
        }
    
    return render(request, "contact.html", context)
    
def error(request, exception):
    logo_images = Logo.objects.all()
    
    context = {
            'communication_info': communication_info,
            'logo_images': logo_images
        }
    
    return render(request, "error.html", context, status=404 )
    


def show_location(request): 
    #! koordinat bilgilerini daha sonra guncelleyebilmek icin model olusturup admin paneline kayit edilecek
    latitude = 40.1956
    longitude = 29.0601
    
    m = folium.Map(location=[latitude, longitude], width='50%', height='50%', zoom_start=13)
    
    folium.Marker([latitude, longitude], popup='Bursa').add_to(m)
    
    m = m._repr_html_()
    
    context = {
        # 'map': m,
        'latitude': latitude,
        'longitude': longitude, 
    }
    
    return render(request, "components/contact/map.html", context)
    





