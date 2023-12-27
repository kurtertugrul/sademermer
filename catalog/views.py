from django.shortcuts import render
from .models import CatalogGranite, CatalogBelenco, CatalogCimstone, CatalogCalisco, CatalogGraniteKitchen, CatalogMarble
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from insaat.models import Logo, Communicate
from django.conf import settings
import os




communication_info = Communicate.objects.first()


def catalog_granite(request):
    logo_images = Logo.objects.all()
    catalog_granite = CatalogGranite.objects.all()
    return render(request, 'catalog_granite.html', {'communication_info': communication_info,
                                                    'logo_images': logo_images,
                                                    'catalog_granite': catalog_granite
                                                    })


def catalog_belenco(request):
    logo_images = Logo.objects.all()
    catalog_belenco = CatalogBelenco.objects.all()
    return render(request, 'catalog_belenco.html', {'communication_info': communication_info,
                                                    'logo_images': logo_images,
                                                    'catalog_belenco': catalog_belenco
                                                    })
    
    
def catalog_cimstone(request):
    logo_images = Logo.objects.all()
    catalog_cimstone = CatalogCimstone.objects.all()
    return render(request, 'catalog_cimstone.html', {'communication_info': communication_info,
                                                    'logo_images': logo_images,
                                                    'catalog_cimstone': catalog_cimstone
                                                    })


def catalog_calisco(request):
    logo_images = Logo.objects.all()
    catalog_calisco = CatalogCalisco.objects.all()
    return render(request, 'catalog_calisco.html', {'communication_info': communication_info,
                                                    'logo_images': logo_images,
                                                    'catalog_calisco': catalog_calisco
                                                    })
    
def catalog_granite_kitchen(request):
    logo_images = Logo.objects.all()
    catalog_granite_kitchen = CatalogGraniteKitchen.objects.all()
    return render(request, 'catalog_granite_kitchen.html', {'communication_info': communication_info,
                                                    'logo_images': logo_images,
                                                    'catalog_granite_kitchen': catalog_granite_kitchen
                                                    })

def catalog_marble(request):
    logo_images = Logo.objects.all()
    catalog_marble = CatalogMarble.objects.all()
    return render(request, 'catalog_marble.html', {'communication_info': communication_info,
                                                    'logo_images': logo_images,
                                                    'catalog_marble': catalog_marble
                                                    })





# def download_catalog(request, catalog_name):
#     # Katalog isimlerini ve ilgili model sınıflarını eşleştirecek bir sözlük
#     catalog_mapping = {
#         'granite': CatalogGranite,
#         'belenco': CatalogBelenco,
#         'cimstone': CatalogCimstone,
#         'calisco': CatalogCalisco,
#         'granite_kitchen': CatalogGraniteKitchen,
#         'marble': CatalogMarble,
#     }

#     # Katalog ismi ile ilgili model sınıfını al
#     catalog_model = catalog_mapping.get(catalog_name)
#     if not catalog_model:
#         return HttpResponseNotFound("Geçersiz katalog ismi")

#     # Modeldeki tüm öğeleri al
#     catalog_items = catalog_model.objects.all()

#     # Katalog adını temizle (URL güvenli hale getir)
#     clean_catalog_name = catalog_name.replace('_', '-')

#     # İndirme bağlantısı oluştur
#     file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', f'{clean_catalog_name}_catalog.txt')
    
#     # Katalog içeriğini bir dosyaya yaz
#     with open(file_path, 'w') as file:
#         for item in catalog_items:
#             file.write(f"{item.text}\n")

#     # Dosyayı HttpResponse ile geri döndür
#     response = HttpResponse(content_type='text/plain')
#     response['Content-Disposition'] = f'attachment; filename="{clean_catalog_name}_catalog.txt"'

#     with open(file_path, 'r') as file:
#         response.write(file.read())

#     return response








