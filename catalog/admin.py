from django.contrib import admin
from .models import CatalogGranite, CatalogBelenco, CatalogCimstone, CatalogCalisco, CatalogGraniteKitchen, CatalogMarble, FAQ, ContactText
from django.utils.html import format_html, strip_tags

class BaseCatalogAdmin(admin.ModelAdmin):
    list_display = ['display_text', 'display_image']
    
    def display_text(self, obj):
        return strip_tags(obj.text)

    display_text.short_description = 'Ürün İsmi'
        
    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)

    display_image.short_description = 'Ürün Fotoğrafi'


@admin.register(CatalogGranite)
class GraniteAdmin(BaseCatalogAdmin):
    pass

@admin.register(CatalogBelenco)
class BelencoAdmin(BaseCatalogAdmin):
    pass

@admin.register(CatalogCimstone)
class CimstoneAdmin(BaseCatalogAdmin):
    pass

@admin.register(CatalogCalisco)
class CaliscoAdmin(BaseCatalogAdmin):
    pass

@admin.register(CatalogGraniteKitchen)
class GraniteKitchenAdmin(BaseCatalogAdmin):
    pass

@admin.register(CatalogMarble)
class MarbleAdmin(BaseCatalogAdmin):
    pass

class FAQAdmin(admin.ModelAdmin):
    list_display = ['display_question', 'display_answer']
    
    def display_question(self, obj):
        return strip_tags(obj.question)

    display_question.short_description = 'Soru'
        
    def display_answer(self, obj):
        return strip_tags(obj.answer)

    display_answer.short_description = 'Cevap'
    
    
class ContactTextAdmin(admin.ModelAdmin):
    list_display = ['display_text']
    
    def display_text(self, obj):
        return strip_tags(obj.text)




admin.site.register(FAQ, FAQAdmin)
admin.site.register(ContactText, ContactTextAdmin)



