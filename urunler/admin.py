
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product, CatFloor, Floor, FAQ

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image_display',)
    list_filter = ('category',)
    search_fields = ('name', 'category__name',)

    def image_display(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')

    image_display.short_description = 'Image'
    
    
@admin.register(CatFloor)
class CatFloorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image_display',)
    list_filter = ('category',)
    search_fields = ('name', 'category__name',)

    def image_display(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')

    image_display.short_description = 'Image'
    
admin.site.register(FAQ)
    


