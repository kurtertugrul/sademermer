from django.contrib import admin
from .models import Communicate, SlideImage, ServiceImage, ProjectImage, Testimonial, Logo, AboutText, WhyUs, FreeQuote
from django.utils.html import format_html, strip_tags



    
admin.site.site_header = 'Sade Mermer Yönetim Paneli'
admin.site.site_title = 'Sade Mermer'
admin.site.index_title = 'Yönetim Paneli'



    

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['display_project_title', 'display_project_choices', 'display_project_image']

    def display_project_title(self, obj):
        return obj.project_title

    display_project_title.short_description = 'Projenin Başlığı'

    def display_project_choices(self, obj):
        return obj.project_choices

    display_project_choices.short_description = 'Projenin Seçeneği'

    def display_project_image(self, obj):
        if obj.project_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.project_image.url)
        return None

    display_project_image.short_description = 'Fotoğraf'
    
    
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['display_fullname', 'display_says', 'display_jobs','display_image']
    
    
    def display_fullname(self, obj):
        return obj.fullname
    
    display_fullname.short_description = 'İsim'
    
    
    def display_says(self, obj):
        return obj.says
    
    display_says.short_description = 'Ne Söyledi'
    
      
    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
    
    display_image.short_description = 'Fotograf'
    
       
    def display_jobs(self, obj):
        return obj.jobs
    
    display_jobs.short_description = 'Mesleği'
    

class SlideImageAdmin(admin.ModelAdmin):
    list_display = ['display_h5_text', 'display_h1_text', 'display_p_text', 'display_image']
    
    def display_h5_text(self, obj):
        return strip_tags(obj.h5_text)
    
    display_h5_text.short_description = 'Küçük Yazi'
    
    def display_h1_text(self, obj):
        return strip_tags(obj.h1_text)
    
    display_h1_text.short_description = 'Büyük Yazi'
    
    def display_p_text(self, obj):
        return strip_tags(obj.p_text)
    
    display_p_text.short_description = 'Açiklama Yazisi'
    
    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>', obj.image.url)
    
    display_image.short_description = 'Fotoğraf'
    
    
class CommunicateAdmin(admin.ModelAdmin):
    list_display = ['display_phone_number',
                    'display_address',
                    'display_hour',
                    'display_facebook_link',
                    'display_x_link',
                    'display_instagram_link',
                    'display_linkedin_link',
                    'display_mail']
    
    def display_phone_number(self,obj):
        return obj.phone_number
    
    display_phone_number.short_description = 'Telefon Numarasi'
    
    def display_address(self, obj):
        return obj.address
    
    display_address.short_description = 'Adres'
    
    def display_hour(self, obj):
        return obj.hour 
    
    display_hour.short_description = 'Açiliş Kapaniş Saatleri'
    
    def display_facebook_link(self, obj):
        return obj.facebook_link
    
    display_facebook_link.short_description = 'Facebook Hesabi Link Olarak'
    
    def display_x_link(self, obj):
        return obj.x_link
    
    display_x_link.short_description = 'Twitter Hesabi Link Olarak'
    
    def display_instagram_link(self, obj):
        return obj.instagram_link
    
    display_instagram_link.short_description = 'Instagram Hesabi Link Olarak'
    
    def display_linkedin_link(self, obj):
        return obj.linkedin_link
    
    display_linkedin_link.short_description = 'Linkedin Hesabi Link Olarak'
    
    def display_mail(self, obj):
        return obj.mail

    display_mail.short_description = 'Mail Adresi'
    


class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ['display_title', 'display_description', 'display_image']
 
    def display_title(self, obj):
        return obj.title
    
    display_title.short_description = 'Başlik'
    
    def display_description(self, obj):
        return obj.description
    
    display_description.short_description = 'Açiklama'
    
    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
    
    display_image.short_description = 'Fotoğraf'

class LogoAdmin(admin.ModelAdmin):
    list_display = ['display_image']

    def display_image(self, obj):
        return format_html('<img src = "{}" width="50" height="50" />', obj.image.url)
    
    display_image.short_description = "Logo"
    
admin.site.register(Logo, LogoAdmin)
admin.site.register(Communicate, CommunicateAdmin)
admin.site.register(SlideImage, SlideImageAdmin)
admin.site.register(ServiceImage, ServiceImageAdmin)
admin.site.register(ProjectImage, ProjectAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(AboutText)
admin.site.register(WhyUs)
admin.site.register(FreeQuote)

