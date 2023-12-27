from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
# Create your models here.

class CatalogBase(models.Model):
    text = RichTextField(blank=True, null=True, max_length=150)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        abstract = True

    def __str__(self):
        return self.text

class CatalogGranite(CatalogBase):
    class Meta:
        verbose_name = 'Granit Doseme Katalog'
        verbose_name_plural = 'Granit Doseme Katalog '

class CatalogBelenco(CatalogBase):
    class Meta:
        verbose_name = 'Belenco Katalog'
        verbose_name_plural = 'Belenco Katalog '

class CatalogCimstone(CatalogBase):
    class Meta:
        verbose_name = 'Cimstone Katalog'
        verbose_name_plural = 'Cimstone Katalog '

class CatalogCalisco(CatalogBase):
    class Meta:
        verbose_name = 'Calisco Katalog'
        verbose_name_plural = 'Calisco Katalog '

class CatalogGraniteKitchen(CatalogBase):
    class Meta:
        verbose_name = 'Granit Mutfak Tezgahi Katalog'
        verbose_name_plural = 'Granit Mutfak Tezgahi Katalog'

class CatalogMarble(CatalogBase):
    class Meta:
        verbose_name = 'Mermer Mutfak Tezgahi Katalog'
        verbose_name_plural = 'Mermer Mutfak Tezgahi Katalog'
        
class FAQ(models.Model):
    question = RichTextField(null=True, blank=True, max_length=500)
    answer = RichTextField(null=True, blank=True, max_length=500)
    
    class Meta:
        verbose_name = 'Soru-Cevap'
        verbose_name_plural = 'Sikça Sorulan Sorular'
        
    def __str__(self):
        return f'Sikça Sorulan Sorular'
    
class ContactText(models.Model):
    text = RichTextField(null=True, blank=True, max_length=500)
    
    class Meta:
        verbose_name = 'Bize Ulaşin'
        verbose_name_plural = 'Bize Ulaşin Yazisi'
        
    def __str__(self):
        return f'Bize Ulaşin Yazisi'
        
