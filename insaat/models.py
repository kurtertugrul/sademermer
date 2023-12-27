from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField





class Communicate(models.Model):
    phone_number = models.CharField(null=True, blank=True, max_length=100)
    address = models.CharField(null=True, blank=True, max_length=100)
    hour = models.CharField(null=True, blank=True, max_length=100)
    facebook_link = models.CharField(null=True, blank=True, max_length=100)
    x_link = models.CharField(null=True, blank=True, max_length=100)
    instagram_link = models.CharField(null=True, blank=True, max_length=100)
    linkedin_link = models.CharField(null=True, blank=True, max_length=100)
    mail = models.CharField(null=True, blank=True, max_length=100)
    
    class Meta:
        verbose_name = 'sosyal medya hesabı'
        verbose_name_plural = 'Sosyal Medya Hesapları'
    
    def __str__(self):
        return f'İletişim Bilgileri'

class SlideImage(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    h5_text = RichTextField(null=True, blank=True, max_length=150)
    h1_text = RichTextField(null=True, blank=True, max_length=150)
    p_text = RichTextField(null=True, blank=True, max_length=150)    
    
    class Meta:
        verbose_name = 'site sileder'
        verbose_name_plural = 'Site Slider Ayarları'
    
    def __str__(self):
        return f'Ana Sayfa Kayan Fotoğraflar Ve Yazıları'
    
class ServiceImage(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    title = models.CharField(null=True, blank=True, max_length=50)
    description = models.CharField(null=True, blank=True, max_length=500)
    
    class Meta:
        verbose_name = 'iş'
        verbose_name_plural = 'Servisler'
    
    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project_image = models.ImageField(null=True, blank=True, upload_to="images/")
    project_title = models.CharField(null=True, blank=True, max_length=50)
    project_choices = models.CharField(null=True, blank=True, max_length=50)
    
    PROJECT_CHOICES = [
        ('General', 'General Carpentry'),
        ('Custom', 'Custom Carpentry'),
        # Add other choices if needed
    ]

    project_choices = models.CharField(
        max_length=20,
        choices=PROJECT_CHOICES,
        default='General',
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'  
    
    def __str__(self):
        return self.project_title
        

    
class Testimonial(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    says = models.CharField(null=True, blank=True, max_length=500)
    fullname = models.CharField(null=True, blank=True, max_length=50)
    jobs = models.CharField(null=True, blank=True, max_length=50)
    
    class Meta:
        verbose_name = 'referans'
        verbose_name_plural = 'Referanslar'  


    def __str__(self):
        return f'Referanslar'
    
class Logo(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Firma Logosu'
        
    def __str__(self):
        return f'Logolar'
  
class AboutText(models.Model):
    text = RichTextField(blank=True, null=True, max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    class Meta:
        verbose_name = 'Hakkimizda'
        verbose_name_plural = 'Hakkimizda Yazisi'
        
    def __str__(self):
        return f'Hakkimizda Yazisi'
  
class WhyUs(models.Model):
    text = RichTextField(blank=True, null=True, max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    class Meta:
        verbose_name = 'Neden Biz'
        verbose_name_plural = 'Neden Biz Yazisi'
        
    def __str__(self):
        return f'Neden Biz?'
    
class FreeQuote(models.Model):
    text = RichTextField(blank=True, null=True, max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    class Meta:
        verbose_name = 'Fiyat Teklifi'
        verbose_name_plural = 'Fiyat Teklifi Yazisi'
        
    def __str__(self):
        return f'Fiyat Teklifi'
    

class FAQ(models.Model):
    question = RichTextField(null=True, blank=True, max_length=500)
    answer = RichTextField(null=True, blank=True, max_length=500)
    
    class Meta:
        verbose_name = 'Soru-Cevap'
        verbose_name_plural = 'Sikça Sorulan Sorular'
        
    def __str__(self):
        return f'Sikça Sorulan Sorular'
    









  