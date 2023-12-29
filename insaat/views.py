from django.shortcuts import render
from .models import Communicate, SlideImage, ServiceImage, ProjectImage, Testimonial, Logo, AboutText, WhyUs, FreeQuote
from django.http import HttpResponse
from django.http import HttpResponseNotFound

from urunler.models import Product, Category, CatFloor
from urunler.views import Category, Product

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
    return render(request, 'index.html', {'communication_info': communication_info,
                                          'slide_images': slide_images,
                                          'service_images': service_images,
                                          'project_images': project_images,
                                          'testimonials': testimonials,
                                          "logo_images": logo_images,
                                          'about_text': about_text,
                                          'why_us': wyh_us,
                                          'quote': quote,
                                          'categories': categories,
                                          'products': products,
                                          'floor_categories': floor_categories,
                                        #   'cat_floor': cat_floor,
                                        #   'floor': floor,
                                          
                                          })




def about(request):
    logo_images = Logo.objects.all()
    about_text = AboutText.objects.first()
    wyh_us = WhyUs.objects.get()
    return render(request, "about.html", {'communication_info': communication_info,
                                          "logo_images": logo_images,
                                          'about_text': about_text,
                                          'why_us': wyh_us,
                                          'categories': categories,
                                          'products': products,
                                          'floor_categories': floor_categories,
                                          })

def service(request):
    service_images = ServiceImage.objects.all()
    testimonials = Testimonial.objects.all()
    logo_images = Logo.objects.all()
    quote = FreeQuote.objects.get()
    return render(request, "service.html", {'communication_info': communication_info,
                                            'service_images': service_images,
                                            'testimonials': testimonials,
                                            "logo_images": logo_images,
                                            'quote': quote,
                                            'categories': categories,
                                            'products': products,
                                            'floor_categories': floor_categories,
                                            })

def project(request):
    project_images = ProjectImage.objects.all()
    logo_images = Logo.objects.all()
    return render(request, "project.html", {'communication_info': communication_info,
                                            'project_images': project_images,
                                            "logo_images": logo_images,
                                            'categories': categories,
                                            'products': products,
                                            'floor_categories': floor_categories,})

def feature(request):
    logo_images = Logo.objects.all()
    wyh_us = WhyUs.objects.get()
    return render(request, "feature.html", {'communication_info': communication_info,
                                            "logo_images": logo_images,
                                            'why_us': wyh_us,
                                            'categories': categories,
                                            'products': products,
                                            'floor_categories': floor_categories,
                                            })

def freequote(request):
    logo_images = Logo.objects.all()
    quote = FreeQuote.objects.get()
    return render(request, "freequote.html", {'communication_info': communication_info,
                                              "logo_images": logo_images,
                                              'quote': quote,
                                            'categories': categories,
                                            'products': products,
                                            'floor_categories': floor_categories,})



def testimonial(request):
    testimonials = Testimonial.objects.all()
    logo_images = Logo.objects.all()
    return render(request, "testimonial.html", {'communication_info': communication_info,
                                                'testimonials': testimonials,
                                                "logo_images": logo_images,
                                                'categories': categories,
                                                'products': products,
                                                'floor_categories': floor_categories,})


def contact(request):
    logo_images = Logo.objects.all()
    return render(request, "contact.html", {'communication_info': communication_info,
                                            "logo_images": logo_images,
                                            'categories': categories,
                                            'products': products,
                                            'floor_categories': floor_categories,   
                                            })
    
def error(request, exception):
    logo_images = Logo.objects.all()
    
    return render(request, "error.html", {'communication_info': communication_info,
                                          'logo_images': logo_images},
                  status=404 )
    










