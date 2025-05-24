from django.db import models

from projects.service import optimize_image


class SEOData(models.Model):
    meta_title = models.CharField(max_length=55, verbose_name="Meta Title")
    meta_description = models.CharField(max_length=158, verbose_name="Meta Description")
    meta_keywords = models.CharField(max_length=158, blank=True, verbose_name="Meta Keywords - separated by commas")

    og_title = models.CharField(max_length=55, blank=True, verbose_name="OG Title")
    og_description = models.CharField(max_length=158, blank=True, verbose_name="OG Description")
    og_image = models.ImageField(upload_to='seo/og_images/', verbose_name="OG Image")

    def save(self, *args, **kwargs):
        if not self.og_title:
            self.og_title = self.meta_title
        if not self.og_description:
            self.og_description = self.meta_description
        super().save(*args, **kwargs)


class Feedback(models.Model):
    fullname = models.CharField(max_length=100, verbose_name='Fullname')
    service = models.CharField(max_length=100, verbose_name='Service')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=100, null=True, blank=True, verbose_name='Phone')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"


class MainBanner(models.Model):
    banner_image = models.ImageField(upload_to='banners', verbose_name='Main Banner image', null=True, blank=True)
    banner_description = models.TextField(verbose_name='Main Banner Description')

    def save(self, *args, **kwargs):
        if self.banner_image:
            optimized_image = optimize_image(self.banner_image, max_size=(1920, 1080), format='WEBP', quality=85)
            if optimized_image:
                self.banner_image = optimized_image
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class ContactPage(MainBanner, SEOData):
    banner_slogan = models.CharField(max_length=256, verbose_name='Main Banner slogan')
    banner_title = models.CharField(max_length=256, verbose_name='Main Banner title')
    banner_image = models.ImageField(upload_to='contact', verbose_name=' ', null=True, blank=True)
    location_title = models.CharField(max_length=256, verbose_name='Location Title')
    location_description = models.TextField(verbose_name='Location Description')
    call_title = models.CharField(max_length=256, verbose_name='Call Title')
    call_number = models.CharField(max_length=256, verbose_name='Call Number')
    email_title = models.CharField(max_length=256, verbose_name='Email Title')
    email_address = models.EmailField(verbose_name='Email Address')
    working_hours_title = models.CharField(max_length=256, verbose_name='Working Hours Title')
    working_hours_description = models.TextField(verbose_name='Working Hours Description')
    our_location_description = models.TextField(verbose_name='Our Location Description')

    def __str__(self):
        return 'Contact Page Configurations'

    class Meta:
        verbose_name = 'Contact Page'
        verbose_name_plural = 'Contact Page'