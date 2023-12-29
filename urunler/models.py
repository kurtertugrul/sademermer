from django.db import models

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
    
