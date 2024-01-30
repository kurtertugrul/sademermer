from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=50)

    

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tezgahlar'
        
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tezgah Çeşitleri'
        

class CatFloor(models.Model):
    name = models.CharField(max_length=50)

    

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Döşeme Çeşitleri'

class Floor(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CatFloor, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Dosemeler'
        
        

class FAQ(models.Model):
    question = RichTextField(null=True, blank=True, max_length=500)
    answer = RichTextField(null=True, blank=True, max_length=500)
    
    class Meta:
        verbose_name = 'Soru-Cevap'
        verbose_name_plural = 'Sikça Sorulan Sorular'
        
    def __str__(self):
        return f'Sikça Sorulan Sorular'
    
