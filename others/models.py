from django.db import models


class SEOData(models.Model):
    meta_title = models.CharField(max_length=55, verbose_name="Meta Title")
    meta_description = models.CharField(max_length=158, verbose_name="Meta Description")
    meta_keywords = models.CharField(max_length=158, blank=True, verbose_name="Meta Keywords - separated by commas")

    og_title = models.CharField(max_length=55, blank=True, verbose_name="OG Title")
    og_description = models.CharField(max_length=158, blank=True, verbose_name="OG Description")
    og_image = models.ImageField(upload_to='seo/og_images/', blank=True, null=True, verbose_name="OG Image")

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

    class Meta:
        abstract = True